
# coding: utf-8

# In[13]:

# Making a horizontal histogram using str() x vector label values
# Note : we can't use np.array for this as it returns only NaN values. As general, np.array is not recommended for handling str()
# better re-import data as dataframe, and retrieve the tickers in a variable properly
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.genfromtxt('D:/work/github1.txt', delimiter="\t", skip_header=1)
patents = np.array(data[:,1], int)
years = np.array(data[:,0], str)

data2 = pd.read_table('D:/work/github1.txt', delimiter="\t")
tickersx_str = data2['x'].values

freq_series = pd.Series.from_array(patents)

# now to plot the figure... we have to use plt.figure method because we have 2 information years and patents
# this goes through plt.figure method and ax. method (this is no longer a simple plot but a 2-axis-information plot)
plt.figure(figsize=(8, 4)) # adjusting graph size / proportions
ax = freq_series.plot(kind='bar', label='Volume', color='lightblue')
ax.set_title("title", fontweight='bold', size=15)
ax.set_xlabel("y label", size = 13)
ax.set_ylabel('x label', size = 13)
ax.set_xticklabels(tickersx_str) # tickles for X axis
ax.grid(False) #no grid
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

rects = ax.patches

# Rotating the xticklabels for years
for label in ax.get_xmajorticklabels():
    label.set_rotation(45)
    label.set_horizontalalignment("right")

# Making the labels
def autolabel(rects, ax):
    # Get y-axis height to calculate label position from. 
    (y_bottom, y_top) = ax.get_ylim()
    y_height = y_top - y_bottom

    for rect in rects:
        height = rect.get_height()

        # Fraction of axis height taken up by this rectangle
        p_height = (height / y_height)

        # If we can fit the label above the column, do that;
        # otherwise, put it inside the column.
        if p_height > 0.95: # arbitrary; 95% looked good to me.
            label_position = height - (y_height * 0.1)
        else:
            label_position = height + (y_height * 0.01)

        ax.text(rect.get_x() + rect.get_width()/2., label_position,
                '%d' % int(height), ha='center', va='bottom', rotation=0, fontweight='bold')

autolabel(rects, ax)
plt.tight_layout()
plt.legend(loc='upper center')
plt.savefig("D:/work/github/horizontal_histgrm_1.png")
plt.show()


# In[14]:

# form improvement over vertical histogram
import pandas as pd
import matplotlib.pyplot as plt

# Import data
data = pd.read_table("D:\work\github2.txt", sep='\t')

# Reverse table from smallest to highest
data2 = data.sort_values(by=['y', 'x'], ascending=[True, False])
tickers = data2['x'].values

# Plot data
fig, ax = plt.subplots(figsize=(9, 9))
rects = ax.barh(range(len(tickers)), data2['y'].values, align='center', color='#4E8DC4', alpha=0.6)
ax.set_yticks(range(len(tickers)))
ax.set_yticklabels(tickers, fontweight='normal')
ax.set_xlabel('x label', size= 13)
ax.set_ylabel('y label', size = 13)
ax.set_title('title', fontweight='bold', size=15)
ax.set_ylim((-1, len(tickers))) # allows to auto-size Y axis depending of [-1:N] bars
ax.grid(False) #no grid
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Rotating the xticklabels for patents volume
for label in ax.get_xmajorticklabels():
    label.set_rotation(30)
    label.set_verticalalignment("top")

# Add label to the right of the bars
for i, rect in enumerate(rects):
    # Get width of the bar
    xloc = int(rect.get_width()) - 0.1 #x-dimension label position (the highest, the farthest)
    # Center the text vertically in the bar
    yloc = rect.get_y() + rect.get_height()/2.0 #y-dimension label position
    label = ax.text(
        xloc, yloc,
        data2['y'].values[i],
        horizontalalignment='right',
        verticalalignment='center',
        color='k',
        clip_on=True, fontweight='bold')

plt.tight_layout() # allows to autosize-labels & tickers to fit diagram
plt.savefig("D:/work/github/horizontal_histgrm_2.png")
plt.show()


# In[ ]:



