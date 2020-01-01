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

input_file1 = 'results/correlation_missing_vs_ideal.csv'
input_file2 = 'results/kurtosis_missing_vs_ideal_random.csv'
input_file3 = 'results/skewness_missing_vs_ideal_random.csv'
input_file4 = 'results/sim_missing_a_m_vs_ideal.csv'
input_file5 = 'results/div_missing_a_m_vs_ideal.csv'

output_plot = 'jaccard_10_missing_attributes_vs_ideal'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard'])

percent = 10
#[5, 10, 15, 20, 100, 256]



kj11 = df1[(df1['k'] == 1) & (df1['percentage'] == percent)]
kj11 = kj11['Jaccard']

kj12 = df1[(df1['k'] == 2) & (df1['percentage'] == percent)]
kj12 = kj12['Jaccard']

kj13 = df1[(df1['k'] == 3) & (df1['percentage'] == percent)]
kj13 = kj13['Jaccard']

kj14 = df1[(df1['k'] == 4) & (df1['percentage'] == percent)]
kj14 = kj14['Jaccard'] 

kj15 = df1[(df1['k'] == 5) & (df1['percentage'] == percent)]
kj15 = kj15['Jaccard']

kj16 = df1[(df1['k'] == 6) & (df1['percentage'] == percent)]
kj16 = kj16['Jaccard']

kj17 = df1[(df1['k'] == 7) & (df1['percentage'] == percent)]
kj17 = kj17['Jaccard']

kj18 = df1[(df1['k'] == 8) & (df1['percentage'] == percent)]
kj18 = kj18['Jaccard']

kj19 = df1[(df1['k'] == 9) & (df1['percentage'] == percent)]
kj19 = kj19['Jaccard']

kj110 = df1[(df1['k'] == 10) & (df1['percentage'] == percent)]
kj110 = kj110['Jaccard']

kj111 = df1[(df1['k'] == 11) & (df1['percentage'] == percent)]
kj111 = kj111['Jaccard']

kj112 = df1[(df1['k'] == 12) & (df1['percentage'] == percent)]
kj112 = kj112['Jaccard']


kj113 = df1[(df1['k'] == 13) & (df1['percentage'] == percent)]
kj113 = kj113['Jaccard']

kj120 = df1[(df1['k'] == 20) & (df1['percentage'] == percent)]
kj120 = kj120['Jaccard']

kj130 = df1[(df1['k'] == 30) & (df1['percentage'] == percent)]
kj130 = kj130['Jaccard']

kj140 = df1[(df1['k'] == 40) & (df1['percentage'] == percent)]
kj140 = kj140['Jaccard']


kj150 = df1[(df1['k'] == 50) & (df1['percentage'] == percent)]
kj150 = kj150['Jaccard']
kj160 = df1[(df1['k'] == 60) & (df1['percentage'] == percent)]
kj160 = kj160['Jaccard']

kj166 = df1[(df1['k'] == 66) & (df1['percentage'] == percent)]
kj166 = kj166['Jaccard']

kj1192 = df1[(df1['k'] == 192) & (df1['percentage'] == percent)]
kj1192 = kj1192['Jaccard']


kj11 = list(mean_confidence_interval(kj11))
kj11.insert(0,1)
kj11.insert(1,'Jaccard')

kj12 = list(mean_confidence_interval(kj12))
kj12.insert(0,2)
kj12.insert(1,'Jaccard')

kj13 = list(mean_confidence_interval(kj13))
kj13.insert(0,3)
kj13.insert(1,'Jaccard')

kj14 = list(mean_confidence_interval(kj14))
kj14.insert(0,4)
kj14.insert(1,'Jaccard')

kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,5)
kj15.insert(1,'Jaccard')

kj16 = list(mean_confidence_interval(kj16))
kj16.insert(0,6)
kj16.insert(1,'Jaccard')

kj17 = list(mean_confidence_interval(kj17))
kj17.insert(0,7)
kj17.insert(1,'Jaccard')

kj18 = list(mean_confidence_interval(kj18))
kj18.insert(0,8)
kj18.insert(1,'Jaccard')

kj19 = list(mean_confidence_interval(kj19))
kj19.insert(0,9)
kj19.insert(1,'Jaccard')

kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,10)
kj110.insert(1,'Jaccard')

kj111 = list(mean_confidence_interval(kj111))
kj111.insert(0,11)
kj111.insert(1,'Jaccard')

kj112 = list(mean_confidence_interval(kj112))
kj112.insert(0,12)
kj112.insert(1,'Jaccard')

kj113 = list(mean_confidence_interval(kj113))
kj113.insert(0,13)
kj113.insert(1,'Jaccard')

kj120 = list(mean_confidence_interval(kj120))
kj120.insert(0,20)
kj120.insert(1,'Jaccard')

kj130 = list(mean_confidence_interval(kj130))
kj130.insert(0,30)
kj130.insert(1,'Jaccard')

kj140 = list(mean_confidence_interval(kj140))
kj140.insert(0,40)
kj140.insert(1,'Jaccard')

kj150 = list(mean_confidence_interval(kj150))
kj150.insert(0,50)
kj150.insert(1,'Jaccard')

kj160 = list(mean_confidence_interval(kj160))
kj160.insert(0,60)
kj160.insert(1,'Jaccard')

kj166 = list(mean_confidence_interval(kj166))
kj166.insert(0,66)
kj166.insert(1,'Jaccard')

kj1192 = list(mean_confidence_interval(kj1192))
kj1192.insert(0,192)
kj1192.insert(1,'Jaccard')

df1 = pd.DataFrame([kj11, kj12, kj13, kj14, kj15, kj16, kj17, kj18, kj19, kj110, kj111, kj112, kj113, kj120, kj130, kj140, kj150, kj160, kj166, kj1192])
df1.columns = ['k','measurement','mean','lb','ub']


df2 = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard'])



kj21 = df2[(df2['k'] == 1) & (df2['percentage'] == percent)]
kj21 = kj21['Jaccard']

kj22 = df2[(df2['k'] == 2) & (df2['percentage'] == percent)]
kj22 = kj22['Jaccard']

kj23 = df2[(df2['k'] == 3) & (df2['percentage'] == percent)]
kj23 = kj23['Jaccard']

kj24 = df2[(df2['k'] == 4) & (df2['percentage'] == percent)]
kj24 = kj24['Jaccard'] 

kj25 = df2[(df2['k'] == 5) & (df2['percentage'] == percent)]
kj25 = kj25['Jaccard']

kj26 = df2[(df2['k'] == 6) & (df2['percentage'] == percent)]
kj26 = kj26['Jaccard']

kj27 = df2[(df2['k'] == 7) & (df2['percentage'] == percent)]
kj27 = kj27['Jaccard']

kj28 = df2[(df2['k'] == 8) & (df2['percentage'] == percent)]
kj28 = kj28['Jaccard']

kj29 = df2[(df2['k'] == 9) & (df2['percentage'] == percent)]
kj29 = kj29['Jaccard']

kj210 = df2[(df2['k'] == 10) & (df2['percentage'] == percent)]
kj210 = kj210['Jaccard']

kj211 = df2[(df2['k'] == 11) & (df2['percentage'] == percent)]
kj211 = kj211['Jaccard']

kj212 = df2[(df2['k'] == 12) & (df2['percentage'] == percent)]
kj212 = kj212['Jaccard']

kj213 = df2[(df2['k'] == 13) & (df2['percentage'] == percent)]
kj213 = kj213['Jaccard']

kj220 = df2[(df2['k'] == 20) & (df2['percentage'] == percent)]
kj220 = kj220['Jaccard']

kj230 = df2[(df2['k'] == 30) & (df2['percentage'] == percent)]
kj230 = kj230['Jaccard']

kj240 = df2[(df2['k'] == 40) & (df2['percentage'] == percent)]
kj240 = kj240['Jaccard']


kj250 = df2[(df2['k'] == 50) & (df2['percentage'] == percent)]
kj250 = kj250['Jaccard']
kj260 = df2[(df2['k'] == 60) & (df2['percentage'] == percent)]
kj260 = kj260['Jaccard']

