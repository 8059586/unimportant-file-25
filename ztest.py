import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist()
pmean = statistics.mean(data)
pstd = statistics.stdev(data)

print(pmean)
print(pstd)

#fig = ff.create_distplot([data],["Math_score"],show_hist = False)

#fig.show()

meanlist = []
for i in range(1000):
    dataset = []
    for g in range(100):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    meanlist.append(mean)

smean = statistics.mean(meanlist)
sstd = statistics.stdev(meanlist)

print(smean)
print(sstd)

fig = ff.create_distplot([meanlist],["Math_score"],show_hist = False)
#fig.show()
#1.sampling mean distribution for large sample sizes are always normal distribution
#2.Sampling Mean = Population Mean
#3.Sampling Standard Deviation =Population Standard Deviation / sqrt (sampling size)

firststdstart,firststdend = smean-sstd,smean+sstd
secondstdstart,secondstdend = smean-(2*sstd),smean+(2*sstd)
thirdstdstart,thirdstdend = smean-(3*sstd),smean+(3*sstd)

fig.add_trace(go.Scatter(x = [smean,smean],y = [0,0.18],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.18],mode = "lines",name = "sstd1"))
fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.18],mode = "lines",name = "sstd1"))
fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.18],mode = "lines",name = "sstd2"))
fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.18],mode = "lines",name = "sstd2"))
fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.18],mode = "lines",name = "sstd3"))
fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.18],mode = "lines",name = "sstd3"))


df1 = pd.read_csv("data1.csv")

data1 = df["Math_score"].tolist()
mean1 = statistics.mean(data1)

print(mean1)

fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.18],mode = "lines",name = "mean1"))

df2 = pd.read_csv("data2.csv")

data2 = df["Math_score"].tolist()
mean2 = statistics.mean(data2)

print(mean2)

fig.add_trace(go.Scatter(x = [mean2,mean2],y = [0,0.18],mode = "lines",name = "mean2"))

df3 = pd.read_csv("data3.csv")

data3 = df["Math_score"].tolist()
mean3 = statistics.mean(data3)

print(mean3)

fig.add_trace(go.Scatter(x = [mean3,mean3],y = [0,0.18],mode = "lines",name = "mean3"))

fig.show()

zscore1 = (smean-mean1)/sstd
zscore2 = (smean-mean2)/sstd
zscore3 = (smean-mean3)/sstd

print(zscore1)
print(zscore2)
print(zscore3)