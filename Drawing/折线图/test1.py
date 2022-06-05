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
    legend_labels = ['DGA','IOT']


    fig, ax = plt.subplots(figsize=(6.5,3.5))

    x_DGA = [1.01, 1.45, 2.48, 3.27, 3.62, 4.43]
    x_IOT=[1.69,2.20,2.84,4.78]

    y_DGA = [97.09, 98.10, 98.11, 98.18, 98.19, 98.20]
    y_IOT=[99.9928,99.9935,99.9943,99.9948]

    plt.plot(x_DGA, y_DGA, "red", marker='p', linestyle=':', linewidth=1, markersize=13, label="DGA")
    plt.plot(x_IOT, y_IOT, "green", marker='$\u266B$', linestyle=':', linewidth=1, markersize=13, label="IOT")


    ax.set_ylabel(y_label, fontsize=FONTSIZE)
    # plt.yscale('log')
    plt.xlim(1.0, 5.0)
    plt.ylim(97, 101)
    y_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ax.tick_params(labelsize=FONTSIZE - 5)
    plt.tick_params(axis='both', which='both', length=0)
    ax.grid(linestyle=':', axis='y')
    fig.legend(fontsize=FONTSIZE-6, loc='lower right', ncol=1,
               handlelength=ALLWIDTH, handletextpad=0.4, columnspacing=1, frameon=True, shadow=True, bbox_to_anchor=(0.95, 0.18))
    plt.tight_layout()

    plt.show()

if __name__=='__main__':
    bar_plot()
