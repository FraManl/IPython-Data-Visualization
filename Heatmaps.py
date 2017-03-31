
# coding: utf-8

# In[3]:

# Example of a heatmap simulating temporal dynamic of patents with color gradients
# improvements in design and form (colorbar, colors, police size and positions, titles, textlabels, tickers, fig size)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Generate a random number, you can refer your data values also
data = pd.read_table('D:/work/matrix2.txt', sep='\t', index_col=0)
rows = list(data.index) #rows categories
columns = list(data.columns) #column categories

fig,ax = plt.subplots(figsize=(20, 12)) # adjust chart size (x,y)

#Advance color controls
heatmap_bar = ax.pcolor(data, cmap=plt.cm.Blues, edgecolors='k') # stock the .pcolor graph into heatmap variable
heatmap_bar2 = ax.pcolor(data, cmap=plt.cm.Blues, edgecolors='k')

ax.pcolor(data, cmap=plt.cm.Blues) # adds gradient and intensity color. edgecolors='k' this argument adds grids for boxes, can remove
ax.set_xticks(np.arange(len(columns))+0.5) # puts the xticklabel into position (the lower the bottomer)
ax.set_yticks(np.arange(len(rows))+0.5) # puts the yticklabel into position (the lower the bottomer)
ax.set_xlabel('Years', size=25)
ax.set_ylabel('Y label', size=25)
ax.xaxis.tick_top() # puts xticklabels at the top of chart
ax.yaxis.tick_left() # puts yticklabels on the right side

#Values against each labels, draws the labels
ax.set_xticklabels(columns, minor=False, fontsize=14)
ax.set_yticklabels(rows, minor=False, fontsize=13)

# we display matrix data for each x datashape[0] and each y data.shape[1], as text labels into the heatmap squares
for y in range(data.shape[0]): # looping through rows
    for x in range(data.shape[1]): #looping through columns
        if data.iloc[y, x] != 0: # displaying only data that are != 0, display label position, modulo data.x,y position (remember its panda dataframe, so iloc)
            plt.text(x + 0.5, y + 0.5, '%.0f' % data.iloc[y, x], horizontalalignment='center',verticalalignment='center')

plt.colorbar(heatmap_bar, orientation='horizontal', shrink=0.7, pad = 0.08) # draw the colorbar and adjust its position, its size
plt.colorbar(heatmap_bar2, orientation='vertical', shrink=1, pad = 0.05)
plt.xticks(rotation=45) # rotate xticks labels
plt.title('title', y=1.08, fontsize = 30, fontweight="bold") # title + offset
plt.axis('tight') # eliminats blanks and empty spaces at axis periphery
plt.grid(False) # supposed to handle grid
plt.tight_layout() # ensure window autosizing

plt.savefig("D:/work/github/heatmaps1.png")

plt.show()


# In[ ]:



