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

output_plot = '70_correlation_zipf_missing_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['percentage','alpha','k','RBO','Jaccard'])

percent = 70
alpha = 1.4
#[5, 10, 15, 20, 30, 45]
k5j = df[(df['k'] == 5) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k5j = k5j['Jaccard']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k10j = k10j['Jaccard']
k15j = df[(df['k'] == 15) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k15j = k15j['Jaccard']

k20j = df[(df['k'] == 20) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k20j = k20j['Jaccard']

k25j = df[(df['k'] == 25) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k25j = k25j['Jaccard']

k30j = df[(df['k'] == 30) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k30j = k30j['Jaccard']

k35j = df[(df['k'] == 35) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k35j = k35j['Jaccard']

k40j = df[(df['k'] == 40) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k40j = k40j['Jaccard']

k45j = df[(df['k'] == 45) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k45j = k45j['Jaccard']

#RBO
k5r = df[(df['k'] == 5) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k5r = k5r['RBO']
k10r = df[(df['k'] == 10) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k10r = k10r['RBO']
k15r = df[(df['k'] == 15) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k15r = k15r['RBO']
k20r = df[(df['k'] == 20) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k20r = k20r['RBO']

k25r = df[(df['k'] == 25) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k25r = k25r['RBO']

k30r = df[(df['k'] == 30) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k30r = k30r['RBO']

k35r = df[(df['k'] == 35) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k35r = k35r['RBO']

k40r = df[(df['k'] == 40) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k40r = k40r['RBO']

k45r = df[(df['k'] == 45) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k45r = k45r['RBO']

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'Jaccard')
k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')
k15j = list(mean_confidence_interval(k15j))
k15j.insert(0,15)
k15j.insert(1,'Jaccard')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
k20j.insert(1,'Jaccard')

k25j = list(mean_confidence_interval(k25j))
k25j.insert(0,25)
k25j.insert(1,'Jaccard')

k30j = list(mean_confidence_interval(k30j))
k30j.insert(0,30)
k30j.insert(1,'Jaccard')

k35j = list(mean_confidence_interval(k35j))
k35j.insert(0,35)
k35j.insert(1,'Jaccard')

k40j = list(mean_confidence_interval(k40j))
k40j.insert(0,40)
k40j.insert(1,'Jaccard')

k45j = list(mean_confidence_interval(k45j))
k45j.insert(0,45)
k45j.insert(1,'Jaccard')

k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
k5r.insert(1,'RBO 0.95')
k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO 0.95')
k15r = list(mean_confidence_interval(k15r))
k15r.insert(0,15)
k15r.insert(1,'RBO 0.95')
k20r = list(mean_confidence_interval(k20r))
k20r.insert(0,20)
k20r.insert(1,'RBO 0.95')
k25r = list(mean_confidence_interval(k25r))
k25r.insert(0,25)
k25r.insert(1,'RBO 0.95')
k30r = list(mean_confidence_interval(k30r))
k30r.insert(0,30)
k30r.insert(1,'RBO 0.95')


k35r = list(mean_confidence_interval(k35r))
k35r.insert(0,35)
k35r.insert(1,'RBO 0.95')

k40r = list(mean_confidence_interval(k40r))
k40r.insert(0,40)
k40r.insert(1,'RBO 0.95')


k45r = list(mean_confidence_interval(k45r))
k45r.insert(0,45)
k45r.insert(1,'RBO 0.95')

df = pd.DataFrame([k5j, k10j, k15j,k20j, k25j, k30j,k35j,k40j, k45j, k5r, k10r, k15r,k20r, k25r, k30r,k35r, k40r,k45r])
df.columns = ['k','measurement','mean','lb','ub']

mean0 = df[df['measurement'] == 'Jaccard'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'Jaccard'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'Jaccard'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'RBO 0.95'].reset_index()
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
ax.set_title(r'Impact of k on Effectiveness, Zipf 70% missing $\alpha = 1.4$')
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Missing zipf ")
x = [5, 10, 15, 20, 25, 30, 35, 40, 45]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
