import pandas as pd
import plotly.figure_factory as ff
import statistics as st

df = pd.read_csv('C:/Users/yena0/Downloads/Python/class 109/height-weight.csv')
height = df['Height(Inches)'].tolist()
mean = st.mean(height)
std = st.stdev(height)
fsstd = mean-std
festd = mean+std
ssstd = mean-(2*std)
sestd = mean+(2*std)
tsstd = mean-(3*std)
testd = mean+(3*std)
fstd = []
for f in height:
    if(fsstd<= f and f <= festd):
        fstd.append(f)
fp = (len(fstd)/len(height))*100
print(fp)

sstd = []
for f in height:
    if(ssstd<= f and f<= sestd):
        sstd.append(f)
sp = (len(sstd)/len(height))*100
print(sp)

tstd = []
for f in height:
    if(tsstd <= f and f <= testd):
        tstd.append(f)
tp = (len(tstd)/len(height))*100
print(tp)
# graph = ff.create_distplot([height],['Average height'],show_hist=False)
# graph.show()