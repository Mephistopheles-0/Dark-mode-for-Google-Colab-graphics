# -*- coding: utf-8 -*-

#                   -------by--Mephistopheles-------


# This code will allow you to switch your graphics to dark mode
import matplotlib.pyplot as plt

import matplotlib as mpl
from matplotlib import cycler
colors = cycler('color',
                  ['#669FEE','#66EE91','#9988DD',
                   '#EECC55','#88BB44','#FFBBBB'])
plt.rc('figure',facecolor = '#313233')
plt.rc('axes',facecolor = "#313233",edgecolor = 'none',
         axisbelow = True, grid =True, prop_cycle = colors, labelcolor = 'gray')
plt.rc('grid', color = '#474A4A', linestyle = 'solid')
plt.rc('xtick', color = 'gray')
plt.rc('ytick', direction = 'out', color = 'gray')
plt.rc('legend',facecolor = "#313233", edgecolor = "#313233")
plt.rc("text", color = "#C9C9C9")
