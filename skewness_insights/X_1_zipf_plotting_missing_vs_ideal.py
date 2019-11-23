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

output_plot = '70_skewness_zipf_missing_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['percentage','alpha','k','RBO','Jaccard'])

percent = 70
alpha = 1.4

k3j = df[(df['k'] == 3) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k3j = k3j['Jaccard']

k5j = df[(df['k'] == 5) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k5j = k5j['Jaccard']

k8j = df[(df['k'] == 8) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k8j = k8j['Jaccard']

k10j = df[(df['k'] == 10) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k10j = k10j['Jaccard']

#RBO

k3r = df[(df['k'] == 3) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k3r = k3r['RBO']

k5r = df[(df['k'] == 5) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k5r = k5r['RBO']

k8r = df[(df['k'] == 8) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k8r = k8r['RBO']

k10r = df[(df['k'] == 10) & (df['percentage'] == percent) & (df['alpha'] == alpha)]
k10r = k10r['RBO']


k3j = list(mean_confidence_interval(k3j))
k3j.insert(0,3)
k3j.insert(1,'Jaccard')

k5j = list(mean_confidence_interval(k5j))
k5j.insert(0,5)
k5j.insert(1,'Jaccard')

k8j = list(mean_confidence_interval(k8j))
k8j.insert(0,8)
k8j.insert(1,'Jaccard')

k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')


k3r = list(mean_confidence_interval(k3r))
k3r.insert(0,3)
k3r.insert(1,'RBO 0.95')


k5r = list(mean_confidence_interval(k5r))
k5r.insert(0,5)
k5r.insert(1,'RBO 0.95')

k8r = list(mean_confidence_interval(k8r))
k8r.insert(0,8)
k8r.insert(1,'RBO 0.95')

k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO 0.95')





df = pd.DataFrame([k3j, k5j, k8j, k10j, k3r, k5r, k8r, k10r])
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
x = [3,5,8,10]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