kj266 = df2[(df2['k'] == 66) & (df2['percentage'] == percent)]
kj266 = kj266['Jaccard']

kj2192 = df2[(df2['k'] == 192) & (df2['percentage'] == percent)]
kj2192 = kj2192['Jaccard']


kj21 = list(mean_confidence_interval(kj21))
kj21.insert(0,1)
kj21.insert(1,'Jaccard')

kj22 = list(mean_confidence_interval(kj22))
kj22.insert(0,2)
kj22.insert(1,'Jaccard')

kj23 = list(mean_confidence_interval(kj23))
kj23.insert(0,3)
kj23.insert(1,'Jaccard')

kj24 = list(mean_confidence_interval(kj24))
kj24.insert(0,4)
kj24.insert(1,'Jaccard')

kj25 = list(mean_confidence_interval(kj25))
kj25.insert(0,5)
kj25.insert(1,'Jaccard')

kj26 = list(mean_confidence_interval(kj26))
kj26.insert(0,6)
kj26.insert(1,'Jaccard')

kj27 = list(mean_confidence_interval(kj27))
kj27.insert(0,7)
kj27.insert(1,'Jaccard')

kj28 = list(mean_confidence_interval(kj28))
kj28.insert(0,8)
kj28.insert(1,'Jaccard')

kj29 = list(mean_confidence_interval(kj29))
kj29.insert(0,9)
kj29.insert(1,'Jaccard')

kj210 = list(mean_confidence_interval(kj210))
kj210.insert(0,10)
kj210.insert(1,'Jaccard')

kj211 = list(mean_confidence_interval(kj211))
kj211.insert(0,11)
kj211.insert(1,'Jaccard')

kj212 = list(mean_confidence_interval(kj212))
kj212.insert(0,12)
kj212.insert(1,'Jaccard')

kj213 = list(mean_confidence_interval(kj213))
kj213.insert(0,13)
kj213.insert(1,'Jaccard')

kj220 = list(mean_confidence_interval(kj220))
kj220.insert(0,20)
kj220.insert(1,'Jaccard')

kj230 = list(mean_confidence_interval(kj230))
kj230.insert(0,30)
kj230.insert(1,'Jaccard')

kj240 = list(mean_confidence_interval(kj240))
kj240.insert(0,40)
kj240.insert(1,'Jaccard')

kj250 = list(mean_confidence_interval(kj250))
kj250.insert(0,50)
kj250.insert(1,'Jaccard')

kj260 = list(mean_confidence_interval(kj260))
kj260.insert(0,60)
kj260.insert(1,'Jaccard')

kj266 = list(mean_confidence_interval(kj266))
kj266.insert(0,66)
kj266.insert(1,'Jaccard')

kj2192 = list(mean_confidence_interval(kj2192))
kj2192.insert(0,192)
kj2192.insert(1,'Jaccard')

df2 = pd.DataFrame([kj21, kj22, kj23, kj24, kj25, kj26, kj27, kj28, kj29, kj210, kj211, kj212, kj213, kj220, kj230, kj240, kj250, kj260, kj266, kj2192])
df2.columns = ['k','measurement','mean','lb','ub']


df3 = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard'])



kj31 = df3[(df3['k'] == 1) & (df3['percentage'] == percent)]
kj31 = kj31['Jaccard']

kj32 = df3[(df3['k'] == 2) & (df3['percentage'] == percent)]
kj32 = kj32['Jaccard']

kj33 = df3[(df3['k'] == 3) & (df3['percentage'] == percent)]
kj33 = kj33['Jaccard']

kj34 = df3[(df3['k'] == 4) & (df3['percentage'] == percent)]
kj34 = kj34['Jaccard'] 

kj35 = df3[(df3['k'] == 5) & (df3['percentage'] == percent)]
kj35 = kj35['Jaccard']

kj36 = df3[(df3['k'] == 6) & (df3['percentage'] == percent)]
kj36 = kj36['Jaccard']

kj37 = df3[(df3['k'] == 7) & (df3['percentage'] == percent)]
kj37 = kj37['Jaccard']

