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

input_file1 = 'results/age_missing_a_m_vs_ideal.csv'
input_file2 = 'results/gender_missing_a_m_vs_ideal.csv'
input_file3 = 'results/insulin_missing_a_m_vs_ideal.csv'
input_file4 = 'results/readmitted_missing_a_m_vs_ideal.csv'

output_plot = 'rbo_all_percentage_missing_a_m_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD
df1 = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])
k = 5

df1j00 = df1[(df1['k'] == 5) & (df1['percentage'] == 0)]
df1j00 = df1j00['RBO']

df1j10 = df1[(df1['k'] == 5) & (df1['percentage'] == 10)]
df1j10 = df1j10['RBO']

df1j20 = df1[(df1['k'] == 5) & (df1['percentage'] == 20)]
df1j20 = df1j20['RBO']

df1j30 = df1[(df1['k'] == 5) & (df1['percentage'] == 30)]
df1j30 = df1j30['RBO']

df1j40 = df1[(df1['k'] == 5) & (df1['percentage'] == 40)]
df1j40 = df1j40['RBO']

df1j50 = df1[(df1['k'] == 5) & (df1['percentage'] == 50)]
df1j50 = df1j50['RBO']

df1j60 = df1[(df1['k'] == 5) & (df1['percentage'] == 60)]
df1j60 = df1j60['RBO']

df1j70 = df1[(df1['k'] == 5) & (df1['percentage'] == 70)]
df1j70 = df1j70['RBO']

df1j80 = df1[(df1['k'] == 5) & (df1['percentage'] == 80)]
df1j80 = df1j80['RBO']


df1j00 = list(mean_confidence_interval(df1j00))
df1j00.insert(0,0)
df1j00.insert(1,'Jaccard')

df1j10 = list(mean_confidence_interval(df1j10))
df1j10.insert(0,10)
df1j10.insert(1,'Jaccard')

df1j20 = list(mean_confidence_interval(df1j20))
df1j20.insert(0,20)
df1j20.insert(1,'Jaccard')

df1j30 = list(mean_confidence_interval(df1j30))
df1j30.insert(0,30)
df1j30.insert(1,'Jaccard')

df1j40 = list(mean_confidence_interval(df1j40))
df1j40.insert(0,40)
df1j40.insert(1,'Jaccard')

df1j50 = list(mean_confidence_interval(df1j50))
df1j50.insert(0,50)
df1j50.insert(1,'Jaccard')

df1j60 = list(mean_confidence_interval(df1j60))
df1j60.insert(0,60)
df1j60.insert(1,'Jaccard')

df1j70 = list(mean_confidence_interval(df1j70))
df1j70.insert(0,70)
df1j70.insert(1,'Jaccard')

df1j80 = list(mean_confidence_interval(df1j80))
df1j80.insert(0,80)
df1j80.insert(1,'Jaccard')



df1 = pd.DataFrame([df1j00, df1j10, df1j20, df1j30, df1j40, df1j50, df1j60, df1j70, df1j80])
df1.columns = ['k','measurement','mean','lb','ub']

mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']



df2 = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])
k = 5

df2j00 = df2[(df2['k'] == 5) & (df2['percentage'] == 0)]
df2j00 = df2j00['RBO']

df2j10 = df2[(df2['k'] == 5) & (df2['percentage'] == 10)]
df2j10 = df2j10['RBO']

df2j20 = df2[(df2['k'] == 5) & (df2['percentage'] == 20)]
df2j20 = df2j20['RBO']

df2j30 = df2[(df2['k'] == 5) & (df2['percentage'] == 30)]
df2j30 = df2j30['RBO']

df2j40 = df2[(df2['k'] == 5) & (df2['percentage'] == 40)]
df2j40 = df2j40['RBO']

df2j50 = df2[(df2['k'] == 5) & (df2['percentage'] == 50)]
df2j50 = df2j50['RBO']

df2j60 = df2[(df2['k'] == 5) & (df2['percentage'] == 60)]
df2j60 = df2j60['RBO']

df2j70 = df2[(df2['k'] == 5) & (df2['percentage'] == 70)]
df2j70 = df2j70['RBO']

df2j80 = df2[(df2['k'] == 5) & (df2['percentage'] == 80)]
df2j80 = df2j80['RBO']



df2j00 = list(mean_confidence_interval(df2j00))
df2j00.insert(0,0)
df2j00.insert(1,'Jaccard')

df2j10 = list(mean_confidence_interval(df2j10))
df2j10.insert(0,10)
df2j10.insert(1,'Jaccard')

df2j20 = list(mean_confidence_interval(df2j20))
df2j20.insert(0,20)
df2j20.insert(1,'Jaccard')

df2j30 = list(mean_confidence_interval(df2j30))
df2j30.insert(0,30)
df2j30.insert(1,'Jaccard')

df2j40 = list(mean_confidence_interval(df2j40))
df2j40.insert(0,40)
df2j40.insert(1,'Jaccard')

df2j50 = list(mean_confidence_interval(df2j50))
df2j50.insert(0,50)
df2j50.insert(1,'Jaccard')

df2j60 = list(mean_confidence_interval(df2j60))
df2j60.insert(0,60)
df2j60.insert(1,'Jaccard')

df2j70 = list(mean_confidence_interval(df2j70))
df2j70.insert(0,70)
df2j70.insert(1,'Jaccard')

df2j80 = list(mean_confidence_interval(df2j80))
df2j80.insert(0,80)
df2j80.insert(1,'Jaccard')


df2 = pd.DataFrame([df2j00, df2j10, df2j20, df2j30, df2j40, df2j50, df2j60, df2j70, df2j80])
df2.columns = ['k','measurement','mean','lb','ub']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']



df3 = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])
k = 5

