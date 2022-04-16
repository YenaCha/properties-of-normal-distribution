import pandas as pd
import plotly.figure_factory as ff
import statistics as st

df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 109/StudentsPerformance.csv')
math = df["math score"].tolist()
graph = ff.create_distplot([math],['math score'],show_hist=False)
#graph.show()

mean = st.mean(math)
std = st.stdev(math)
fs = mean-std
fe = mean+std
ss = mean-2*std
se = mean+2*std
ts = mean-3*std
te = mean+3*std

fstd = []
for f in math:
    if(fs <= f and f <= fe):
        fstd.append(f)
fp = (len(fstd)/len(math))*100
print(fp)

sstd = []
for f in math:
    if(ss <= f and f <= se):
        sstd.append(f)
sp = (len(sstd)/len(math))*100
print(sp)

tstd = []
for f in math:
    if(ts <= f and f <= te):
        tstd.append(f)
tp = (len(tstd)/len(math))*100
print(tp)