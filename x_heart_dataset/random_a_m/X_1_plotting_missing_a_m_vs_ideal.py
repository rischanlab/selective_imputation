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

output_plot = '10_cum_missing_a_m_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['percentage','k','Cum_distance'])

percent = 10


#Cum_distance
kj11 = df1[(df1['k'] == 1) & (df1['percentage'] == percent)]
kj11 = kj11['Cum_distance']

kj12 = df1[(df1['k'] == 2) & (df1['percentage'] == percent)]
kj12 = kj12['Cum_distance']

kj13 = df1[(df1['k'] == 3) & (df1['percentage'] == percent)]
kj13 = kj13['Cum_distance']

kj14 = df1[(df1['k'] == 4) & (df1['percentage'] == percent)]
kj14 = kj14['Cum_distance'] 

kj15 = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
kj15 = kj15['Cum_distance']

kj16 = df1[(df1['k'] == 6) & (df1['percentage'] == percent)]
kj16 = kj16['Cum_distance']

kj17 = df1[(df1['k'] == 7) & (df1['percentage'] == percent)]
kj17 = kj17['Cum_distance']

kj18 = df1[(df1['k'] == 8) & (df1['percentage'] == percent)]
kj18 = kj18['Cum_distance']

kj19 = df1[(df1['k'] == 9) & (df1['percentage'] == percent)]
kj19 = kj19['Cum_distance']

kj110 = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
kj110 = kj110['Cum_distance']

kj111 = df1[(df1['k'] == 11) & (df1['percentage'] == percent)]
kj111 = kj111['Cum_distance']

kj112 = df1[(df1['k'] == 12) & (df1['percentage'] == percent)]
kj112 = kj112['Cum_distance']


kj113 = df1[(df1['k'] == 13) & (df1['percentage'] == percent)]
kj113 = kj113['Cum_distance']

kj120 = df1[(df1['k'] == 20) & (df1['percentage'] == percent)]
kj120 = kj120['Cum_distance']

kj130 = df1[(df1['k'] == 30) & (df1['percentage'] == percent)]
kj130 = kj130['Cum_distance']

kj140 = df1[(df1['k'] == 40) & (df1['percentage'] == percent)]
kj140 = kj140['Cum_distance']


kj150 = df1[(df1['k'] == 50) & (df1['percentage'] == percent)]
kj150 = kj150['Cum_distance']
kj160 = df1[(df1['k'] == 60) & (df1['percentage'] == percent)]
kj160 = kj160['Cum_distance']

kj166 = df1[(df1['k'] == 66) & (df1['percentage'] == percent)]
kj166 = kj166['Cum_distance']

kj1192 = df1[(df1['k'] == 192) & (df1['percentage'] == percent)]
kj1192 = kj1192['Cum_distance']


kj11 = list(mean_confidence_interval(kj11))
kj11.insert(0,1)
kj11.insert(1,'Cum_distance')

kj12 = list(mean_confidence_interval(kj12))
kj12.insert(0,2)
kj12.insert(1,'Cum_distance')

kj13 = list(mean_confidence_interval(kj13))
kj13.insert(0,3)
kj13.insert(1,'Cum_distance')

kj14 = list(mean_confidence_interval(kj14))
kj14.insert(0,4)
kj14.insert(1,'Cum_distance')

kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,5)
kj15.insert(1,'Cum_distance')

kj16 = list(mean_confidence_interval(kj16))
kj16.insert(0,6)
kj16.insert(1,'Cum_distance')

kj17 = list(mean_confidence_interval(kj17))
kj17.insert(0,7)
kj17.insert(1,'Cum_distance')

kj18 = list(mean_confidence_interval(kj18))
kj18.insert(0,8)
kj18.insert(1,'Cum_distance')

kj19 = list(mean_confidence_interval(kj19))
kj19.insert(0,9)
kj19.insert(1,'Cum_distance')

kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,10)
kj110.insert(1,'Cum_distance')

kj111 = list(mean_confidence_interval(kj111))
kj111.insert(0,11)
kj111.insert(1,'Cum_distance')

