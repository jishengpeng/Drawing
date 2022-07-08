import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.backends.backend_pdf import PdfPages



def main():
    x_DGA = [1.5631,2.2473,3.0784,3.6431]
    x_IOT=[0.960,1.992,3.555]
    x_ISCX=[1.384, 1.873, 2.196, 3.177, 4.166]
    x_UNSW=[0.995, 1.958, 2.357, 2.755, 3.007]
    x_UNIBS=[1.448, 1.869, 2.760, 3.546]
    x_DNS=[-0.04,1.235]

    y_DGA = [94.312,96.475,97.831,97.896]
    y_IOT=[99.993,99.995,99.997]
    y_ISCX=[93.529, 93.818, 93.889, 93.965,  94.003]
    y_UNSW=[97.123, 97.414, 97.511, 97.611, 97.652]
    y_UNIBS=[95.246, 95.295, 95.307, 95.316]
    y_DNS=[95,100]


    plt.rcParams["font.family"]="SimHei"

    fig=plt.figure(figsize=(6.5,3.5))

    ax=fig.add_subplot(2,3,1)
    plt.title("DGA Family")
    ax.plot(x_DGA, y_DGA, "blue", marker= '*', linestyle=':', linewidth=1, markersize=5, label="DGA")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 5)
    plt.ylim(93.00, 99.00)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    ax=fig.add_subplot(2,3,2)
    plt.title("Traffic Service")
    ax.plot(x_ISCX, y_ISCX, "red", marker='^', linestyle=':', linewidth=1, markersize=5, label="ISCX")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 5)
    plt.ylim(93.4, 94.1)

    ax=fig.add_subplot(2,3,3)
    plt.title("IOT Attack" )
    ax.plot(x_IOT, y_IOT, "green", marker='<', linestyle=':', linewidth=1, markersize=5, label="IOT")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 5)
    plt.ylim(99.989, 99.999)
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    ax=fig.add_subplot(2,3,4)
    plt.title("Anomaly")
    plt.plot(x_UNSW, y_UNSW, "orange", marker='p', linestyle=':', linewidth=1, markersize=5, label="UNSW")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 5)
    plt.ylim(97.0, 98)

    ax=fig.add_subplot(2,3,5)
    plt.title("Traffic Application")
    ax.plot(x_UNIBS, y_UNIBS, "black", marker='8', linestyle=':', linewidth=1, markersize=5, label="UNIBS")
    ax.set_ylabel("Accuracy(%)")
    ax.set_xlabel("Latency(ms)", fontsize=20)
    plt.xlim(0.0, 5)
    plt.ylim(95.20, 95.40)

    ax=fig.add_subplot(2,3,6)
    plt.title("DNS Tunnel")
    ax.plot(x_DNS, y_DNS, "pink", marker='h', linestyle=':', linewidth=1, markersize=5, label="DNS")
    ax.set_ylabel("Accuracy(%)")
    plt.xlim(0.0, 5)
    plt.ylim(95, 105)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    # plt.suptitle("Latency",fontsize=40)

    plt.tight_layout(rect=[0,0,1,1])

    pp = PdfPages('延迟六图版.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

if __name__=="__main__":
    main()