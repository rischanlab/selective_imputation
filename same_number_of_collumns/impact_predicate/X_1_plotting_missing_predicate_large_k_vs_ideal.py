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

input_file = 'results/large_k_missing_predicate_vs_ideal.csv'

output_plot = '50_large_k_missing_predicate_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df = pd.read_csv(input_file, names=['percentage','k','RBO','Jaccard'])

percent = 50
#[5, 10, 15, 20, 100, 256]
k10j = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10j = k10j['Jaccard']
k20j = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20j = k20j['Jaccard']
k30j = df[(df['k'] == 30) & (df['percentage'] == percent)]
k30j = k30j['Jaccard']
k40j = df[(df['k'] == 40) & (df['percentage'] == percent)]
k40j = k40j['Jaccard']
k50j = df[(df['k'] == 50) & (df['percentage'] == percent)]
k50j = k50j['Jaccard']
k60j = df[(df['k'] == 60) & (df['percentage'] == percent)]
k60j = k60j['Jaccard']
k70j = df[(df['k'] == 70) & (df['percentage'] == percent)]
k70j = k70j['Jaccard']
k80j = df[(df['k'] == 80) & (df['percentage'] == percent)]
k80j = k80j['Jaccard']
k90j = df[(df['k'] == 90) & (df['percentage'] == percent)]
k90j = k90j['Jaccard']
k100j = df[(df['k'] == 100) & (df['percentage'] == percent)]
k100j = k100j['Jaccard']
k256j = df[(df['k'] == 256) & (df['percentage'] == percent)]
k256j = k256j['Jaccard']

#RBO
k10r = df[(df['k'] == 10) & (df['percentage'] == percent)]
k10r = k10r['RBO']
k20r = df[(df['k'] == 20) & (df['percentage'] == percent)]
k20r = k20r['RBO']
k30r = df[(df['k'] == 30) & (df['percentage'] == percent)]
k30r = k30r['RBO']
k40r = df[(df['k'] == 40) & (df['percentage'] == percent)]
k40r = k40r['RBO']
k50r = df[(df['k'] == 50) & (df['percentage'] == percent)]
k50r = k50r['RBO']
k60r = df[(df['k'] == 60) & (df['percentage'] == percent)]
k60r = k60r['RBO']
k70r = df[(df['k'] == 70) & (df['percentage'] == percent)]
k70r = k70r['RBO']
k80r = df[(df['k'] == 80) & (df['percentage'] == percent)]
k80r = k80r['RBO']
k90r = df[(df['k'] == 90) & (df['percentage'] == percent)]
k90r = k90r['RBO']
k100r = df[(df['k'] == 100) & (df['percentage'] == percent)]
k100r = k100r['RBO']
k256r = df[(df['k'] == 256) & (df['percentage'] == percent)]
k256r = k256r['RBO']

k10j = list(mean_confidence_interval(k10j))
k10j.insert(0,10)
k10j.insert(1,'Jaccard')
k20j = list(mean_confidence_interval(k20j))
k20j.insert(0,20)
k20j.insert(1,'Jaccard')
k30j = list(mean_confidence_interval(k30j))
k30j.insert(0,30)
k30j.insert(1,'Jaccard')
k40j = list(mean_confidence_interval(k40j))
k40j.insert(0,40)
k40j.insert(1,'Jaccard')
k50j = list(mean_confidence_interval(k50j))
k50j.insert(0,50)
k50j.insert(1,'Jaccard')
k60j = list(mean_confidence_interval(k60j))
k60j.insert(0,60)
k60j.insert(1,'Jaccard')
k70j = list(mean_confidence_interval(k70j))
k70j.insert(0,70)
k70j.insert(1,'Jaccard')
k80j = list(mean_confidence_interval(k80j))
k80j.insert(0,80)
k80j.insert(1,'Jaccard')
k90j = list(mean_confidence_interval(k90j))
k90j.insert(0,90)
k90j.insert(1,'Jaccard')

k100j = list(mean_confidence_interval(k100j))
k100j.insert(0,100)
k100j.insert(1,'Jaccard')
k256j = list(mean_confidence_interval(k256j))
k256j.insert(0,256)
k256j.insert(1,'Jaccard')

k10r = list(mean_confidence_interval(k10r))
k10r.insert(0,10)
k10r.insert(1,'RBO')
k20r = list(mean_confidence_interval(k20r))
k20r.insert(0,20)
k20r.insert(1,'RBO')
k30r = list(mean_confidence_interval(k30r))
k30r.insert(0,30)
k30r.insert(1,'RBO')
k40r = list(mean_confidence_interval(k40r))
k40r.insert(0,40)
k40r.insert(1,'RBO')
k50r = list(mean_confidence_interval(k50r))
k50r.insert(0,50)
k50r.insert(1,'RBO')
k60r = list(mean_confidence_interval(k60r))
k60r.insert(0,60)
k60r.insert(1,'RBO')
k70r = list(mean_confidence_interval(k70r))
k70r.insert(0,70)
k70r.insert(1,'RBO')
k80r = list(mean_confidence_interval(k80r))
k80r.insert(0,80)
k80r.insert(1,'RBO')
k90r = list(mean_confidence_interval(k90r))
k90r.insert(0,90)
k90r.insert(1,'RBO')

k100r = list(mean_confidence_interval(k100r))
k100r.insert(0,100)
k100r.insert(1,'RBO')
k256r = list(mean_confidence_interval(k256r))
k256r.insert(0,256)
k256r.insert(1,'RBO')

df = pd.DataFrame([k10j, k20j, k30j,k40j,k50j, k60j, k70j,k80j, k90j, k100j,k256j,k10r, k20r, k30r,k40r,k50r, k60r, k70r,k80r, k90r, k100r,k256r])
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
ax.set_title("Impact of k on Effectiveness, 95% CI, 50 % predicate missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness - Missing on predicate to Ideal")
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 256]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
