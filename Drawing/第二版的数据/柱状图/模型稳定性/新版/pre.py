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
FONTSIZE = 29
ALLWIDTH = 1.5
Marker = ['o', 'v', '8', 's', 'p', '^', '<', '>', '*', 'h', 'H', 'D', 'd', 'P', 'X']
HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
Line_Style = ['-', '--', '-.', ':']
COLORS = sns.color_palette("Paired")
rcParams.update(config)

def bar_plot(x_label='Sketches', y_label='Precision(%)'):
    FONTSIZE = 18
    width = 0.2

    y = np.array([[99.99,97.52,100,97.91], [99.25,96.46,99.83,70.91],[0 ,0,99.99,93.38],[0,0,99.93,92.35]])
    x_labels = ['Loong','CNN','LSTM','BCNN']
    legend_labels = ["IoT Attack Detection","Anomaly Detection","DNS Tunnel Detection","DGA Family Classification"]
    x = np.arange(len(x_labels))
    print(x)

    fig, ax = plt.subplots(figsize=(6.5,3.5))
    # fig, ax = plt.subplots()
    ax.bar(x - 1.5*width, y[:, 0], width=width, label=legend_labels[0], color='white',
           ec=COLORS[1], hatch=HATCH[1] * 2, linewidth=ALLWIDTH)
    ax.bar(x -0.5*width, y[:, 1], width=width, label=legend_labels[1], color='white',
           ec=COLORS[6], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x +0.5*width, y[:, 2], width=width, label=legend_labels[2], color='white',
           ec=COLORS[3], hatch=HATCH[5] * 2, linewidth=ALLWIDTH)
    ax.bar(x + 1.5*width, y[:, 3], width=width, label=legend_labels[3], color='white',
           ec=COLORS[9], hatch=HATCH[4] * 4, linewidth=ALLWIDTH)

    #画空的格子

    # x_kong=np.array([3,4])
    # y_kong=np.array([80,80])
    # ax.bar(x_kong - 0.5 * width,y_kong , width=width,  color='white',
    #        ec=COLORS[5], hatch=HATCH[3] * 0, linewidth=ALLWIDTH)
    # ax.bar(x_kong -1.5 * width, y_kong, width=width, color='white',
    #        ec=COLORS[5], hatch=HATCH[2] * 0, linewidth=ALLWIDTH)

    plt.axhline(y=94.60, color='black', linestyle=':', lw=1.5)





    ax.set_xticks(x)
    ax.set_xticklabels(x_labels,fontsize = 'small')
    # ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.ylim(70, 105)
    plt.yticks([70, 80, 90, 94.6, 100])
    # y_major_locator = MultipleLocator(10)
    ax = plt.gca()
    # ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    # fig.legend(fontsize=FONTSIZE - 13, ncol=4,
    #            handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.15, 1.05))
    plt.legend(ncol=2,bbox_to_anchor=(0.9, 1.4),fontsize=12)
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('稳定性精确率.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    # plt.savefig('DNS多指标对比.jpg', dpi=300)
    plt.show()

if __name__=='__main__':
    bar_plot()
