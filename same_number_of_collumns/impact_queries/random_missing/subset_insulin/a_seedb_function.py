# -*- coding:utf-8 -*-
import pandas as pd
import time,math,numpy as np
from itertools import combinations
from a_seedb_config import config_data
import matplotlib.pyplot as plt



class SeeDB:
    query_time,deviance_time,sort_time,div_time,visualization_time = 0,0,0,0,0
    def __init__(self, db,data_set,table,k):
        self.cursor = config_data(db)
        self.data_set, self.table,self.k = data_set, table, k
        self.terms()
        self.start = time.time()
        self.top_k = {}
        self.best_k = {}

    def terms(self):
        #self.where1,self.where2 = input('enter WHERE clause for q1->'),input('enter WHERE clause for q2->')
        self.where1, self.where2 = "insulin = 'Steady'", "insulin != 'Steady'"

    def query(self):
        #q = 'delete from ' + self.table + ' where not (' + self.table + ' is not null)'
        # if self.func == 'sum' or 'order_amount' in self.attribute1:
        #     query1 = 'select ' + self.attribute2 +',' + self.func + '(' + 'CAST(' + self.attribute1 + ' AS BIGINT' + '))' + ' from ' + self.table
        # else:
        query1 = 'select ' + self.attribute2 + ',' + self.func + '(' + self.attribute1 + ')' + ' from ' + self.table
        if self.where1 != '':
            query1 += ' where ' + self.where1
        query1 += ' and '  + self.attribute2 +  ' is not null and ' + self.attribute1 + ' is not null group by ' + self.attribute2 + ' order by ' + self.attribute2

        # if self.func == 'sum' or 'order_amount' in self.attribute1:
        #     query2 = 'select ' + self.attribute2 + ',' + self.func + '(' + 'CAST(' + self.attribute1 + ' AS BIGINT' + ')) ' + ' from ' + self.table
        # else:
        query2 = 'select ' + self.attribute2 +',' + self.func + '(' + self.attribute1 + ')' + ' from ' + self.table
        if self.where2 != '':
            query2 += ' where ' + self.where2
        query2 += ' and '  + self.attribute2 +  ' is not null and ' + self.attribute1 + ' is not null group by ' + self.attribute2 + ' order by ' + self.attribute2

        #self.cursor.execute(q)
        self.cursor.execute(query1)
        data1 = self.cursor.fetchall()
        self.cursor.execute(query2)
        data2 = self.cursor.fetchall()

        return data1,data2

    def nomalization(self, data):
        #print(data)
        z,sum_x = tuple(),0
        for x,y in data:
            sum_x += y
        for x,y in data:
            z += ( (x , y/sum_x), )
        return z

    def distance(self):
        # make queries and execute these
        a = time.time()
        x,y = self.query()
        self.query_time += time.time() - a

        # calclate deviance
        deviance = 0
        a = time.time()
        x,y = self.nomalization(x),self.nomalization(y)
        dd = dict()
        for i, j in x:
            dd[i] = j
        for i, j in y:
            if i in dd:
                dd[i] = math.fabs(dd[i] - j)
            else:
                dd[i] = j
        for x, dis in dd.items():
            deviance += float(dis)
        self.deviance_time += time.time() - a

        return math.sqrt(deviance)

    def cheak_k(self,d):
        # preprocessing
        if self.attribute1 == '*':
            self.attribute1 = '.'+self.attribute1
        # cheak deviance and sort results
        if len(self.top_k) == 0:
            self.top_k[0] = (d,(self.func,self.attribute1,self.attribute2))
        elif len(self.top_k) < self.k:
            target = (d, (self.func,self.attribute1, self.attribute2))
            for i, j in self.top_k.items():
                if j[0] < target[0]:
                    self.top_k[i] = target
                    target = j
            self.top_k[len(self.top_k)] = target
        else:
            target = (d,(self.func,self.attribute1,self.attribute2))
            for i,j in self.top_k.items():
                if j[0] < target[0]:
                    self.top_k[i] = target
                    target = j

    def get_best_k(self,d):
        # preprocessing
        if self.attribute1 == '*':
            self.attribute1 = '.'+self.attribute1
        # cheak deviance and sort results
        if len(self.best_k) == 0:
            self.best_k[0] = (d,(self.func,self.attribute1,self.attribute2))
        # elif len(self.best_k) > self.k:
        #     target = (d, (self.func,self.attribute1, self.attribute2))
        #     for i, j in self.best_k.items():
        #         if j[0] < target[0]:
        #             self.best_k[i] = target
        #             target = j
        #     self.best_k[len(self.best_k)] = target
        else:
            target = (d,(self.func,self.attribute1,self.attribute2))
            for i,j in self.best_k.items():
                if j[0] < target[0]:
                    self.best_k[i] = target
                    target = j
            self.best_k[len(self.best_k)] = target

    def visualization(self):
        # setting n*m
        n = math.ceil(np.sqrt(self.k))
        m = math.ceil(self.k / n)
        fig, axes = plt.subplots(nrows=n, ncols=m, figsize=(10, 8))
        ii = 0
        for dis,dt in self.top_k.items():
            if '*' in dt[1][1]:
                self.attribute1, self.attribute2, self.func = dt[1][1].split('.')[1], dt[1][2], dt[1][0]
            else:
                self.attribute1, self.attribute2, self.func = dt[1][1], dt[1][2], dt[1][0]
            data1, data2 = self.query()
            data1, data2 = self.nomalization(data1), self.nomalization(data2)
            x_agre = list()
            for i, j in data1 + data2:
                if not i in x_agre:
                    x_agre.append(i)
            t1, t2 = dict(data1), dict(data2)
            x, y1, y2 = [i for i in range(0, len(x_agre))], list(), list()
            for i in x_agre:
                if i in t1:
                    y1.append(t1[i])
                else:
                    y1.append(0)
                if i in t2:
                    y2.append(t2[i])
                else:
                    y2.append(0)
            axes[int(ii/m), ii%m].plot(x, y1, linewidth=2)
            axes[int(ii/m), ii%m].plot(x, y2, linewidth=2)
            axes[int(ii/m), ii%m].set_xticks(x)
            axes[int(ii/m), ii%m].set_xticklabels(x_agre, rotation=30)
            axes[int(ii/m), ii%m].set_title(ii)
            axes[int(ii/m), ii%m].set_xlabel(self.attribute2)
            axes[int(ii/m), ii%m].grid(True)
            ii+=1
            if ii > self.k:
                break
        plt.savefig('sample.png')
        plt.show()

    def store_result(self, table):
        data_result = []
        for i,j in self.best_k.items():
            data_result.append([i+1,j[1][2],j[1][1],j[1][0],j[0]])
        writer = pd.ExcelWriter('raw_results/' + table + '.xlsx')
        df = pd.DataFrame(data_result, columns=['ID','Attributes', 'Meassure', 'Function', 'Utility'])
        df.to_excel(writer,'Sheet1', index=0)
        writer.save()

    def output(self):
        print('================================================================')
        print('Query time:',self.query_time)
        print('Utility time:',self.deviance_time+self.sort_time)
        print('Total view processing time:',time.time()-self.start)
       

    def visualize(self):
        print('================================================================')
        print('Visualization time:',self.visualization_time)

    def main(self):
        # roop
        for self.attribute2, ite in self.data_set.items():
            for self.func, self.attribute1 in ite:
                # calclate euclid distance
                d = self.distance()
                # sort results
                a = time.time()
                # if d != -1 and d<1:
                #self.store_result(d)
                self.cheak_k(d)
                self.get_best_k(d)
                self.sort_time += time.time() - a
            #print(time.time() - self.start)
        self.output()
        self.store_result(self.table)
