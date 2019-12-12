
import aggregate_insight as ag

file_name = 'heart.xlsx'
k = 192
x = ag.get_unique(file_name, k)
print(x)