# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,20,30,40,50,60,66,192]

    for k in k_list:
        file_ideal_topk = 'raw_results/heart.xlsx'
        topk = ag.get_topk_aggregate(k, file_ideal_topk)
        print("Ideal topk", topk)
        percentage_list = [0,10,20,30,40,50,60,70,80,90]
        for percent in percentage_list:
            for i in range(100):
                try:
                    file_name = 'raw_results/db_' +str(percent) + 'rand_missing_predicate' + str(i+1) + '.xlsx'
                    for file_view in glob.glob(file_name):
                        print(percent, file_name, k)
                        missing = ag.get_topk_aggregate(k, file_view)
                        #print("Missing topk: ", missing)
                        #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                        #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                        with open('results/missing_predicate_vs_ideal.csv', 'a', newline='') as f:
                            fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                            writer = csv.writer(f)
                            writer.writerow(fields)
                except:
                    pass  # doing nothing on exception
                print("done")
