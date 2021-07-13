import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

data = df["temp"].tolist()
pmean = statistics.mean(data)
pstd = statistics.stdev(data)

print(pmean)
print(pstd)

#fig = ff.create_distplot([data],["Temp"],show_hist = False)

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

fig = ff.create_distplot([meanlist],["Temp"],show_hist = False)

fig.show()
#1.sampling mean distribution for large sample sizes are always normal distribution
#2.Sampling Mean = Population Mean
#3.Sampling Standard Deviation =Population Standard Deviation / sqrt (sampling size)