kj112 = list(mean_confidence_interval(kj112))
kj112.insert(0,12)
kj112.insert(1,'Cum_distance')

kj113 = list(mean_confidence_interval(kj113))
kj113.insert(0,13)
kj113.insert(1,'Cum_distance')

kj120 = list(mean_confidence_interval(kj120))
kj120.insert(0,20)
kj120.insert(1,'Cum_distance')

kj130 = list(mean_confidence_interval(kj130))
kj130.insert(0,30)
kj130.insert(1,'Cum_distance')

kj140 = list(mean_confidence_interval(kj140))
kj140.insert(0,40)
kj140.insert(1,'Cum_distance')

kj150 = list(mean_confidence_interval(kj150))
kj150.insert(0,50)
kj150.insert(1,'Cum_distance')

kj160 = list(mean_confidence_interval(kj160))
kj160.insert(0,60)
kj160.insert(1,'Cum_distance')

kj166 = list(mean_confidence_interval(kj166))
kj166.insert(0,66)
kj166.insert(1,'Cum_distance')

kj1192 = list(mean_confidence_interval(kj1192))
kj1192.insert(0,192)
kj1192.insert(1,'Cum_distance')

df1 = pd.DataFrame([kj11, kj12, kj13, kj14, kj15, kj16, kj17, kj18, kj19, kj110, kj111, kj112, kj113, kj120, kj130, kj140, kj150, kj160, kj166, kj1192])
df1.columns = ['k','measurement','mean','lb','ub']


df2 = pd.read_csv(input_file2, names=['percentage','k','Cum_distance'])


kj221 = df2[(df2['k'] == 1) & (df2['percentage'] == percent)]
kj221 = kj221['Cum_distance']

kj222 = df2[(df2['k'] == 2) & (df2['percentage'] == percent)]
kj222 = kj222['Cum_distance']

kj223 = df2[(df2['k'] == 3) & (df2['percentage'] == percent)]
kj223 = kj223['Cum_distance']

kj224 = df2[(df2['k'] == 4) & (df2['percentage'] == percent)]
kj224 = kj224['Cum_distance'] 

kj225 = df2[(df2['k'] == 5) & (df2['percentage'] == percent)]
kj225 = kj225['Cum_distance']

kj226 = df2[(df2['k'] == 6) & (df2['percentage'] == percent)]
kj226 = kj226['Cum_distance']

kj227 = df2[(df2['k'] == 7) & (df2['percentage'] == percent)]
kj227 = kj227['Cum_distance']

kj228 = df2[(df2['k'] == 8) & (df2['percentage'] == percent)]
kj228 = kj228['Cum_distance']

kj229 = df2[(df2['k'] == 9) & (df2['percentage'] == percent)]
kj229 = kj229['Cum_distance']

kj2210 = df2[(df2['k'] == 10) & (df2['percentage'] == percent)]
kj2210 = kj2210['Cum_distance']

kj2211 = df2[(df2['k'] == 11) & (df2['percentage'] == percent)]
kj2211 = kj2211['Cum_distance']

kj2212 = df2[(df2['k'] == 12) & (df2['percentage'] == percent)]
kj2212 = kj2212['Cum_distance']


kj2213 = df2[(df2['k'] == 13) & (df2['percentage'] == percent)]
kj2213 = kj2213['Cum_distance']

kj2220 = df2[(df2['k'] == 20) & (df2['percentage'] == percent)]
kj2220 = kj2220['Cum_distance']

kj2230 = df2[(df2['k'] == 30) & (df2['percentage'] == percent)]
kj2230 = kj2230['Cum_distance']

kj2240 = df2[(df2['k'] == 40) & (df2['percentage'] == percent)]
kj2240 = kj2240['Cum_distance']


kj2250 = df2[(df2['k'] == 50) & (df2['percentage'] == percent)]
kj2250 = kj2250['Cum_distance']
kj2260 = df2[(df2['k'] == 60) & (df2['percentage'] == percent)]
kj2260 = kj2260['Cum_distance']