kj38 = df3[(df3['k'] == 8) & (df3['percentage'] == percent)]
kj38 = kj38['Jaccard']

kj39 = df3[(df3['k'] == 9) & (df3['percentage'] == percent)]
kj39 = kj39['Jaccard']

kj310 = df3[(df3['k'] == 10) & (df3['percentage'] == percent)]
kj310 = kj310['Jaccard']

kj311 = df3[(df3['k'] == 11) & (df3['percentage'] == percent)]
kj311 = kj311['Jaccard']

kj312 = df3[(df3['k'] == 12) & (df3['percentage'] == percent)]
kj312 = kj312['Jaccard']

kj313 = df3[(df3['k'] == 13) & (df3['percentage'] == percent)]
kj313 = kj313['Jaccard']

kj320 = df3[(df3['k'] == 20) & (df3['percentage'] == percent)]
kj320 = kj320['Jaccard']

kj330 = df3[(df3['k'] == 30) & (df3['percentage'] == percent)]
kj330 = kj330['Jaccard']

kj340 = df3[(df3['k'] == 40) & (df3['percentage'] == percent)]
kj340 = kj340['Jaccard']


kj350 = df3[(df3['k'] == 50) & (df3['percentage'] == percent)]
kj350 = kj350['Jaccard']
kj360 = df3[(df3['k'] == 60) & (df3['percentage'] == percent)]
kj360 = kj360['Jaccard']

kj366 = df3[(df3['k'] == 66) & (df3['percentage'] == percent)]
kj366 = kj366['Jaccard']

kj3192 = df3[(df3['k'] == 192) & (df3['percentage'] == percent)]
kj3192 = kj3192['Jaccard']


kj31 = list(mean_confidence_interval(kj31))
kj31.insert(0,1)
kj31.insert(1,'Jaccard')

kj32 = list(mean_confidence_interval(kj32))
kj32.insert(0,2)
kj32.insert(1,'Jaccard')

kj33 = list(mean_confidence_interval(kj33))
kj33.insert(0,3)
kj33.insert(1,'Jaccard')

kj34 = list(mean_confidence_interval(kj34))
kj34.insert(0,4)
kj34.insert(1,'Jaccard')

kj35 = list(mean_confidence_interval(kj35))
kj35.insert(0,5)
kj35.insert(1,'Jaccard')

kj36 = list(mean_confidence_interval(kj36))
kj36.insert(0,6)
kj36.insert(1,'Jaccard')

kj37 = list(mean_confidence_interval(kj37))
kj37.insert(0,7)
kj37.insert(1,'Jaccard')

kj38 = list(mean_confidence_interval(kj38))
kj38.insert(0,8)
kj38.insert(1,'Jaccard')

kj39 = list(mean_confidence_interval(kj39))
kj39.insert(0,9)
kj39.insert(1,'Jaccard')

kj310 = list(mean_confidence_interval(kj310))
kj310.insert(0,10)
kj310.insert(1,'Jaccard')

kj311 = list(mean_confidence_interval(kj311))
kj311.insert(0,11)
kj311.insert(1,'Jaccard')

kj312 = list(mean_confidence_interval(kj312))
kj312.insert(0,12)
kj312.insert(1,'Jaccard')

kj313 = list(mean_confidence_interval(kj313))
kj313.insert(0,13)
kj313.insert(1,'Jaccard')

kj320 = list(mean_confidence_interval(kj320))
kj320.insert(0,20)
kj320.insert(1,'Jaccard')

kj330 = list(mean_confidence_interval(kj330))
kj330.insert(0,30)
kj330.insert(1,'Jaccard')

kj340 = list(mean_confidence_interval(kj340))
kj340.insert(0,40)
kj340.insert(1,'Jaccard')

kj350 = list(mean_confidence_interval(kj350))
kj350.insert(0,50)
kj350.insert(1,'Jaccard')

kj360 = list(mean_confidence_interval(kj360))
kj360.insert(0,60)
kj360.insert(1,'Jaccard')

kj366 = list(mean_confidence_interval(kj366))
kj366.insert(0,66)
kj366.insert(1,'Jaccard')

