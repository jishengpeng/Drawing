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

def bar_plot(x_label='Sketches', y_label='Metrics(%)'):
    FONTSIZE = 22
    width = 0.2
    y = np.array([[99.35,99.34,	99.35,99.34], [99.27,	99.25	,99.26,	99.27],
                  [99.30	,99.30,99.29,	99.30],[99.99,99.99,99.99,99.99]])
    x_labels = ['BiLSTM', 'LA_Mul07', 'CNN+LSTM','Elixir']
    legend_labels = ['Accuracy', 'Precision', 'Recall','F1-score']
    x = np.arange(len(x_labels))

    fig, ax = plt.subplots(figsize=(6.5,3.5))
    ax.bar(x - 1.5*width, y[:, 0], width=width, label=legend_labels[0], color='white',
           ec=COLORS[1], hatch=HATCH[1] * 2, linewidth=ALLWIDTH)
    ax.bar(x -0.5*width, y[:, 1], width=width, label=legend_labels[1], color='white',
           ec=COLORS[5], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x +0.5*width, y[:, 2], width=width, label=legend_labels[2], color='white',
           ec=COLORS[3], hatch=HATCH[5] * 2, linewidth=ALLWIDTH)
    ax.bar(x + 1.5*width, y[:, 3], width=width, label=legend_labels[3], color='white',
           ec=COLORS[9], hatch=HATCH[4] * 4, linewidth=ALLWIDTH)

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels,fontsize = 'small',rotation = 30)
    # ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.ylim(98.80,100.80)
    y_major_locator = MultipleLocator(0.4)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE - 5)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    fig.legend(fontsize=FONTSIZE - 8, loc='upper left', ncol=4,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.18, 0.9))
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('IOT多指标.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    # plt.savefig('DNS多指标对比.jpg', dpi=300)
    plt.show()

if __name__=='__main__':
    bar_plot()
