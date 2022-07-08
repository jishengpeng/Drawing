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
    y = np.array([[55.84,68.33,70.91,	98.57], [99.17,99.94,99.72,	100.00],
                  [99.30,98.79,99.27,99.99],[91.53,79.152,92.62,93.97],[94.68,89.01,94.95,95.36],[97.61,97.53,97.03,97.71]])
    # x_labels = ['DGA', 'LA_Mul07', 'CNN+LSTM','Elixir']
    # legend_labels = ['Accuracy', 'Precision', 'Recall','F1-score']
    x_labels = ['DGA Family', 'DNS Tunnel', 'IOT Attack','Traffic Service','Anomaly','Traffic Application']
    legend_labels = ['RNN','DNN','CNN', 'Loong']
    x = np.arange(len(x_labels))

    fig, ax = plt.subplots(figsize=(6.5,3.5))
    #画几个颜色的柱状图
    ax.bar(x - 1.5*width, y[:, 0], width=width, label=legend_labels[0], color='white',
           ec=COLORS[1], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x-0.5*width, y[:, 1], width=width, label=legend_labels[1], color='white',
           ec=COLORS[5], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x+0.5*width, y[:, 2], width=width, label=legend_labels[2], color='white',
           ec=COLORS[3], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x + 1.5*width, y[:, 3], width=width, label=legend_labels[3], color='white',
           ec=COLORS[7], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)


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
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.19, 0.95))
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('模型稳定性.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    # plt.savefig('DNS多指标对比.jpg', dpi=300)
    plt.show()

if __name__=='__main__':
    bar_plot()
