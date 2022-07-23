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
FONTSIZE = 29
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

    y = np.array([[91.72, 91.81, 91.71, 91.68], [93.61, 93.57, 93.60, 93.52],
                  [93.71, 93.66, 93.69, 93.61], [94.04, 94.05, 94.04, 93.97]])
    x_labels = ['DeepPacket', 'AppNet', 'BGRUA', 'Loong']

    # UNSW:

    # y = np.array([[97.55, 97.49, 97.56, 97.50], [97.58, 97.50, 97.57, 97.51],
    #               [97.38, 97.47, 97.39, 97.41], [97.72, 97.52, 97.72, 97.59]])
    # x_labels = ['DeepLSTM', 'FFDNN', 'LuNet', 'Loong']

    # UNIBS:
    '''
    y = np.array([[95.35, 95.77, 95.34, 95.41], [95.36, 95.78, 95.36, 95.43],
                  [95.29, 95.72, 95.28, 95.36], [95.35, 95.77, 95.35, 95.42]])
    x_labels = ['FSNet', 'AppNet', 'CRNN', 'Loong']
    '''
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
    plt.ylim(91, 94.5)  # ISCX: (91, 95) # UNSW: (97.2, 97.85) # UNIBS: (90, 98)
    y_major_locator = MultipleLocator(1)  # ISCX: (1) # UNSW: (0.15) # UNIBS: (2)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    # fig.legend(fontsize=FONTSIZE - 9.5, loc='upper left', ncol=4,
    #            handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True,
    #            bbox_to_anchor=(0.185, 0.95))
    # ISCX: (0.16, 0.91) # UNSW: (0.185, 0.95) # UNIBS: (0.17, 0.91)
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('ISCX_bar.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()


bar6_plot()