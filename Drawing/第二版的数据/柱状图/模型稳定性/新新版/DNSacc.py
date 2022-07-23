import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 11,
    "mathtext.fontset": 'stix',
    "font.serif": ['Times New Roman'],
}  #设置一些字体和大小

matplotlib.rc('pdf', fonttype=42)

ALLWIDTH = 1.5
Marker = ['o', 'v', '8', 's', 'p', '^', '<', '>', '*', 'h', 'H', 'D', 'd', 'P', 'X']
HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
Line_Style = ['-', '--', '-.', ':']
COLORS = sns.color_palette("Paired")
rcParams.update(config)

def bar_plot(x_label='Sketches', y_label='Accuracy(%)'):
    FONTSIZE = 18
    width = 0.12

    y = np.array([[97.72,100],[0,99.99],[0,99.93]])
    x_labels = ['Loong','LSTM','BCNN']
    legend_labels = ["Anomaly Detection","DNS Tunnel Detection"]
    x = np.arange(len(x_labels))
    x = np.array([0, 0.5, 1])


    fig, ax = plt.subplots(figsize=(3.8,2.2))
    # fig, ax = plt.subplots()

    ax.bar(x -0.5*width, y[:, 0], width=width,  color='white',
           ec=COLORS[6], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x +0.5*width, y[:, 1], width=width, color='white',
           ec=COLORS[3], hatch=HATCH[5] * 2, linewidth=ALLWIDTH)


    # plt.axhline(y=94.60, color='black', linestyle=':', lw=1.5)
    #
    # ax.annotate('94.6',xy=(-0.9, 94.60))






    ax.set_xticks(x)
    ax.set_xticklabels(x_labels,fontsize = FONTSIZE)
    # ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.ylim(70, 105)
    # y_major_locator = MultipleLocator(10)
    plt.yticks([70,80,90,100])
    ax = plt.gca()
    # ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE )
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    # fig.legend(fontsize=FONTSIZE - 13, ncol=4,
    #            handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.15, 1.05))
    # plt.legend(ncol=2,bbox_to_anchor=(0.9, 1.4),fontsize=12)
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('genacc_DNS.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    # plt.savefig('DNS多指标对比.jpg', dpi=300)
    plt.show()

if __name__=='__main__':
    bar_plot()
