
# coding: utf-8

# In[2]:

# Apparition
# Bubble graph / Scatter plot from edge list
# Working version
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

#prepping the data
k = pd.read_table('D:\work\githubscatter.csv', sep=',')

#sorting out, reseting index, collecting them
df = k.groupby('y').apply(lambda d: d.sort_index()).reset_index('y',drop=True)
df.sort_index(inplace = True)
idf = df.index

#generate graph
colors = df['z']
fig = plt.figure(figsize = (18, 14))
ax = fig.add_subplot(1,1,1)
ax.scatter(df['y'], idf, s = df['z'] * 500, c = colors, cmap=plt.cm.YlOrRd)

ax.xaxis.tick_bottom() # puts xticklabels at the top of chart
ax.yaxis.tick_left() # puts yticklabels on the right side
ax.set_xlabel('x label', size=15, fontweight='bold')
ax.set_ylabel('y label', size=15, fontweight='bold')
ax.patch.set_facecolor('lightblue') # background
ax.patch.set_alpha(0.1) # background transparency

#looping bubble label information through index for 3 variables, applying form
for i, txt in enumerate(df['z']):
    if df['z'][i] != 0:
        ax.annotate(txt, (df['y'][i], idf[i]), 
                        fontsize=15, fontweight='bold', horizontalalignment='center', verticalalignment='center')

yt = list(df['x'])
#prepping axis with list of string through range[i]
plt.yticks(range(len(df['z'])), yt, fontsize = 10)
plt.xticks(rotation=30, fontsize = 20)


#design parameters
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.title('title', y = 1, fontsize = 30, fontweight = "bold") # title + offset
plt.axis('tight') # eliminats blanks and empty spaces at axis periphery
plt.grid(False) # grid or not
plt.tight_layout() #auto-size window to chart frame

plt.savefig("D:/work/githubscatter.png")

plt.show()


# In[ ]:



