import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams
import matplotlib.ticker as mtick
import pandas as pd
import pickle
import itertools

config = {
    "font.family": 'serif',
    "font.size": 11,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}

matplotlib.rc('pdf', fonttype=42)

ALLWIDTH = 1.5
Marker = ['o', 'v', '8', 's', 'p', '^', '<', '>', '*', 'h', 'H', 'D', 'd', 'P', 'X']
HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
Line_Style = ['-', '--', '-.', ':']
COLORS = sns.color_palette("Paired")
rcParams.update(config)


def bar6_plot(x_label='', y_label='Metrics(%)'):
    FONTSIZE = 18
    width = 0.2
    # ISCX:



    y = np.array([[95.35, 95.77, 95.34, 95.41], [95.36, 95.78, 95.36, 95.43],
                  [95.29, 95.72, 95.28, 95.36], [95.35, 95.77, 95.35, 95.42]])
    x_labels = ['FSNet', 'AppNet', 'CRNN', 'Loong']

    labels = ['Accuracy', 'Precision', 'Recall', 'F1-score']

    x = np.arange(len(x_labels))

    fig, ax = plt.subplots(figsize=(6, 2.8))
    ax.bar(x - 1.5 * width, y[:, 0], width=width, label=labels[0], color='white',
           ec=COLORS[1], hatch=HATCH[1] * 2, linewidth=ALLWIDTH)
    ax.bar(x - 0.5 * width, y[:, 1], width=width, label=labels[1], color='white',
           ec=COLORS[5], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x + 0.5 * width, y[:, 2], width=width, label=labels[2], color='white',
           ec=COLORS[3], hatch=HATCH[5] * 2, linewidth=ALLWIDTH)
    ax.bar(x + 1.5 * width, y[:, 3], width=width, label=labels[3], color='white',
           ec=COLORS[9], hatch=HATCH[4] * 4, linewidth=ALLWIDTH)

    # for xx, yy in zip(x, y):
    #     plt.text(xx - 0.5 * width, yy[0] + 0.1, '%.2f' % yy[0], ha='center', va='bottom')
    #     plt.text(xx + 0.5 * width, yy[1] + 0.1, '%.2f' % yy[1], ha='center', va='bottom')

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize='small', rotation=0)
    ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.ylim(90,97)  # ISCX: (91, 95) # UNSW: (97.2, 97.85) # UNIBS: (90, 98)
    y_major_locator = MultipleLocator(2)  # ISCX: (1) # UNSW: (0.15) # UNIBS: (2)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('UNIBS_bar.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()


bar6_plot()