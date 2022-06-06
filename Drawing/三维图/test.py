import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits import mplot3d
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

def bar_plot(x_label='Latency(ms)', y_label='Metrics(%)',z_label="Flops(M)"):
    FONTSIZE = 22
    width = 0.2



    fig, ax = plt.subplots(figsize=(6.5,3.5))

    x_DGA = [-0.04,4.29, 5.35, 7.45,8.52,10.64,11.70,13.82]
    x_IOT=[-0.04,1.69,2.20,2.84,4.78]
    x_ISCX=[-0.1,1.92, 2.51, 3.11, 3.95]
    x_UNSW=[-0.04,0.51, 0.94, 1.49, 1.80, 4.51]
    x_UNIBS=[-0.04,0.616, 0.975, 1.594, 2.204]

    y_DGA=[-0.04,1.69,2.20,2.84,4.78,5.67,6.7,8.9]

    z_DGA = [96,97.00,97.99,98.09,98.22,98.28,98.29,98.31 ]
    y_IOT=[93,99.9928,99.9935,99.9943,99.9948]
    y_ISCX=[93,93.67, 93.82, 93.85, 93.93]
    y_UNSW=[93,97.22, 97.58, 97.60, 97.64, 97.67]
    y_UNIBS=[93,94.79, 95.28,95.33,  95.3645]

    # ax.plot3D(x_DGA, y_DGA, z_DGA,"blue", marker= '*', linestyle=':', linewidth=1, markersize=10, label="DGA")
    # plt.plot(x_IOT, y_IOT, "green", marker='<', linestyle=':', linewidth=1, markersize=10, label="IOT")
    # plt.plot(x_ISCX, y_ISCX, "red", marker='^', linestyle=':', linewidth=1, markersize=10, label="ISCX")
    # plt.plot(x_UNSW, y_UNSW, "orange", marker='p', linestyle=':', linewidth=1, markersize=10, label="UNSW")
    # plt.plot(x_UNIBS, y_UNIBS, "black", marker='8', linestyle=':', linewidth=1, markersize=10, label="UNIBS")


    #坐标标签
    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    ax.set_xlabel(x_label, fontsize=FONTSIZE)
    ax.set_zlabel(z_label, fontsize=FONTSIZE)
    #横纵坐标刻度
    # plt.xlim(0, 15)
    # plt.zlim(96, 103)
    #变化范围
    # y_major_locator = MultipleLocator(3)
    # x_major_locator = MultipleLocator(3)
    # # ax = plt.gca()
    # ax.yaxis.set_major_locator(y_major_locator)
    # ax.xaxis.set_major_locator(x_major_locator)
    #先用着
    ax.tick_params(labelsize=FONTSIZE - 5)
    plt.tick_params(axis='both', which='both', length=0)
    #网格
    # ax.grid(linestyle='-', axis='y')
    # ax.grid(linestyle='-', axis='x')
    #标签
    fig.legend(fontsize=FONTSIZE-10, loc='center left', ncol=5,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.2, 0.86))
    plt.tight_layout()

    pp = PdfPages('三维.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()

    plt.show()

if __name__=='__main__':
    bar_plot()
