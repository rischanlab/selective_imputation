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

input_file = 'results/missing_vs_ideal_zipf.csv'

output_plot = 'all_alpha_measures_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file, names=['percent','alpha','k','RBO','Jaccard'])
k = 10
percent = 50

dfj00 = df[(df['k'] == k) & (df['alpha'] == 1.1) & (df['percent'] == percent)]
dfj00 = dfj00['Jaccard']

dfj10 = df[(df['k'] == k) & (df['alpha'] == 1.2) & (df['percent'] == percent)]
dfj10 = dfj10['Jaccard']

dfj20 = df[(df['k'] == k) & (df['alpha'] == 1.3) & (df['percent'] == percent)]
dfj20 = dfj20['Jaccard']

dfj30 = df[(df['k'] == k) & (df['alpha'] == 1.4) & (df['percent'] == percent)]
dfj30 = dfj30['Jaccard']

dfj40 = df[(df['k'] == k) & (df['alpha'] == 1.5) & (df['percent'] == percent)]
dfj40 = dfj40['Jaccard']

dfj50 = df[(df['k'] == k) & (df['alpha'] == 1.6) & (df['percent'] == percent)]
dfj50 = dfj50['Jaccard']

dfj60 = df[(df['k'] == k) & (df['alpha'] == 1.7) & (df['percent'] == percent)]
dfj60 = dfj60['Jaccard']

dfj00 = list(mean_confidence_interval(dfj00))
dfj00.insert(0,1.1)
dfj00.insert(1,'Jaccard')

dfj10 = list(mean_confidence_interval(dfj10))
dfj10.insert(0,1.2)
dfj10.insert(1,'Jaccard')

dfj20 = list(mean_confidence_interval(dfj20))
dfj20.insert(0,1.3)
dfj20.insert(1,'Jaccard')

dfj30 = list(mean_confidence_interval(dfj30))
dfj30.insert(0,1.4)
dfj30.insert(1,'Jaccard')

dfj40 = list(mean_confidence_interval(dfj40))
dfj40.insert(0,1.5)
dfj40.insert(1,'Jaccard')

dfj50 = list(mean_confidence_interval(dfj50))
dfj50.insert(0,1.6)
dfj50.insert(1,'Jaccard')


dfj60 = list(mean_confidence_interval(dfj60))
dfj60.insert(0,1.7)
dfj60.insert(1,'Jaccard')


dfr00 = df[(df['k'] == k) & (df['alpha'] == 1.1) & (df['percent'] == percent)]
dfr00 = dfr00['RBO']

dfr10 = df[(df['k'] == k) & (df['alpha'] == 1.2) & (df['percent'] == percent)]
dfr10 = dfr10['RBO']

dfr20 = df[(df['k'] == k) & (df['alpha'] == 1.3) & (df['percent'] == percent)]
dfr20 = dfr20['RBO']

dfr30 = df[(df['k'] == k) & (df['alpha'] == 1.4) & (df['percent'] == percent)]
dfr30 = dfr30['RBO']

dfr40 = df[(df['k'] == k) & (df['alpha'] == 1.5) & (df['percent'] == percent)]
dfr40 = dfr40['RBO']

dfr50 = df[(df['k'] == k) & (df['alpha'] == 1.6) & (df['percent'] == percent)]
dfr50 = dfr50['RBO']

dfr60 = df[(df['k'] == k) & (df['alpha'] == 1.7) & (df['percent'] == percent)]
dfr60 = dfr60['RBO']

dfr00 = list(mean_confidence_interval(dfr00))
dfr00.insert(0,1.1)
dfr00.insert(1,'RBO')

dfr10 = list(mean_confidence_interval(dfr10))
dfr10.insert(0,1.2)
dfr10.insert(1,'RBO')

dfr20 = list(mean_confidence_interval(dfr20))
dfr20.insert(0,1.3)
dfr20.insert(1,'RBO')

dfr30 = list(mean_confidence_interval(dfr30))
dfr30.insert(0,1.4)
dfr30.insert(1,'RBO')

dfr40 = list(mean_confidence_interval(dfr40))
dfr40.insert(0,1.5)
dfr40.insert(1,'RBO')

dfr50 = list(mean_confidence_interval(dfr50))
dfr50.insert(0,1.6)
dfr50.insert(1,'RBO')

dfr60 = list(mean_confidence_interval(dfr60))
dfr60.insert(0,1.7)
dfr60.insert(1,'RBO')


df = pd.DataFrame([dfj00, dfj10, dfj20, dfj30, dfj40, dfj50,dfj60,
                   dfr00, dfr10, dfr20, dfr30, dfr40, dfr50, dfr60])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']


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


t = np.arange(len(mean0))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95', marker='<', linestyle='-', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)

# Label the axes and provide a title
ax.set_title(r'Impact of $\alpha$ on Effectiveness, k = 10')
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel("Effectiveness - Missing Zipf")
x = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
