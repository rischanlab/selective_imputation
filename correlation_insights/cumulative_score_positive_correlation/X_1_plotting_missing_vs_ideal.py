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

output_plot = '50_correlation_missing_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['percentage','k','gap'])

percent = 50
#[5, 10, 15, 20, 30, 45]
k5j = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5j = k5j['gap']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['gap']
k15j = df[(df['k'] == 15) & (df['percentage'] == percent)]
k15j = k15j['gap']

k20j = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20j = k20j['gap']

k25j = df[(df['k'] == 25) & (df['percentage'] == percent)]
k25j = k25j['gap']

k30j = df[(df['k'] == 30) & (df['percentage'] == percent)]
k30j = k30j['gap']

k35j = df[(df['k'] == 35) & (df['percentage'] == percent)]
k35j = k35j['gap']

k40j = df[(df['k'] == 40) & (df['percentage'] == percent)]
k40j = k40j['gap']

k45j = df[(df['k'] == 45) & (df['percentage'] == percent)]
k45j = k45j['gap']


k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'gap')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'gap')
k15j = list(mean_confidence_interval(k15j))
k15j.insert(0,15)
k15j.insert(1,'gap')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
k20j.insert(1,'gap')

k25j = list(mean_confidence_interval(k25j))
k25j.insert(0,25)
k25j.insert(1,'gap')

k30j = list(mean_confidence_interval(k30j))
k30j.insert(0,30)
k30j.insert(1,'gap')

k35j = list(mean_confidence_interval(k35j))
k35j.insert(0,35)
k35j.insert(1,'gap')

k40j = list(mean_confidence_interval(k40j))
k40j.insert(0,40)
k40j.insert(1,'gap')

k45j = list(mean_confidence_interval(k45j))
k45j.insert(0,45)
k45j.insert(1,'gap')

df = pd.DataFrame([k5j, k10j, k15j,k20j, k25j, k30j,k35j,k40j, k45j])
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
ax.set_title("Impact of k on Effectiveness, 95% CI, 50 % missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Missing to Ideal")
x = [5, 10, 15, 20, 25, 30, 35, 40, 45]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
#ax.set_ylim(ymin=0.0)
#ax.set_ylim(ymax=1.1)
ax.invert_yaxis()


ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 300)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
