import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file1 = 'skew_kurtosis/positive_skew_missing_vs_ideal_random.csv'
input_file2 = 'skew_kurtosis/negative_skew_missing_vs_ideal_random.csv'
input_file3 = 'skew_kurtosis/positive_kurtosis_missing_vs_ideal_random.csv'
input_file4 = 'skew_kurtosis/negative_kurtosis_missing_vs_ideal_random.csv'

output_plot = 'skew_kurtosis_RBO_10_missing_attributes_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

percent = 10
#[5, 10, 15, 20, 100, 256]

kj15 = df[(df['k'] == 3) & (df['percentage'] == percent)]
kj15 = kj15['RBO']
kj110 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj110 = kj110['RBO']
kj115 = df[(df['k'] == 8) & (df['percentage'] == percent)]
kj115 = kj115['RBO']
kj120 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj120 = kj120['RBO']

kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,3)
kj15.insert(1,'RBO')
kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,5)
kj110.insert(1,'RBO')
kj115 = list(mean_confidence_interval(kj115))
kj115.insert(0,8)
kj115.insert(1,'RBO')
kj120 = list(mean_confidence_interval(kj120))
kj120.insert(0,10)
kj120.insert(1,'RBO')


df1 = pd.DataFrame([kj15, kj110, kj115,kj120])
df1.columns = ['k','measurement','mean','lb','ub']


df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])

kj25 = df[(df['k'] == 3) & (df['percentage'] == percent)]
kj25 = kj25['RBO']
kj210 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj210 = kj210['RBO']
kj215 = df[(df['k'] == 8) & (df['percentage'] == percent)]
kj215 = kj215['RBO']
kj220 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj220 = kj220['RBO']


kj25 = list(mean_confidence_interval(kj25))
kj25.insert(0,3)
kj25.insert(1,'RBO')
kj210 = list(mean_confidence_interval(kj210))
kj210.insert(0,5)
kj210.insert(1,'RBO')
kj215 = list(mean_confidence_interval(kj215))
kj215.insert(0,8)
kj215.insert(1,'RBO')
kj220 = list(mean_confidence_interval(kj220))
kj220.insert(0,10)
kj220.insert(1,'RBO')


df2 = pd.DataFrame([kj25, kj210, kj215,kj220])
df2.columns = ['k','measurement','mean','lb','ub']

df = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])


kj35 = df[(df['k'] == 3) & (df['percentage'] == percent)]
kj35 = kj35['RBO']
kj310 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj310 = kj310['RBO']
kj315 = df[(df['k'] == 8) & (df['percentage'] == percent)]
kj315 = kj315['RBO']
kj320 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj320 = kj320['RBO']


kj35 = list(mean_confidence_interval(kj35))
kj35.insert(0,3)
kj35.insert(1,'RBO')
kj310 = list(mean_confidence_interval(kj310))
kj310.insert(0,5)
kj310.insert(1,'RBO')
kj315 = list(mean_confidence_interval(kj315))
kj315.insert(0,8)
kj315.insert(1,'RBO')
kj320 = list(mean_confidence_interval(kj320))
kj320.insert(0,10)
kj320.insert(1,'RBO')


df3 = pd.DataFrame([kj35, kj310, kj315,kj320])
df3.columns = ['k','measurement','mean','lb','ub']


df = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])


kj45 = df[(df['k'] == 3) & (df['percentage'] == percent)]
kj45 = kj45['RBO']
kj410 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj410 = kj410['RBO']
kj415 = df[(df['k'] == 8) & (df['percentage'] == percent)]
kj415 = kj415['RBO']
kj420 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj420 = kj420['RBO']

kj45 = list(mean_confidence_interval(kj45))
kj45.insert(0,3)
kj45.insert(1,'RBO')
kj410 = list(mean_confidence_interval(kj410))
kj410.insert(0,5)
kj410.insert(1,'RBO')
kj415 = list(mean_confidence_interval(kj415))
kj415.insert(0,8)
kj415.insert(1,'RBO')
kj420 = list(mean_confidence_interval(kj420))
kj420.insert(0,10)
kj420.insert(1,'RBO')


df4 = pd.DataFrame([kj45, kj410, kj415,kj420])
df4.columns = ['k','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'RBO'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'RBO'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'RBO'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'RBO'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'RBO'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'RBO'].reset_index()
lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'RBO'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'RBO'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'RBO'].reset_index()
lb4 = lb4['lb']


# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 14))
# Font size to 14
matplotlib.rc('font', size = 25)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')


t = np.arange(len(mean1))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'Positive skewness', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'Negative skewness', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'Positive kurtosis', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Negative kurtosis', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness RBO")
x = [3, 5, 8, 10]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
