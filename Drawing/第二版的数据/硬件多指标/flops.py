import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.backends.backend_pdf import PdfPages

# flops：(没改变，和上次发的一样)
# Traffic Service(ISCX):
# [93.530, 93.767, 93.835, 93.883, 93.867, 93.878, 93.925, 93.949, 93.993, 93.938]
# [5.049, 6.822, 8.525, 12.300, 14.086, 15.897, 19.628, 21.427, 23.148, 24.921]
# Traffic Application(UNIBS):
# [94.904, 95.226, 95.266, 95.298, 95.264, 95.265, 95.257, 95.236, 95.173, 95.165]
# [5.017, 6.707, 8.416, 16.249, 20.025, 23.769, 27.513, 29.203, 31.001, 32.736]
# Anomaly(UNSW-NB15):
# [97.120, 97.435, 97.577, 97.551, 97.548, 97.600, 97.566, 97.567, 97.496, 97.512]
# [1.250, 2.793, 4.274, 5.767, 7.248, 8.757, 10.250, 11.748, 13.235, 14.761]

def main():
    x_DGA = [ 6.6176*2,8.480*2,10.37*2,12.230*2,13.06*2,13.89*2,14.72*2]
    x_IOT = [3.451392*2,5.541120*2,6.764544*2]
    x_ISCX = [5.049*2, 6.822*2, 8.525*2, 12.300*2,  19.628*2, 21.427*2, 23.148*2]
    x_UNSW = [1.250*2, 2.793*2, 4.274*2, 8.757*2]
    x_UNIBS = [5.017*2,  8.416*2, 16.249*2]
    x_DNS = [-0.04*2,15.168 * 2]

    y_DGA = [ 95.822,97.206,97.7748,97.8613,97.8670,97.888,97.9391]
    y_IOT = [ 99.993,99.995,99.997]
    y_ISCX = [93.530, 93.767, 93.835, 93.883,  93.925, 93.949, 93.993]
    y_UNSW = [97.120, 97.435, 97.577,  97.600 ]
    y_UNIBS = [94.904,  95.266, 95.298 ]
    y_DNS = [ 95,100]


    plt.rcParams["font.family"]="SimHei"

    fig=plt.figure(figsize=(6.5,3.5))

    ax=fig.add_subplot(2,3,1)
    plt.title("DGA Family")
    ax.plot(x_DGA, y_DGA, "blue", marker= '*', linestyle=':', linewidth=1, markersize=5, label="DGA")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(10, 32)
    plt.ylim(95.50, 99)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    ax=fig.add_subplot(2,3,2)
    plt.title("Traffic Service")
    ax.plot(x_ISCX, y_ISCX, "red", marker='^', linestyle=':', linewidth=1, markersize=5, label="ISCX")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0,50)
    plt.ylim(93.20, 94.50)

    ax=fig.add_subplot(2,3,3)
    plt.title("IOT Attack")
    ax.plot(x_IOT, y_IOT, "green", marker='<', linestyle=':', linewidth=1, markersize=5, label="IOT")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 20)
    plt.ylim(99.99, 99.998)
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    ax=fig.add_subplot(2,3,4)
    plt.title("Anomaly")
    ax.plot(x_UNSW, y_UNSW, "orange", marker='p', linestyle=':', linewidth=1, markersize=5, label="UNSW")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 20)
    plt.ylim(97.0, 98)

    ax=fig.add_subplot(2,3,5)
    plt.title("Traffic Application")
    ax.plot(x_UNIBS, y_UNIBS, "black", marker='8', linestyle=':', linewidth=1, markersize=5, label="UNIBS")
    ax.set_ylabel("Accuracy(%)")
    ax.set_xlabel("Flops(M)", fontsize=20)
    plt.xlim(0.0, 40)
    plt.ylim(94.50, 95.50)

    ax=fig.add_subplot(2,3,6)
    plt.title("DNS Tunnel")
    ax.plot(x_DNS, y_DNS, "pink", marker='h', linestyle=':', linewidth=1, markersize=5, label="DNS")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 40)
    plt.ylim(95, 105)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    # plt.suptitle("Latency",fontsize=40)

    plt.tight_layout(rect=[0,0,1,1])

    pp = PdfPages('Flops六图版.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

if __name__=="__main__":
    main()