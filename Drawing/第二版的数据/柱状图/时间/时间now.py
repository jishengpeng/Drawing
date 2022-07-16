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
FONTSIZE = 18
ALLWIDTH = 1.5
Marker = ['o', 'v', '8', 's', 'p', '^', '<', '>', '*', 'h', 'H', 'D', 'd', 'P', 'X']
HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
Line_Style = ['-', '--', '-.', ':']
COLORS = sns.color_palette("Paired")
rcParams.update(config)


def bar1_plot():
    width = 0.25


    DGA = np.array([[306/60, 0], [55/60, 55*17/60], [31/60, 31*17/60],[42/60, 42*17/60]])
    DGAlabel = ["Loong", "BiLSTM", "LA_Mul07", "CLSTM"]
    DNS = np.array([[1340/60,0],[ 116/60,166*11/60],[ 128/60,128*26/60],[ 95/60,95*26/60]])
    DNSlabel = ["Loong", "LSTM", "BCNN", "DNN1"]
    IOT=np.array([[571/60,0],[ 213/60,213*17/60],[ 124/60,124*26/60],[ 119/60,119*17/60]])
    IOTlabel = ["Loong", "DNN2", "CNN", "RNN"]
    ISCX = np.array([[769/60,0],[ 42/60,42*26/60],[ 107/60,107*35/60],[ 75/60,75*35/60]])
    ISCXlabel = ['Loong', 'DeepPacket', 'AppNet', 'BGRUA']
    UNIBS = np.array([[456/60,0],[ 124/60,124*15/60],[ 107/60,107*35/60],[ 274/60,274*17/60]])
    UNIBSlabel = ['Loong', 'FSNet', 'AppNet', 'CRNN']
    UNSW = np.array([[266/60,0],[ 38/60,38*26/60],[ 31/60,31*26/60],[ 45/60,45*17/60]])
    UNSWlabel = ['Loong', 'DeepLSTM', 'FFDNN', 'LuNet']


    y=UNSW
    x_labels=UNSWlabel
    # x_labels = ['None/DT', 'RF/DT', 'GBDT/DT', 'GRU/DT', 'LSTM/DT', 'MLP/DT']
    legend_labels = ['Train', 'Design','Train+Design']
    x = np.arange(len(x_labels))
    print(x)

    fig, ax = plt.subplots(figsize=(6.5, 3.5))
    ax.bar(x[0], y[0, 0] , width=width, color='white',label=legend_labels[2],
           ec=COLORS[1], hatch=HATCH[2] * 2, linewidth=ALLWIDTH)
    ax.bar(x[1:] - 0.5 * width, y[1:, 0] , width=width, label=legend_labels[0], color='white',
           ec=COLORS[5], hatch=HATCH[4] * 4, linewidth=ALLWIDTH)
    ax.bar(x[1:] + 0.5 * width, y[1:, 1] , width=width, label=legend_labels[1], color='white',
           ec=COLORS[3], hatch=HATCH[5] * 4, linewidth=ALLWIDTH)

    # for xx, yy in zip(x, y):
    #     plt.text(xx - width, yy[0], '%.2f' % (yy[0]), ha='center', va='bottom')
    #     plt.text(xx, yy[1] + 0.01, '%.2f' % (yy[1]), ha='center', va='bottom')
    #     plt.text(xx + width, yy[2] + 0.01, '%.2f' % (yy[2]), ha='center', va='bottom')

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)
    # ax.set_xlabel('Flow Size Prediction', fontsize=FONTSIZE)
    ax.set_ylabel('Time(h)', fontsize=FONTSIZE)
    plt.ylim(0, 1200/60)
    # plt.xticks(rotation=30)
    y_major_locator = MultipleLocator(5)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE - 4)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    # ax.ticklabel_format(style='sci', scilimits=(0, 1), axis='y', useMathText=True)
    fig.legend(fontsize=FONTSIZE-3 , loc='upper left', ncol=3,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.14, 0.94))
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('时间UNSW.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

if __name__=="__main__":
    bar1_plot()