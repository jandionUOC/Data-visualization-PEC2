import pandas as pd
import seaborn as sns
import ptitprince as pt
import matplotlib.pyplot as plt

sns.set(style="whitegrid", font_scale=2)
df = pd.read_csv("Placement_Data_Full_Class.csv")

grouped_data = df.groupby('hsc_s')['degree_p'].sum()
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%')
plt.title('Pie plot')
plt.savefig("Pie plot.jpg")

f, ax = plt.subplots(figsize = (15, 15))
ax = pt.half_violinplot(x="hsc_s", y="degree_p", data=df, palette="Set2", bw=0.2, cut=0.,
                        scale="area", width=.6, inner=None)
ax = sns.stripplot(x="hsc_s", y="degree_p", data=df, palette="Set2", edgecolor="white", size=3, jitter=1, zorder=0)
ax = sns.boxplot(x="hsc_s", y="degree_p", data=df, color="black", width=.15, zorder=10,
                 showcaps=True, boxprops={'facecolor': 'none', "zorder": 10},
                 showfliers=True, whiskerprops={'linewidth': 2, "zorder": 10}, saturation=1)
plt.xlabel('Secondary education')
plt.ylabel('Score')
plt.title("Raincloud plot")
plt.savefig("Raincloud plot.jpg")
