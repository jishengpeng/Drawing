import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.backends.backend_pdf import PdfPages



def main():
    x_DGA = [1.01, 1.45, 2.48, 3.27, 3.62, 4.43]
    x_IOT=[1.69,2.20,2.84,4.78]
    x_ISCX=[1.92, 2.51, 3.11, 3.95]
    x_UNSW=[0.51, 0.94, 1.49, 1.80, 4.51]
    x_UNIBS=[0.616, 0.975, 1.594, 2.204]
    x_DNS=[-0.04,1.213]

    y_DGA = [97.09, 98.10, 98.11, 98.18, 98.19, 98.20]
    y_IOT=[99.9928,99.9935,99.9943,99.9948]
    y_ISCX=[93.67, 93.82, 93.85, 93.93]
    y_UNSW=[97.22, 97.58, 97.60, 97.64, 97.67]
    y_UNIBS=[94.79, 95.28,95.33,  95.3645]
    y_DNS=[95,100]


    plt.rcParams["font.family"]="SimHei"

    fig=plt.figure(figsize=(6.5,3.5))

    ax=fig.add_subplot(2,3,1)
    plt.title("DGA")
    ax.plot(x_DGA, y_DGA, "blue", marker= '*', linestyle=':', linewidth=1, markersize=5, label="DGA")
    plt.xlim(0.0, 5)
    plt.ylim(97.00, 99.00)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    plt.subplot(2,3,2)
    plt.title("ISCX")
    plt.plot(x_ISCX, y_ISCX, "red", marker='^', linestyle=':', linewidth=1, markersize=5, label="ISCX")
    plt.xlim(0.0, 5)
    plt.ylim(93.5, 94)

    ax=fig.add_subplot(2,3,3)
    plt.title("IOT")
    ax.plot(x_IOT, y_IOT, "green", marker='<', linestyle=':', linewidth=1, markersize=5, label="IOT")
    plt.xlim(0.0, 5)
    plt.ylim(99.99, 99.996)
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    plt.subplot(2,3,4)
    plt.title("UNSW")
    plt.plot(x_UNSW, y_UNSW, "orange", marker='p', linestyle=':', linewidth=1, markersize=5, label="UNSW")
    plt.xlim(0.0, 5)
    plt.ylim(97.0, 98)

    ax=fig.add_subplot(2,3,5)
    plt.title("UNIBS")
    ax.plot(x_UNIBS, y_UNIBS, "black", marker='8', linestyle=':', linewidth=1, markersize=5, label="UNIBS")
    plt.xlim(0.0, 5)
    plt.ylim(94.50, 95.50)

    ax=fig.add_subplot(2,3,6)
    plt.title("DNS")
    ax.plot(x_DNS, y_DNS, "pink", marker='h', linestyle=':', linewidth=1, markersize=5, label="DNS")
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