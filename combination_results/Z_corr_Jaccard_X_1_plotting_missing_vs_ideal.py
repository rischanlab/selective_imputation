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

input_file1 = 'correlation/positive_corr_missing_vs_ideal.csv'
input_file2 = 'correlation/negative_corr_missing_vs_ideal.csv'
input_file3 = 'correlation/positive_corr_v2_missing_vs_ideal_zipf.csv'
input_file4 = 'correlation/negative_corr_v2_missing_vs_ideal_zipf.csv'

output_plot = 'jaccard_10_missing_attributes_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

percent = 10
#[5, 10, 15, 20, 100, 256]

kj15 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj15 = kj15['Jaccard']
kj110 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj110 = kj110['Jaccard']
kj115 = df[(df['k'] == 15) & (df['percentage'] == percent)]
kj115 = kj115['Jaccard']
kj120 = df[(df['k'] == 20) & (df['percentage'] == percent)]
kj120 = kj120['Jaccard']
kj180 = df[(df['k'] == 80) & (df['percentage'] == percent)]
kj180 = kj180['Jaccard']
kj1100 = df[(df['k'] == 100) & (df['percentage'] == percent)]
kj1100 = kj1100['Jaccard']
kj1192 = df[(df['k'] == 192) & (df['percentage'] == percent)]
kj1192 = kj1192['Jaccard']

kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,5)
kj15.insert(1,'Jaccard')
kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,10)
kj110.insert(1,'Jaccard')
kj115 = list(mean_confidence_interval(kj115))
kj115.insert(0,15)
kj115.insert(1,'Jaccard')
kj120 = list(mean_confidence_interval(kj120))
kj120.insert(0,20)
kj120.insert(1,'Jaccard')
kj180 = list(mean_confidence_interval(kj180))
kj180.insert(0,80)
kj180.insert(1,'Jaccard')
kj1100 = list(mean_confidence_interval(kj1100))
kj1100.insert(0,100)
kj1100.insert(1,'Jaccard')
kj1192 = list(mean_confidence_interval(kj1192))
kj1192.insert(0,192)
kj1192.insert(1,'Jaccard')

df1 = pd.DataFrame([kj15, kj110, kj115,kj120, kj180, kj1100,kj1192])
df1.columns = ['k','measurement','mean','lb','ub']


df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])

kj25 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj25 = kj25['Jaccard']
kj210 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj210 = kj210['Jaccard']
kj215 = df[(df['k'] == 15) & (df['percentage'] == percent)]
kj215 = kj215['Jaccard']
kj220 = df[(df['k'] == 20) & (df['percentage'] == percent)]
kj220 = kj220['Jaccard']
kj280 = df[(df['k'] == 80) & (df['percentage'] == percent)]
kj280 = kj280['Jaccard']
kj2100 = df[(df['k'] == 100) & (df['percentage'] == percent)]
kj2100 = kj2100['Jaccard']
kj2192 = df[(df['k'] == 192) & (df['percentage'] == percent)]
kj2192 = kj2192['Jaccard']

kj25 = list(mean_confidence_interval(kj25))
kj25.insert(0,5)
kj25.insert(1,'Jaccard')
kj210 = list(mean_confidence_interval(kj210))
kj210.insert(0,10)
kj210.insert(1,'Jaccard')
kj215 = list(mean_confidence_interval(kj215))
kj215.insert(0,15)
kj215.insert(1,'Jaccard')
kj220 = list(mean_confidence_interval(kj220))
kj220.insert(0,20)
kj220.insert(1,'Jaccard')
kj280 = list(mean_confidence_interval(kj280))
kj280.insert(0,80)
kj280.insert(1,'Jaccard')
kj2100 = list(mean_confidence_interval(kj2100))
kj2100.insert(0,100)
kj2100.insert(1,'Jaccard')
kj2192 = list(mean_confidence_interval(kj2192))
kj2192.insert(0,192)
kj2192.insert(1,'Jaccard')

df2 = pd.DataFrame([kj25, kj210, kj215,kj220, kj280, kj2100,kj2192])
df2.columns = ['k','measurement','mean','lb','ub']

df = pd.read_csv(input_file3, names=['percentage','a','k','RBO','Jaccard'])


