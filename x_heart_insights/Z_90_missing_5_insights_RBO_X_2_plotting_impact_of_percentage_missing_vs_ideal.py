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

input_file1 = 'results/correlation_missing_vs_ideal.csv'
input_file2 = 'results/kurtosis_missing_vs_ideal_random.csv'
input_file3 = 'results/skewness_missing_vs_ideal_random.csv'
input_file4 = 'results/sim_missing_a_m_vs_ideal.csv'
input_file5 = 'results/div_missing_a_m_vs_ideal.csv'


output_plot = 'RBO_90_all_percentage_missing_attributes_vs_ideal'

k = 5
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

dfj100 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj100 = dfj100['RBO']

dfj110 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj110 = dfj110['RBO']

dfj120 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj120 = dfj120['RBO']

dfj130 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj130 = dfj130['RBO']

dfj140 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj140 = dfj140['RBO']

dfj150 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj150 = dfj150['RBO']

dfj160 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj160 = dfj160['RBO']

dfj170 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj170 = dfj170['RBO']

dfj180 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj180 = dfj180['RBO']

dfj190 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj190 = dfj190['RBO']



dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'RBO')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,10)
dfj110.insert(1,'RBO')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,20)
dfj120.insert(1,'RBO')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,30)
dfj130.insert(1,'RBO')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,40)
dfj140.insert(1,'RBO')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,50)
dfj150.insert(1,'RBO')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,60)
dfj160.insert(1,'RBO')

dfj170 = list(mean_confidence_interval(dfj170))
dfj170.insert(0,70)
dfj170.insert(1,'RBO')

dfj180 = list(mean_confidence_interval(dfj180))
dfj180.insert(0,80)
dfj180.insert(1,'RBO')

dfj190 = list(mean_confidence_interval(dfj190))
dfj190.insert(0,90)
dfj190.insert(1,'RBO')



df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])


dfj200 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj200 = dfj200['RBO']

dfj210 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj210 = dfj210['RBO']

dfj220 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj220 = dfj220['RBO']

dfj230 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj230 = dfj230['RBO']

dfj240 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj240 = dfj240['RBO']

dfj250 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj250 = dfj250['RBO']

dfj260 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj260 = dfj260['RBO']

dfj270 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj270 = dfj270['RBO']

dfj280 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj280 = dfj280['RBO']

dfj290 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj290 = dfj290['RBO']



dfj200 = list(mean_confidence_interval(dfj200))
dfj200.insert(0,0)
dfj200.insert(1,'RBO')

dfj210 = list(mean_confidence_interval(dfj210))
dfj210.insert(0,10)
dfj210.insert(1,'RBO')

dfj220 = list(mean_confidence_interval(dfj220))
dfj220.insert(0,20)
dfj220.insert(1,'RBO')

dfj230 = list(mean_confidence_interval(dfj230))
dfj230.insert(0,30)
dfj230.insert(1,'RBO')

dfj240 = list(mean_confidence_interval(dfj240))
dfj240.insert(0,40)
dfj240.insert(1,'RBO')

dfj250 = list(mean_confidence_interval(dfj250))
dfj250.insert(0,50)
dfj250.insert(1,'RBO')

dfj260 = list(mean_confidence_interval(dfj260))
dfj260.insert(0,60)
dfj260.insert(1,'RBO')

dfj270 = list(mean_confidence_interval(dfj270))
dfj270.insert(0,70)
dfj270.insert(1,'RBO')

dfj280 = list(mean_confidence_interval(dfj280))
dfj280.insert(0,80)
dfj280.insert(1,'RBO')

dfj290 = list(mean_confidence_interval(dfj290))
dfj290.insert(0,90)
dfj290.insert(1,'RBO')


df = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])



dfj300 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj300 = dfj300['RBO']

dfj310 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj310 = dfj310['RBO']

dfj320 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj320 = dfj320['RBO']

dfj330 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj330 = dfj330['RBO']

dfj340 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj340 = dfj340['RBO']

dfj350 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj350 = dfj350['RBO']

dfj360 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj360 = dfj360['RBO']

dfj370 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj370 = dfj370['RBO']

dfj380 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj380 = dfj380['RBO']

dfj390 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj390 = dfj390['RBO']



dfj300 = list(mean_confidence_interval(dfj300))
dfj300.insert(0,0)
dfj300.insert(1,'RBO')

dfj310 = list(mean_confidence_interval(dfj310))
dfj310.insert(0,10)
dfj310.insert(1,'RBO')

dfj320 = list(mean_confidence_interval(dfj320))
dfj320.insert(0,20)
dfj320.insert(1,'RBO')

dfj330 = list(mean_confidence_interval(dfj330))
dfj330.insert(0,30)
dfj330.insert(1,'RBO')

dfj340 = list(mean_confidence_interval(dfj340))
dfj340.insert(0,40)
dfj340.insert(1,'RBO')

dfj350 = list(mean_confidence_interval(dfj350))
dfj350.insert(0,50)
dfj350.insert(1,'RBO')

dfj360 = list(mean_confidence_interval(dfj360))
dfj360.insert(0,60)
dfj360.insert(1,'RBO')

dfj370 = list(mean_confidence_interval(dfj370))
dfj370.insert(0,70)
dfj370.insert(1,'RBO')

dfj380 = list(mean_confidence_interval(dfj380))
dfj380.insert(0,80)
dfj380.insert(1,'RBO')

dfj390 = list(mean_confidence_interval(dfj390))
dfj390.insert(0,90)
dfj390.insert(1,'RBO')



df = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])



dfj400 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj400 = dfj400['RBO']

dfj410 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj410 = dfj410['RBO']

dfj420 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj420 = dfj420['RBO']

dfj430 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj430 = dfj430['RBO']

dfj440 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj440 = dfj440['RBO']

dfj450 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj450 = dfj450['RBO']

dfj460 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj460 = dfj460['RBO']

dfj470 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj470 = dfj470['RBO']

dfj480 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj480 = dfj480['RBO']

dfj490 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj490 = dfj490['RBO']



dfj400 = list(mean_confidence_interval(dfj400))
dfj400.insert(0,0)
dfj400.insert(1,'RBO')

dfj410 = list(mean_confidence_interval(dfj410))
dfj410.insert(0,10)
dfj410.insert(1,'RBO')

dfj420 = list(mean_confidence_interval(dfj420))
dfj420.insert(0,20)
dfj420.insert(1,'RBO')

dfj430 = list(mean_confidence_interval(dfj430))
dfj430.insert(0,30)
dfj430.insert(1,'RBO')

dfj440 = list(mean_confidence_interval(dfj440))
dfj440.insert(0,40)
dfj440.insert(1,'RBO')

dfj450 = list(mean_confidence_interval(dfj450))
dfj450.insert(0,50)
dfj450.insert(1,'RBO')

dfj460 = list(mean_confidence_interval(dfj460))
dfj460.insert(0,60)
dfj460.insert(1,'RBO')

dfj470 = list(mean_confidence_interval(dfj470))
dfj470.insert(0,70)
dfj470.insert(1,'RBO')

dfj480 = list(mean_confidence_interval(dfj480))
dfj480.insert(0,80)
dfj480.insert(1,'RBO')

dfj490 = list(mean_confidence_interval(dfj490))
dfj490.insert(0,90)
dfj490.insert(1,'RBO')


df = pd.read_csv(input_file5, names=['percentage','k','RBO','Jaccard'])


dfj500 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj500 = dfj500['RBO']

dfj510 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj510 = dfj510['RBO']

dfj520 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj520 = dfj520['RBO']

dfj530 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj530 = dfj530['RBO']

dfj540 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj540 = dfj540['RBO']

dfj550 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj550 = dfj550['RBO']

dfj560 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj560 = dfj560['RBO']

dfj570 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj570 = dfj570['RBO']

dfj580 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj580 = dfj580['RBO']

dfj590 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj590 = dfj590['RBO']



dfj500 = list(mean_confidence_interval(dfj500))
dfj500.insert(0,0)
dfj500.insert(1,'RBO')

dfj510 = list(mean_confidence_interval(dfj510))
dfj510.insert(0,10)
dfj510.insert(1,'RBO')

dfj520 = list(mean_confidence_interval(dfj520))
dfj520.insert(0,20)
dfj520.insert(1,'RBO')

dfj530 = list(mean_confidence_interval(dfj530))
dfj530.insert(0,30)
dfj530.insert(1,'RBO')

dfj540 = list(mean_confidence_interval(dfj540))
dfj540.insert(0,40)
dfj540.insert(1,'RBO')

dfj550 = list(mean_confidence_interval(dfj550))
dfj550.insert(0,50)
dfj550.insert(1,'RBO')

dfj560 = list(mean_confidence_interval(dfj560))
dfj560.insert(0,60)
dfj560.insert(1,'RBO')

dfj570 = list(mean_confidence_interval(dfj570))
dfj570.insert(0,70)
dfj570.insert(1,'RBO')

dfj580 = list(mean_confidence_interval(dfj580))
dfj580.insert(0,80)
dfj580.insert(1,'RBO')

dfj590 = list(mean_confidence_interval(dfj590))
dfj590.insert(0,90)
dfj590.insert(1,'RBO')




df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190])
df1.columns = ['k','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfj200, dfj210, dfj220, dfj230, dfj240, dfj250, dfj260, dfj270, dfj280, dfj290])
df2.columns = ['k','measurement','mean','lb','ub']
df3 = pd.DataFrame([dfj300, dfj310, dfj320, dfj330, dfj340, dfj350, dfj360, dfj370, dfj380, dfj390])
df3.columns = ['k','measurement','mean','lb','ub']
df4 = pd.DataFrame([dfj400, dfj410, dfj420, dfj430, dfj440, dfj450, dfj460, dfj470, dfj480, dfj490])
df4.columns = ['k','measurement','mean','lb','ub']
df5 = pd.DataFrame([dfj500, dfj510, dfj520, dfj530, dfj540, dfj550, dfj560, dfj570, dfj580, dfj590])
df5.columns = ['k','measurement','mean','lb','ub']


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

mean5 = df5[df5['measurement'] == 'RBO'].reset_index()
mean5 = mean5['mean']
ub5 = df5[df5['measurement'] == 'RBO'].reset_index()
ub5 = ub5['ub']
lb5 = df5[df5['measurement'] == 'RBO'].reset_index()
lb5 = lb5['lb']


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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = '+ Correlation', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = '+ Kurtosis', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = '+ Skewness', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Similarity to reference', marker='s', linestyle='--', linewidth=2, markersize=12)
ax.plot(mean5, lw = 1, color = '#0d0e0f', alpha = 1, label = 'Deviation/outstanding', marker='x', linestyle='-.', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)
ax.fill_between(t, lb5, ub5, color = '#87888a', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact missing on Effectiveness (Jaccard), 95% CI, k = 5")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Effectiveness - Missing to Ideal")
x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
