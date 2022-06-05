import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib.backends.backend_pdf import PdfPages

x_DGA = [1.01, 1.45, 2.48, 3.27, 3.62, 4.43]
# x_UNSW = [1, 1.5, 2, 2.5, 3, 3.5]
# x_UNIBS = [1, 2, 2.5, 3, 4, 4.4]

y_DGA = [97.09, 98.10, 98.11, 98.18, 98.19, 98.20]
# y_UNSW = [97.3, 97.5, 97.6, 97.9, 96.9, 97.0]
# y_UNIBS = [96.3, 96.4, 96.5, 96.6, 96.7, 96.8]

plt.plot(x_DGA, y_DGA, "red", marker='*', linestyle=':', linewidth=1, markersize=13, label="DGA")
# plt.plot(x_UNSW, y_UNSW, "blue", marker='.', linestyle='-', linewidth=2, markersize=10, label="UNSW")
# plt.plot(x_UNIBS, y_UNIBS, "green", marker='.', linestyle='-', linewidth=2, markersize=10, label="UNIBS")

plt.xlabel("latency(ms)")
plt.ylabel("acc")
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(0.3))
plt.xlim(1.0, 4.5)
plt.ylim(97, 98.5)
plt.title("")
plt.legend(loc="best")
plt.show()
pp = PdfPages('latency.pdf')
plt.savefig(pp, format='pdf', bbox_inches='tight')
pp.close()

