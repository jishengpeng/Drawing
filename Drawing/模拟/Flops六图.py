import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.backends.backend_pdf import PdfPages



def main():
    x_DGA = [ 4.29 * 2, 5.35 * 2, 8.52 * 2, 11.70 * 2, 13.82 * 2]
    x_IOT = [2.231712 * 2, 2 * 7.000992]
    x_ISCX = [4.0352 * 2, 6.4448 * 2, 8.40 * 2, 11.8432 * 2, 13.5648 * 2, 17.0144 * 2, 18.944 * 2]
    x_UNSW = [1.3854 * 2, 4.5534 * 2]
    x_UNIBS = [ 4.288 * 2, 6.4064 * 2]
    x_DNS = [0.189 * 2]

    y_DGA = [ 97.00, 97.99, 98.22, 98.29, 98.31]
    y_IOT = [ 99.99234, 99.993442]
    y_ISCX = [93.6754, 93.8119, 93.8326, 93.9057, 93.9457, 93.9870, 94.0036]
    y_UNSW = [ 97.2067, 97.6643]
    y_UNIBS = [ 95.3111, 95.3701]
    y_DNS = [ 100]


    plt.rcParams["font.family"]="SimHei"

    fig=plt.figure(figsize=(6.5,3.5))

    ax=fig.add_subplot(2,3,1)
    plt.title("DGA")
    ax.plot(x_DGA, y_DGA, "blue", marker= '*', linestyle=':', linewidth=1, markersize=5, label="DGA")
    plt.xlim(0.0, 40)
    plt.ylim(96.50, 99.00)
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    plt.subplot(2,3,2)
    plt.title("ISCX")
    plt.plot(x_ISCX, y_ISCX, "red", marker='^', linestyle=':', linewidth=1, markersize=5, label="ISCX")
    plt.xlim(0.0, 40)
    plt.ylim(93.5, 94.5)

    ax=fig.add_subplot(2,3,3)
    plt.title("IOT")
    ax.plot(x_IOT, y_IOT, "green", marker='<', linestyle=':', linewidth=1, markersize=5, label="IOT")
    plt.xlim(0.0, 20)
    plt.ylim(99.99, 99.996)
    # ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

    plt.subplot(2,3,4)
    plt.title("UNSW")
    plt.plot(x_UNSW, y_UNSW, "orange", marker='p', linestyle=':', linewidth=1, markersize=5, label="UNSW")
    plt.xlim(0.0, 20)
    plt.ylim(97.0, 98)

    ax=fig.add_subplot(2,3,5)
    plt.title("UNIBS")
    ax.plot(x_UNIBS, y_UNIBS, "black", marker='8', linestyle=':', linewidth=1, markersize=5, label="UNIBS")
    plt.xlim(0.0, 20)
    plt.ylim(94.50, 95.50)

    ax=fig.add_subplot(2,3,6)
    plt.title("DNS")
    ax.plot(x_DNS, y_DNS, "pink", marker='h', linestyle=':', linewidth=1, markersize=5, label="DNS")
    plt.xlim(0.0, 1)
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