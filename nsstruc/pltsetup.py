#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

#plt.rcParams['axes.color_cycle'] = ['black', 'limegreen', 'darkgrey', 'orange', 'cyan', 'hotpink', 'blue', 'darkred']
plt.rcParams['axes.labelsize'] = 28
plt.rcParams['figure.figsize'] = 10, 10
AUTO_COLORS = ['black', 'limegreen', 'darkgrey', 'orange', 'cyan', 'hotpink', 'blue', 'darkred']  #plt.rcParams['axes.color_cycle']
AUTO_MARKERS = ['.', '+', 'x', 'd', '1']
AUTO_LINESTYLES = ['-', '--', ':', '-.']
