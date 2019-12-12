# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20, 80, 100, 256]

    for k in k_list:
        file_ideal_topk = 'raw_results/heart.xlsx'
        topk = ag.get_topk_aggregate(k, file_ideal_topk)
        print("Ideal topk", topk)
        percentage_list = [0,10,20,30]
        for percent in percentage_list:
            for i in range(100):
                file_name = 'raw_results/db_' +str(percent) + 'rand_missing_attr' + str(i+1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)
                    missing = ag.get_topk_aggregate(k, file_view)
                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/missing_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                        writer = csv.writer(f)
                        writer.writerow(fields)
