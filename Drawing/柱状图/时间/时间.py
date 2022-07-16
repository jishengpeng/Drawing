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

def bar_plot(x_label='Sketches', y_label='Minute'):
    FONTSIZE = 22
    width = 0.2
    y = np.array([[302,568,906,2998], [1022,1392,2304,3405],
                  [2191,3480,2976,4284]])
    x_labels = ['DGA', 'DNS', 'IOT']
    legend_labels = ['Exilir','Other Models']
    x = np.arange(len(x_labels))
    x=np.arange(3)

    fig, ax = plt.subplots(figsize=(6.5,3.5))
    # ax.bar(x - 1.5*width, y[:, 0], width=width, label=legend_labels[0], color='white',
    #        ec=COLORS[1], hatch=HATCH[1] * 2, linewidth=ALLWIDTH)
    ax.bar(x - 1.5*width, y[:, 0], width=width,  color='white',label=legend_labels[0],
           ec=COLORS[1], hatch=HATCH[1] * 2, linewidth=ALLWIDTH)
    ax.bar(x -0.5*width, y[:, 1], width=width,  color='white',label=legend_labels[1],
           ec=COLORS[5], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x +0.5*width, y[:, 2], width=width, color='white',
           ec=COLORS[5], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)
    ax.bar(x + 1.5*width, y[:, 3], width=width,  color='white',
           ec=COLORS[5], hatch=HATCH[2] * 4, linewidth=ALLWIDTH)

    ax.set_xticks(x)
    ax.set_xticklabels(x_labels,fontsize = 'small',rotation = 30)
    # ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.ylim(0,5000)
    y_major_locator = MultipleLocator(1000)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE - 5)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    fig.legend(fontsize=FONTSIZE - 8, loc='upper left', ncol=4,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.18, 0.9))
    plt.tight_layout()

    # plt.rc('font', family='SimHei', size=12)

    pp = PdfPages('时间对比.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    # plt.savefig('DNS多指标对比.jpg', dpi=300)
    plt.show()

if __name__=='__main__':
    bar_plot()