kj3192 = list(mean_confidence_interval(kj3192))
kj3192.insert(0,192)
kj3192.insert(1,'Jaccard')

df3 = pd.DataFrame([kj31, kj32, kj33, kj34, kj35, kj36, kj37, kj38, kj39, kj310, kj311, kj312, kj313, kj320, kj330, kj340, kj350, kj360, kj366, kj3192])
df3.columns = ['k','measurement','mean','lb','ub']


df4 = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard'])



kj41 = df4[(df4['k'] == 1) & (df4['percentage'] == percent)]
kj41 = kj41['Jaccard']

kj42 = df4[(df4['k'] == 2) & (df4['percentage'] == percent)]
kj42 = kj42['Jaccard']

kj43 = df4[(df4['k'] == 3) & (df4['percentage'] == percent)]
kj43 = kj43['Jaccard']

kj44 = df4[(df4['k'] == 4) & (df4['percentage'] == percent)]
kj44 = kj44['Jaccard'] 

kj45 = df4[(df4['k'] == 5) & (df4['percentage'] == percent)]
kj45 = kj45['Jaccard']

kj46 = df4[(df4['k'] == 6) & (df4['percentage'] == percent)]
kj46 = kj46['Jaccard']

kj47 = df4[(df4['k'] == 7) & (df4['percentage'] == percent)]
kj47 = kj47['Jaccard']

kj48 = df4[(df4['k'] == 8) & (df4['percentage'] == percent)]
kj48 = kj48['Jaccard']

kj49 = df4[(df4['k'] == 9) & (df4['percentage'] == percent)]
kj49 = kj49['Jaccard']

kj410 = df4[(df4['k'] == 10) & (df4['percentage'] == percent)]
kj410 = kj410['Jaccard']

kj411 = df4[(df4['k'] == 11) & (df4['percentage'] == percent)]
kj411 = kj411['Jaccard']

kj412 = df4[(df4['k'] == 12) & (df4['percentage'] == percent)]
kj412 = kj412['Jaccard']

kj413 = df4[(df4['k'] == 13) & (df4['percentage'] == percent)]
kj413 = kj413['Jaccard']

kj420 = df4[(df4['k'] == 20) & (df4['percentage'] == percent)]
kj420 = kj420['Jaccard']

kj430 = df4[(df4['k'] == 30) & (df4['percentage'] == percent)]
kj430 = kj430['Jaccard']

kj440 = df4[(df4['k'] == 40) & (df4['percentage'] == percent)]
kj440 = kj440['Jaccard']


kj450 = df4[(df4['k'] == 50) & (df4['percentage'] == percent)]
kj450 = kj450['Jaccard']
kj460 = df4[(df4['k'] == 60) & (df4['percentage'] == percent)]
kj460 = kj460['Jaccard']

kj466 = df4[(df4['k'] == 66) & (df4['percentage'] == percent)]
kj466 = kj466['Jaccard']

kj4192 = df4[(df4['k'] == 192) & (df4['percentage'] == percent)]
kj4192 = kj4192['Jaccard']


kj41 = list(mean_confidence_interval(kj41))
kj41.insert(0,1)
kj41.insert(1,'Jaccard')

kj42 = list(mean_confidence_interval(kj42))
kj42.insert(0,2)
kj42.insert(1,'Jaccard')

kj43 = list(mean_confidence_interval(kj43))
kj43.insert(0,3)
kj43.insert(1,'Jaccard')

kj44 = list(mean_confidence_interval(kj44))
kj44.insert(0,4)
kj44.insert(1,'Jaccard')

kj45 = list(mean_confidence_interval(kj45))
kj45.insert(0,5)
kj45.insert(1,'Jaccard')

kj46 = list(mean_confidence_interval(kj46))
kj46.insert(0,6)
kj46.insert(1,'Jaccard')

kj47 = list(mean_confidence_interval(kj47))
kj47.insert(0,7)
kj47.insert(1,'Jaccard')

kj48 = list(mean_confidence_interval(kj48))
kj48.insert(0,8)
kj48.insert(1,'Jaccard')

kj49 = list(mean_confidence_interval(kj49))
kj49.insert(0,9)
kj49.insert(1,'Jaccard')