kj2266 = df2[(df2['k'] == 66) & (df2['percentage'] == percent)]
kj2266 = kj2266['Cum_distance']

kj22192 = df2[(df2['k'] == 192) & (df2['percentage'] == percent)]
kj22192 = kj22192['Cum_distance']


kj221 = list(mean_confidence_interval(kj221))
kj221.insert(0,1)
kj221.insert(1,'Cum_distance')

kj222 = list(mean_confidence_interval(kj222))
kj222.insert(0,2)
kj222.insert(1,'Cum_distance')

kj223 = list(mean_confidence_interval(kj223))
kj223.insert(0,3)
kj223.insert(1,'Cum_distance')

kj224 = list(mean_confidence_interval(kj224))
kj224.insert(0,4)
kj224.insert(1,'Cum_distance')

kj225 = list(mean_confidence_interval(kj225))
kj225.insert(0,5)
kj225.insert(1,'Cum_distance')

kj226 = list(mean_confidence_interval(kj226))
kj226.insert(0,6)
kj226.insert(1,'Cum_distance')

kj227 = list(mean_confidence_interval(kj227))
kj227.insert(0,7)
kj227.insert(1,'Cum_distance')

kj228 = list(mean_confidence_interval(kj228))
kj228.insert(0,8)
kj228.insert(1,'Cum_distance')

kj229 = list(mean_confidence_interval(kj229))
kj229.insert(0,9)
kj229.insert(1,'Cum_distance')

kj2210 = list(mean_confidence_interval(kj2210))
kj2210.insert(0,10)
kj2210.insert(1,'Cum_distance')

kj2211 = list(mean_confidence_interval(kj2211))
kj2211.insert(0,11)
kj2211.insert(1,'Cum_distance')

kj2212 = list(mean_confidence_interval(kj2212))
kj2212.insert(0,12)
kj2212.insert(1,'Cum_distance')

kj2213 = list(mean_confidence_interval(kj2213))
kj2213.insert(0,13)
kj2213.insert(1,'Cum_distance')

kj2220 = list(mean_confidence_interval(kj2220))
kj2220.insert(0,20)
kj2220.insert(1,'Cum_distance')

kj2230 = list(mean_confidence_interval(kj2230))
kj2230.insert(0,30)
kj2230.insert(1,'Cum_distance')

kj2240 = list(mean_confidence_interval(kj2240))
kj2240.insert(0,40)
kj2240.insert(1,'Cum_distance')

kj2250 = list(mean_confidence_interval(kj2250))
kj2250.insert(0,50)
kj2250.insert(1,'Cum_distance')

kj2260 = list(mean_confidence_interval(kj2260))
kj2260.insert(0,60)
kj2260.insert(1,'Cum_distance')

kj2266 = list(mean_confidence_interval(kj2266))
kj2266.insert(0,66)
kj2266.insert(1,'Cum_distance')

kj22192 = list(mean_confidence_interval(kj22192))
kj22192.insert(0,192)
kj22192.insert(1,'Cum_distance')

df2 = pd.DataFrame([kj221, kj222, kj223, kj224, kj225, kj226, kj227, kj228, kj229, kj2210, kj2211, kj2212, kj2213, kj2220, kj2230, kj2240, kj2250, kj2260, kj2266, kj22192])
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
matplotlib.rc('figure', figsize = (28, 14))
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
#ax.plot(mean0, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean1, lw = 1, color = '#b65332', alpha = 1, label = 'Deviation/Outstanding', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#539caf', alpha = 1, label = 'Similarity', marker='x', linestyle='-.', linewidth=2, markersize=12)

# Shade the confidence interval
#ax.fill_between(t, lb0, ub0, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#539caf', alpha = 0.4)

# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % A and M missing")
ax.set_xlabel("k")
ax.set_ylabel("Cumulative distance gap to ideal")
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,20,30,40,50,60,66, 192]
xi = list(range(len(x)))
plt.xticks(xi, x)
ax.invert_yaxis()
# Display legend
#ax.set_ylim(ymin=0.0)
#ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
