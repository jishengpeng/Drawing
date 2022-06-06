from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

ax = plt.axes(projection='3d')

# 三维线的数据
xline = [-0.04, 4.29, 5.35, 7.45, 8.52, 10.64, 11.70, 13.82]


yline = [-0.04, 1.69, 2.20, 2.84, 4.78, 5.67, 6.7, 8.9]

zline = [96, 97.00, 97.99, 98.09, 98.22, 98.28, 98.29, 98.31]


ax.plot3D(xline, yline, zline, 'gray')
pp = PdfPages('三维.pdf')
plt.savefig(pp, format='pdf', bbox_inches='tight')
pp.close()

plt.show()