df3j00 = df3[(df3['k'] == 5) & (df3['percentage'] == 0)]
df3j00 = df3j00['RBO']

df3j10 = df3[(df3['k'] == 5) & (df3['percentage'] == 10)]
df3j10 = df3j10['RBO']

df3j20 = df3[(df3['k'] == 5) & (df3['percentage'] == 20)]
df3j20 = df3j20['RBO']

df3j30 = df3[(df3['k'] == 5) & (df3['percentage'] == 30)]
df3j30 = df3j30['RBO']

df3j40 = df3[(df3['k'] == 5) & (df3['percentage'] == 40)]
df3j40 = df3j40['RBO']

df3j50 = df3[(df3['k'] == 5) & (df3['percentage'] == 50)]
df3j50 = df3j50['RBO']

df3j60 = df3[(df3['k'] == 5) & (df3['percentage'] == 60)]
df3j60 = df3j60['RBO']

df3j70 = df3[(df3['k'] == 5) & (df3['percentage'] == 70)]
df3j70 = df3j70['RBO']

df3j80 = df3[(df3['k'] == 5) & (df3['percentage'] == 80)]
df3j80 = df3j80['RBO']



df3j00 = list(mean_confidence_interval(df3j00))
df3j00.insert(0,0)
df3j00.insert(1,'Jaccard')

df3j10 = list(mean_confidence_interval(df3j10))
df3j10.insert(0,10)
df3j10.insert(1,'Jaccard')

df3j20 = list(mean_confidence_interval(df3j20))
df3j20.insert(0,20)
df3j20.insert(1,'Jaccard')

df3j30 = list(mean_confidence_interval(df3j30))
df3j30.insert(0,30)
df3j30.insert(1,'Jaccard')

df3j40 = list(mean_confidence_interval(df3j40))
df3j40.insert(0,40)
df3j40.insert(1,'Jaccard')

df3j50 = list(mean_confidence_interval(df3j50))
df3j50.insert(0,50)
df3j50.insert(1,'Jaccard')

df3j60 = list(mean_confidence_interval(df3j60))
df3j60.insert(0,60)
df3j60.insert(1,'Jaccard')

df3j70 = list(mean_confidence_interval(df3j70))
df3j70.insert(0,70)
df3j70.insert(1,'Jaccard')

df3j80 = list(mean_confidence_interval(df3j80))
df3j80.insert(0,80)
df3j80.insert(1,'Jaccard')




df3 = pd.DataFrame([df3j00, df3j10, df3j20, df3j30, df3j40, df3j50, df3j60, df3j70, df3j80])
df3.columns = ['k','measurement','mean','lb','ub']

mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb3 = lb3['lb']


df4 = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])
k = 5

df4j00 = df4[(df4['k'] == 5) & (df4['percentage'] == 0)]
df4j00 = df4j00['RBO']

df4j10 = df4[(df4['k'] == 5) & (df4['percentage'] == 10)]
df4j10 = df4j10['RBO']

df4j20 = df4[(df4['k'] == 5) & (df4['percentage'] == 20)]
df4j20 = df4j20['RBO']

df4j30 = df4[(df4['k'] == 5) & (df4['percentage'] == 30)]
df4j30 = df4j30['RBO']

df4j40 = df4[(df4['k'] == 5) & (df4['percentage'] == 40)]
df4j40 = df4j40['RBO']

df4j50 = df4[(df4['k'] == 5) & (df4['percentage'] == 50)]
df4j50 = df4j50['RBO']

df4j60 = df4[(df4['k'] == 5) & (df4['percentage'] == 60)]
df4j60 = df4j60['RBO']

df4j70 = df4[(df4['k'] == 5) & (df4['percentage'] == 70)]
df4j70 = df4j70['RBO']

df4j80 = df4[(df4['k'] == 5) & (df4['percentage'] == 80)]
df4j80 = df4j80['RBO']



df4j00 = list(mean_confidence_interval(df4j00))
df4j00.insert(0,0)
df4j00.insert(1,'Jaccard')

df4j10 = list(mean_confidence_interval(df4j10))
df4j10.insert(0,10)
df4j10.insert(1,'Jaccard')

df4j20 = list(mean_confidence_interval(df4j20))
df4j20.insert(0,20)
df4j20.insert(1,'Jaccard')

df4j30 = list(mean_confidence_interval(df4j30))
df4j30.insert(0,30)
df4j30.insert(1,'Jaccard')

df4j40 = list(mean_confidence_interval(df4j40))
df4j40.insert(0,40)
df4j40.insert(1,'Jaccard')

df4j50 = list(mean_confidence_interval(df4j50))
df4j50.insert(0,50)
df4j50.insert(1,'Jaccard')

df4j60 = list(mean_confidence_interval(df4j60))
df4j60.insert(0,60)
df4j60.insert(1,'Jaccard')

df4j70 = list(mean_confidence_interval(df4j70))
df4j70.insert(0,70)
df4j70.insert(1,'Jaccard')

df4j80 = list(mean_confidence_interval(df4j80))
df4j80.insert(0,80)
df4j80.insert(1,'Jaccard')



df4 = pd.DataFrame([df4j00, df4j10, df4j20, df4j30, df4j40, df4j50, df4j60, df4j70, df4j80])
df4.columns = ['k','measurement','mean','lb','ub']

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


t = np.arange(len(mean2))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'q1: age = (80-90) vs !(80-90)', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'q2: gender = Female vs Male', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'q3: insulin = Steady vs !Steady', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'q4: readmitted = NO vs !NO', marker='s', linestyle='--', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of percentage of missing on Effectiveness, 95% CI, k = 5")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Effectiveness - Missing A + M to Ideal")
x = [0, 10, 20, 30, 40, 50, 60, 70, 80]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