kj35 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj35 = kj35['Jaccard']
kj310 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj310 = kj310['Jaccard']
kj315 = df[(df['k'] == 15) & (df['percentage'] == percent)]
kj315 = kj315['Jaccard']
kj320 = df[(df['k'] == 20) & (df['percentage'] == percent)]
kj320 = kj320['Jaccard']
kj380 = df[(df['k'] == 80) & (df['percentage'] == percent)]
kj380 = kj380['Jaccard']
kj3100 = df[(df['k'] == 100) & (df['percentage'] == percent)]
kj3100 = kj3100['Jaccard']
kj3192 = df[(df['k'] == 192) & (df['percentage'] == percent)]
kj3192 = kj3192['Jaccard']

kj35 = list(mean_confidence_interval(kj35))
kj35.insert(0,5)
kj35.insert(1,'Jaccard')
kj310 = list(mean_confidence_interval(kj310))
kj310.insert(0,10)
kj310.insert(1,'Jaccard')
kj315 = list(mean_confidence_interval(kj315))
kj315.insert(0,15)
kj315.insert(1,'Jaccard')
kj320 = list(mean_confidence_interval(kj320))
kj320.insert(0,20)
kj320.insert(1,'Jaccard')
kj380 = list(mean_confidence_interval(kj380))
kj380.insert(0,80)
kj380.insert(1,'Jaccard')
kj3100 = list(mean_confidence_interval(kj3100))
kj3100.insert(0,100)
kj3100.insert(1,'Jaccard')
kj3192 = list(mean_confidence_interval(kj3192))
kj3192.insert(0,192)
kj3192.insert(1,'Jaccard')

df3 = pd.DataFrame([kj35, kj310, kj315,kj320, kj380, kj3100,kj3192])
df3.columns = ['k','measurement','mean','lb','ub']


df = pd.read_csv(input_file4, names=['percentage','a','k','RBO','Jaccard'])


kj45 = df[(df['k'] == 5) & (df['percentage'] == percent)]
kj45 = kj45['Jaccard']
kj410 = df[(df['k'] == 10) & (df['percentage'] == percent)]
kj410 = kj410['Jaccard']
kj415 = df[(df['k'] == 15) & (df['percentage'] == percent)]
kj415 = kj415['Jaccard']
kj420 = df[(df['k'] == 20) & (df['percentage'] == percent)]
kj420 = kj420['Jaccard']
kj480 = df[(df['k'] == 80) & (df['percentage'] == percent)]
kj480 = kj480['Jaccard']
kj4100 = df[(df['k'] == 100) & (df['percentage'] == percent)]
kj4100 = kj4100['Jaccard']
kj4192 = df[(df['k'] == 192) & (df['percentage'] == percent)]
kj4192 = kj4192['Jaccard']

kj45 = list(mean_confidence_interval(kj45))
kj45.insert(0,5)
kj45.insert(1,'Jaccard')
kj410 = list(mean_confidence_interval(kj410))
kj410.insert(0,10)
kj410.insert(1,'Jaccard')
kj415 = list(mean_confidence_interval(kj415))
kj415.insert(0,15)
kj415.insert(1,'Jaccard')
kj420 = list(mean_confidence_interval(kj420))
kj420.insert(0,20)
kj420.insert(1,'Jaccard')
kj480 = list(mean_confidence_interval(kj480))
kj480.insert(0,80)
kj480.insert(1,'Jaccard')
kj4100 = list(mean_confidence_interval(kj4100))
kj4100.insert(0,100)
kj4100.insert(1,'Jaccard')
kj4192 = list(mean_confidence_interval(kj4192))
kj4192.insert(0,192)
kj4192.insert(1,'Jaccard')

df4 = pd.DataFrame([kj45, kj410, kj415,kj420, kj480, kj4100,kj4192])
df4.columns = ['k','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'Deviation missing random', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'Sim missing random', marker='<', linestyle='-', linewidth=2, markersize=12)
#ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'Deviation zipf missing', marker='o', linestyle='-', linewidth=2, markersize=12)
#ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Sim zipf missing', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
#ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
#ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % A missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness Jaccard- Missing on A to Ideal")
x = [5, 10, 15, 20, 80, 100, 192]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
