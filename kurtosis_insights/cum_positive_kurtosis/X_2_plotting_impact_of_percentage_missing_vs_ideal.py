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

input_file = 'results/cum_missing_vs_ideal.csv'

output_plot = 'skewness_all_percentage_missing_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file, names=['percentage','k','gap'])
k = 10

dfj00 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj00 = dfj00['gap']

dfj10 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj10 = dfj10['gap']

dfj20 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj20 = dfj20['gap']

dfj30 = df[(df['k'] == k) & (df['percentage'] == 30)]
dfj30 = dfj30['gap']

dfj40 = df[(df['k'] == k) & (df['percentage'] == 40)]
dfj40 = dfj40['gap']

dfj50 = df[(df['k'] == k) & (df['percentage'] == 50)]
dfj50 = dfj50['gap']

dfj60 = df[(df['k'] == k) & (df['percentage'] == 60)]
dfj60 = dfj60['gap']

dfj70 = df[(df['k'] == k) & (df['percentage'] == 70)]
dfj70 = dfj70['gap']

dfj80 = df[(df['k'] == k) & (df['percentage'] == 80)]
dfj80 = dfj80['gap']

dfj90 = df[(df['k'] == k) & (df['percentage'] == 90)]
dfj90 = dfj90['gap']

dfj00 = list(mean_confidence_interval(dfj00))
dfj00.insert(0,0)
dfj00.insert(1,'gap')

dfj10 = list(mean_confidence_interval(dfj10))
dfj10.insert(0,10)
dfj10.insert(1,'gap')

dfj20 = list(mean_confidence_interval(dfj20))
dfj20.insert(0,20)
dfj20.insert(1,'gap')

dfj30 = list(mean_confidence_interval(dfj30))
dfj30.insert(0,30)
dfj30.insert(1,'gap')

dfj40 = list(mean_confidence_interval(dfj40))
dfj40.insert(0,40)
dfj40.insert(1,'gap')

dfj50 = list(mean_confidence_interval(dfj50))
dfj50.insert(0,50)
dfj50.insert(1,'gap')

dfj60 = list(mean_confidence_interval(dfj60))
dfj60.insert(0,60)
dfj60.insert(1,'gap')

dfj70 = list(mean_confidence_interval(dfj70))
dfj70.insert(0,70)
dfj70.insert(1,'gap')

dfj80 = list(mean_confidence_interval(dfj80))
dfj80.insert(0,80)
dfj80.insert(1,'gap')

dfj90 = list(mean_confidence_interval(dfj90))
dfj90.insert(0,90)
dfj90.insert(1,'gap')


df = pd.DataFrame([dfj00, dfj10, dfj20, dfj30, dfj40, dfj50, dfj60, dfj70, dfj80, dfj90])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'gap'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'gap'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'gap'].reset_index()
lb0 = lb0['lb']


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
ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'gap', marker='x', linestyle='-.', linewidth=2, markersize=12)
#ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'RBO 0.95', marker='<', linestyle='-', linewidth=2, markersize=12)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
#ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of missing on Effectiveness, k = 10")
ax.set_xlabel("percentage of missing")
ax.set_ylabel("Effectiveness - Missing to Ideal")
x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
#ax.set_ylim(ymin=0.0)
#ax.set_ylim(ymax=1.01)
ax.invert_yaxis()


ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