kj410 = list(mean_confidence_interval(kj410))
kj410.insert(0,10)
kj410.insert(1,'Jaccard')

kj411 = list(mean_confidence_interval(kj411))
kj411.insert(0,11)
kj411.insert(1,'Jaccard')

kj412 = list(mean_confidence_interval(kj412))
kj412.insert(0,12)
kj412.insert(1,'Jaccard')

kj413 = list(mean_confidence_interval(kj413))
kj413.insert(0,13)
kj413.insert(1,'Jaccard')

kj420 = list(mean_confidence_interval(kj420))
kj420.insert(0,20)
kj420.insert(1,'Jaccard')

kj430 = list(mean_confidence_interval(kj430))
kj430.insert(0,30)
kj430.insert(1,'Jaccard')

kj440 = list(mean_confidence_interval(kj440))
kj440.insert(0,40)
kj440.insert(1,'Jaccard')

kj450 = list(mean_confidence_interval(kj450))
kj450.insert(0,50)
kj450.insert(1,'Jaccard')

kj460 = list(mean_confidence_interval(kj460))
kj460.insert(0,60)
kj460.insert(1,'Jaccard')

kj466 = list(mean_confidence_interval(kj466))
kj466.insert(0,66)
kj466.insert(1,'Jaccard')

kj4192 = list(mean_confidence_interval(kj4192))
kj4192.insert(0,192)
kj4192.insert(1,'Jaccard')

df4 = pd.DataFrame([kj41, kj42, kj43, kj44, kj45, kj46, kj47, kj48, kj49, kj410, kj411, kj412, kj413, kj420, kj430, kj440, kj450, kj460, kj466, kj4192])
df4.columns = ['k','measurement','mean','lb','ub']


df5 = pd.read_csv(input_file5, names=['percentage','k','RBO','Jaccard'])


kj51 = df5[(df5['k'] == 1) & (df5['percentage'] == percent)]
kj51 = kj51['Jaccard']

kj52 = df5[(df5['k'] == 2) & (df5['percentage'] == percent)]
kj52 = kj52['Jaccard']

kj53 = df5[(df5['k'] == 3) & (df5['percentage'] == percent)]
kj53 = kj53['Jaccard']

kj54 = df5[(df5['k'] == 4) & (df5['percentage'] == percent)]
kj54 = kj54['Jaccard'] 

kj55 = df5[(df5['k'] == 5) & (df5['percentage'] == percent)]
kj55 = kj55['Jaccard']

kj56 = df5[(df5['k'] == 6) & (df5['percentage'] == percent)]
kj56 = kj56['Jaccard']

kj57 = df5[(df5['k'] == 7) & (df5['percentage'] == percent)]
kj57 = kj57['Jaccard']

kj58 = df5[(df5['k'] == 8) & (df5['percentage'] == percent)]
kj58 = kj58['Jaccard']

kj59 = df5[(df5['k'] == 9) & (df5['percentage'] == percent)]
kj59 = kj59['Jaccard']

kj510 = df5[(df5['k'] == 10) & (df5['percentage'] == percent)]
kj510 = kj510['Jaccard']

kj511 = df5[(df5['k'] == 11) & (df5['percentage'] == percent)]
kj511 = kj511['Jaccard']

kj512 = df5[(df5['k'] == 12) & (df5['percentage'] == percent)]
kj512 = kj512['Jaccard']

kj513 = df5[(df5['k'] == 13) & (df5['percentage'] == percent)]
kj513 = kj513['Jaccard']

kj520 = df5[(df5['k'] == 20) & (df5['percentage'] == percent)]
kj520 = kj520['Jaccard']

kj530 = df5[(df5['k'] == 30) & (df5['percentage'] == percent)]
kj530 = kj530['Jaccard']

kj540 = df5[(df5['k'] == 40) & (df5['percentage'] == percent)]
kj540 = kj540['Jaccard']


kj550 = df5[(df5['k'] == 50) & (df5['percentage'] == percent)]
kj550 = kj550['Jaccard']
kj560 = df5[(df5['k'] == 60) & (df5['percentage'] == percent)]
kj560 = kj560['Jaccard']

