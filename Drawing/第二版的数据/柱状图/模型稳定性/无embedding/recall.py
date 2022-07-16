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

def bar_plot(x_label='Sketches', y_label='Accuracy(%)'):
    FONTSIZE = 22
    width = 0.2
    y = np.array([[95.49,94.69,	97.94], [99.99,99.93,	100.00],
                  [0,0,99.99],[93.24,92.62,94.04],[0,0,97.72],[95.26,95.95,95.35]])
    # x_labels = ['DGA', 'LA_Mul07', 'CNN+LSTM','Elixir']
    # legend_labels = ['Accuracy', 'Precision', 'Recall','F1-score']
    x_labels = ['DGA Family', 'DNS Tunnel', 'IoT Attack','Traffic Service','Anomaly','Traffic Application']
    legend_labels = ['LSTM','BCNN', 'Loong']
    x = np.arange(len(x_labels))
    print(x)

    fig, ax = plt.subplots(figsize=(6.5,3.5))
    #画几个颜色的柱状图
    ax.bar(x - 1*width, y[:, 0], width=width, label=legend_labels[0], color='white',
           ec=COLORS[1], hatch=HATCH[1] * 2, linewidth=ALLWIDTH)
    ax.bar(x+0*width, y[:, 1], width=width, label=legend_labels[1], color='white',
           ec=COLORS[3], hatch=HATCH[5] * 2, linewidth=ALLWIDTH)
    ax.bar(x + 1*width, y[:, 2], width=width, label=legend_labels[2], color='white',
           ec=COLORS[9], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)



    ax.bar(2, 80, width=width,  color='white',
           ec=COLORS[9], hatch=HATCH[2] * 0, linewidth=ALLWIDTH)
    ax.bar(2-width, 80, width=width, color='white',
           ec=COLORS[9], hatch=HATCH[2] * 0, linewidth=ALLWIDTH)
    ax.bar(4-width, 80, width=width, color='white',
           ec=COLORS[9], hatch=HATCH[2] * 0, linewidth=ALLWIDTH)
    ax.bar(4, 80, width=width, color='white',
           ec=COLORS[9], hatch=HATCH[2] * 0, linewidth=ALLWIDTH)

    ax.plot([1.7,2.1], [0,80], "purple",  linestyle='-', linewidth=1)
    ax.plot([1.9,2.3], [80, 0], "purple", linestyle='-', linewidth=1)
    ax.plot([1.7, 2.1], [80, 0], "purple", linestyle='-', linewidth=1)
    ax.plot([1.5, 1.9], [0, 80], "purple", linestyle='-', linewidth=1)

    ax.plot([3.7, 4.1], [0, 80], "purple", linestyle='-', linewidth=1)
    ax.plot([3.9, 4.3], [80, 0], "purple", linestyle='-', linewidth=1)
    ax.plot([3.7, 4.1], [80, 0], "purple", linestyle='-', linewidth=1)
    ax.plot([3.5, 3.9], [0, 80], "purple", linestyle='-', linewidth=1)


    ax.set_xticks(x)
    ax.set_xticklabels(x_labels,fontsize = 2,rotation = 30)
    # ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.ylim(40, 120)
    y_major_locator = MultipleLocator(20)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE - 7)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    fig.legend(fontsize=FONTSIZE - 6, loc='upper left', ncol=4,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.25, 0.95))
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('稳定性无embedding召回率.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    # plt.savefig('DNS多指标对比.jpg', dpi=300)
    plt.show()

if __name__=='__main__':
    bar_plot()
