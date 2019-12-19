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

input_file1 = 'results/cum_missing_a_m_vs_ideal.csv'
input_file2 = 'results/cum_sim_missing_a_m_vs_ideal.csv'

output_plot = 'cum_all_percentage_missing_a_m_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD
k = 5

df1 = pd.read_csv(input_file1, names=['percentage','k','Cum_distance'])

df1j100 = df1[(df1['k'] == k) & (df1['percentage'] == 0)]
df1j100 = df1j100['Cum_distance']

df1j110 = df1[(df1['k'] == k) & (df1['percentage'] == 10)]
df1j110 = df1j110['Cum_distance']

df1j120 = df1[(df1['k'] == k) & (df1['percentage'] == 20)]
df1j120 = df1j120['Cum_distance']

df1j130 = df1[(df1['k'] == k) & (df1['percentage'] == 30)]
df1j130 = df1j130['Cum_distance']

df1j140 = df1[(df1['k'] == k) & (df1['percentage'] == 40)]
df1j140 = df1j140['Cum_distance']

df1j150 = df1[(df1['k'] == k) & (df1['percentage'] == 50)]
df1j150 = df1j150['Cum_distance']

df1j160 = df1[(df1['k'] == k) & (df1['percentage'] == 60)]
df1j160 = df1j160['Cum_distance']



df1j100 = list(mean_confidence_interval(df1j100))
df1j100.insert(0,0)
df1j100.insert(1,'Cum_distance')

df1j110 = list(mean_confidence_interval(df1j110))
df1j110.insert(0,10)
df1j110.insert(1,'Cum_distance')

df1j120 = list(mean_confidence_interval(df1j120))
df1j120.insert(0,20)
df1j120.insert(1,'Cum_distance')

df1j130 = list(mean_confidence_interval(df1j130))
df1j130.insert(0,30)
df1j130.insert(1,'Cum_distance')

df1j140 = list(mean_confidence_interval(df1j140))
df1j140.insert(0,40)
df1j140.insert(1,'Cum_distance')

df1j150 = list(mean_confidence_interval(df1j150))
df1j150.insert(0,50)
df1j150.insert(1,'Cum_distance')

df1j160 = list(mean_confidence_interval(df1j160))
df1j160.insert(0,60)
df1j160.insert(1,'Cum_distance')



df1 = pd.DataFrame([df1j100, df1j110, df1j120, df1j130, df1j140, df1j150, df1j160])
df1.columns = ['k','measurement','mean','lb','ub']



df2 = pd.read_csv(input_file2, names=['percentage','k','Cum_distance'])

df2j100 = df2[(df2['k'] == k) & (df2['percentage'] == 0)]
df2j100 = df2j100['Cum_distance']

df2j110 = df2[(df2['k'] == k) & (df2['percentage'] == 10)]
df2j110 = df2j110['Cum_distance']

df2j120 = df2[(df2['k'] == k) & (df2['percentage'] == 20)]
df2j120 = df2j120['Cum_distance']

df2j130 = df2[(df2['k'] == k) & (df2['percentage'] == 30)]
df2j130 = df2j130['Cum_distance']

df2j140 = df2[(df2['k'] == k) & (df2['percentage'] == 40)]
df2j140 = df2j140['Cum_distance']

df2j150 = df2[(df2['k'] == k) & (df2['percentage'] == 50)]
df2j150 = df2j150['Cum_distance']

df2j160 = df2[(df2['k'] == k) & (df2['percentage'] == 60)]
df2j160 = df2j160['Cum_distance']


df2j100 = list(mean_confidence_interval(df2j100))
df2j100.insert(0,0)
df2j100.insert(1,'Cum_distance')

df2j110 = list(mean_confidence_interval(df2j110))
df2j110.insert(0,10)
df2j110.insert(1,'Cum_distance')

df2j120 = list(mean_confidence_interval(df2j120))
df2j120.insert(0,20)
df2j120.insert(1,'Cum_distance')

df2j130 = list(mean_confidence_interval(df2j130))
df2j130.insert(0,30)
df2j130.insert(1,'Cum_distance')

df2j140 = list(mean_confidence_interval(df2j140))
df2j140.insert(0,40)
df2j140.insert(1,'Cum_distance')

df2j150 = list(mean_confidence_interval(df2j150))
df2j150.insert(0,50)
df2j150.insert(1,'Cum_distance')

df2j160 = list(mean_confidence_interval(df2j160))
df2j160.insert(0,60)
df2j160.insert(1,'Cum_distance')



df2 = pd.DataFrame([df2j100, df2j110, df2j120, df2j130, df2j140, df2j150, df2j160])
df2.columns = ['k','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'Cum_distance'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Cum_distance'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Cum_distance'].reset_index()
lb1 = lb1['lb']


mean2 = df2[df2['measurement'] == 'Cum_distance'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Cum_distance'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Cum_distance'].reset_index()
lb2 = lb2['lb']

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
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'Deviation/Outstanding', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#539caf', alpha = 1, label = 'Similarity', marker='x', linestyle='-.', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#539caf', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of percentage of missing on Effectiveness, 95% CI, k = 5")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Cumulative distance gap to ideal")
x = [0, 10, 20, 30, 40, 50, 60]
xi = list(range(len(x)))
plt.xticks(xi, x)
ax.invert_yaxis()

# Display legend
#ax.set_ylim(ymin=0.0)
#ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
