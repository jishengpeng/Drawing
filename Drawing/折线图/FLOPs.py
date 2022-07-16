import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator,FormatStrFormatter
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
Marker = ['o', 'v', '8', 's', 'p', '^', '<', '>', '*', 'h', 'H', 'D', 'd', 'P', 'X','$\u266B$']
HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
Line_Style = ['-', '--', '-.', ':']
COLORS = sns.color_palette("Paired")
rcParams.update(config)

def bar_plot(x_label='Flops(M)', y_label='Accuracy(%)'):
    FONTSIZE = 22
    width = 0.2



    fig, ax = plt.subplots(figsize=(6.5,3.5))

    x_DGA = [-0.4,4.29*2, 5.35*2, 8.52*2,11.70*2,13.82*2]
    x_IOT=[-0.4,2.231712*2,2*7.000992]
    x_ISCX=[-0.4,4.0352 * 2, 6.4448 * 2, 8.40 * 2,  11.8432 * 2, 13.5648 * 2,  17.0144 * 2, 18.944 * 2]
    x_UNSW=[-0.4,1.3854 * 2,  4.5534 * 2]
    x_UNIBS=[-0.5,4.288 * 2, 6.4064 * 2]
    x_DNS=[-0.4,0.189*2]

    y_DGA = [92,97.00,97.99,98.22,98.29,98.31 ]
    y_IOT=[92,99.99234,99.993442]
    y_ISCX=[92,93.6754, 93.8119, 93.8326,  93.9057, 93.9457, 93.9870, 94.0036]
    y_UNSW=[92,97.2067,  97.6643]
    y_UNIBS=[92,95.3111, 95.3701]
    y_DNS = [93, 100]

    plt.plot(x_DGA, y_DGA, "blue", marker= '*', linestyle=':', linewidth=1, markersize=10, label="DGA")
    plt.plot(x_IOT, y_IOT, "green", marker='<', linestyle=':', linewidth=1, markersize=10, label="IOT")
    plt.plot(x_ISCX, y_ISCX, "red", marker='^', linestyle=':', linewidth=1, markersize=10, label="ISCX")
    plt.plot(x_UNSW, y_UNSW, "orange", marker='p', linestyle=':', linewidth=1, markersize=10, label="UNSW")
    plt.plot(x_UNIBS, y_UNIBS, "black", marker='8', linestyle=':', linewidth=1, markersize=10, label="UNIBS")
    plt.plot(x_DNS, y_DNS, "pink", marker='h', linestyle=':', linewidth=1, markersize=10, label="DNS")


    #坐标标签
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    ax.set_xlabel(x_label, fontsize=FONTSIZE)
    #横纵坐标刻度
    plt.xlim(0, 40)
    plt.ylim(92, 103)
    #变化范围
    y_major_locator = MultipleLocator(3)
    x_major_locator = MultipleLocator(5)
    # ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.xaxis.set_major_locator(x_major_locator)
    #先用着
    ax.tick_params(labelsize=FONTSIZE - 5)
    plt.tick_params(axis='both', which='both', length=0)
    #网格
    # ax.grid(linestyle='-', axis='y')
    ax.grid(linestyle='-', axis='x')
    #标签
    fig.legend(fontsize=FONTSIZE-11, loc='center left', ncol=6,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.17, 0.86))
    plt.tight_layout()

    pp = PdfPages('FLOPs.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()

    plt.show()

if __name__=='__main__':
    bar_plot()
