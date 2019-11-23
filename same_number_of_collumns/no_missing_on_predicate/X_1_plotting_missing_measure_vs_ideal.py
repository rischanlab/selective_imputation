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

input_file = 'results/missing_measures_vs_ideal.csv'

output_plot = '10_missing_measures_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['percentage','k','RBO','Jaccard'])

percent = 10
#[5, 10, 15, 20, 100, 256]
k5j = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5j = k5j['Jaccard']
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['Jaccard']
k15j = df[(df['k'] == 15) & (df['percentage'] == percent)]
k15j = k15j['Jaccard']
k20j = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20j = k20j['Jaccard']

k80j = df[(df['k'] == 70) & (df['percentage'] == percent)]
k80j = k80j['Jaccard']


k100j = df[(df['k'] == 100) & (df['percentage'] == percent)]
k100j = k100j['Jaccard']
k256j = df[(df['k'] == 256) & (df['percentage'] == percent)]
k256j = k256j['Jaccard']

#RBO
k5r = df[(df['k'] == 5) & (df['percentage'] == percent)]
k5r = k5r['RBO']
k10r = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10r = k10r['RBO']
k15r = df[(df['k'] == 15) & (df['percentage'] == percent)]
k15r = k15r['RBO']
k20r = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20r = k20r['RBO']

k80r = df[(df['k'] == 70) & (df['percentage'] == percent)]
k80r = k80r['RBO']

k100r = df[(df['k'] == 100) & (df['percentage'] == percent)]
k100r = k100r['RBO']
k256r = df[(df['k'] == 256) & (df['percentage'] == percent)]
k256r = k256r['RBO']

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

k80j = list(mean_confidence_interval(k80j))
k80j.insert(0,70)
k80j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,100)
k100j.insert(1,'Jaccard')
k256j = list(mean_confidence_interval(k256j))
k256j.insert(0,256)
k256j.insert(1,'Jaccard')

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

k80r = list(mean_confidence_interval(k80r))
k80r.insert(0,70)
k80r.insert(1,'RBO 0.95')

k100r = list(mean_confidence_interval(k100r))
k100r.insert(0,100)
k100r.insert(1,'RBO 0.95')
k256r = list(mean_confidence_interval(k256r))
k256r.insert(0,256)
k256r.insert(1,'RBO 0.95')

df = pd.DataFrame([k5j, k10j, k15j,k20j, k80j, k100j,k256j, k5r, k10r, k15r,k20r, k80r, k100r,k256r])
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
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % M missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Missing on M to Ideal")
x = [5, 10, 15, 20, 70, 100, 256]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