kj566 = df5[(df5['k'] == 66) & (df5['percentage'] == percent)]
kj566 = kj566['Jaccard']

kj5192 = df5[(df5['k'] == 192) & (df5['percentage'] == percent)]
kj5192 = kj5192['Jaccard']


kj51 = list(mean_confidence_interval(kj51))
kj51.insert(0,1)
kj51.insert(1,'Jaccard')

kj52 = list(mean_confidence_interval(kj52))
kj52.insert(0,2)
kj52.insert(1,'Jaccard')

kj53 = list(mean_confidence_interval(kj53))
kj53.insert(0,3)
kj53.insert(1,'Jaccard')

kj54 = list(mean_confidence_interval(kj54))
kj54.insert(0,4)
kj54.insert(1,'Jaccard')

kj55 = list(mean_confidence_interval(kj55))
kj55.insert(0,5)
kj55.insert(1,'Jaccard')

kj56 = list(mean_confidence_interval(kj56))
kj56.insert(0,6)
kj56.insert(1,'Jaccard')

kj57 = list(mean_confidence_interval(kj57))
kj57.insert(0,7)
kj57.insert(1,'Jaccard')

kj58 = list(mean_confidence_interval(kj58))
kj58.insert(0,8)
kj58.insert(1,'Jaccard')

kj59 = list(mean_confidence_interval(kj59))
kj59.insert(0,9)
kj59.insert(1,'Jaccard')

kj510 = list(mean_confidence_interval(kj510))
kj510.insert(0,10)
kj510.insert(1,'Jaccard')

kj511 = list(mean_confidence_interval(kj511))
kj511.insert(0,11)
kj511.insert(1,'Jaccard')

kj512 = list(mean_confidence_interval(kj512))
kj512.insert(0,12)
kj512.insert(1,'Jaccard')

kj513 = list(mean_confidence_interval(kj513))
kj513.insert(0,13)
kj513.insert(1,'Jaccard')

kj520 = list(mean_confidence_interval(kj520))
kj520.insert(0,20)
kj520.insert(1,'Jaccard')

kj530 = list(mean_confidence_interval(kj530))
kj530.insert(0,30)
kj530.insert(1,'Jaccard')

kj540 = list(mean_confidence_interval(kj540))
kj540.insert(0,40)
kj540.insert(1,'Jaccard')

kj550 = list(mean_confidence_interval(kj550))
kj550.insert(0,50)
kj550.insert(1,'Jaccard')

kj560 = list(mean_confidence_interval(kj560))
kj560.insert(0,60)
kj560.insert(1,'Jaccard')

kj566 = list(mean_confidence_interval(kj566))
kj566.insert(0,66)
kj566.insert(1,'Jaccard')

kj5192 = list(mean_confidence_interval(kj5192))
kj5192.insert(0,192)
kj5192.insert(1,'Jaccard')

df5 = pd.DataFrame([kj51, kj52, kj53, kj54, kj55, kj56, kj57, kj58, kj59, kj510, kj511, kj512, kj513, kj520, kj530, kj540, kj550, kj560, kj566, kj5192])
df5.columns = ['k','measurement','mean','lb','ub']





mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
lb4 = lb4['lb']

mean5 = df5[df5['measurement'] == 'Jaccard'].reset_index()
mean5 = mean5['mean']
ub5 = df5[df5['measurement'] == 'Jaccard'].reset_index()
ub5 = ub5['ub']
lb5 = df5[df5['measurement'] == 'Jaccard'].reset_index()
lb5 = lb5['lb']


# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (60, 14))
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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = '+ Correlation', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = '+ Kurtosis', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = '+ Skewness', marker='o', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Similarity to reference', marker='s', linestyle='--', linewidth=2, markersize=12)
ax.plot(mean5, lw = 1, color = '#0d0e0f', alpha = 1, label = 'Deviation/outstanding', marker='x', linestyle='-.', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)
ax.fill_between(t, lb5, ub5, color = '#87888a', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness Jaccard- Missing to Ideal")
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,20,30,40,50,60,66, 192]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
