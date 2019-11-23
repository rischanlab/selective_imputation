import glob
import shutil

file_name = 'diabetes.xlsx'
full_name = 'raw_results/' + file_name

for i in range(100):
    src_dir = full_name

    dst_dir4 = "raw_results/db_0rand_missing_predicate" + str(i + 1) + ".xlsx"

    #shutil.copy(src_dir, dst_dir1)
    #shutil.copy(src_dir, dst_dir2)
    #shutil.copy(src_dir, dst_dir3)
    shutil.copy(src_dir, dst_dir4)

