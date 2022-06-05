import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.YlGnBu):
    plt.rc('font', size='18')  # 设置字体样式、大小
    DNN = [[329040, 1094, 0, 0, 0],
           [3508, 381428, 0, 0, 0],
           [44, 0, 0, 50, 0],
           [27, 10, 0, 16432, 0],
           [10, 5, 0, 0, 0]]

    CNN = [[329214, 1091, 0, 1, 0],
           [4174, 380708, 0, 0, 0],
           [1, 7, 0, 87, 0],
           [0, 2, 0, 16350, 0],
           [7, 6, 0, 0, 0]]

    RNN = [[328028, 1298, 0, 0, 0],
           [3742, 382254, 0, 2, 0],
           [0, 0, 0, 79, 0],
           [0, 1, 0, 16227, 0],
           [17, 0, 0, 0, 0]]

    Exilir = [[329720, 14, 0, 1, 0],
              [21, 385497, 0, 0, 0],
              [0, 0, 98, 9, 0],
              [0, 0, 0, 16519, 0],
              [0, 0, 15, 0, 0]]

    cm=np.array(Exilir)
    # 按行进行归一化
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    print("Normalized confusion matrix")
    str_cm = cm.astype(np.str).tolist()
    print(str_cm)

    fig, ax = plt.subplots(figsize=(6.5 , 5 )) #fig表示窗口,ax表示坐标系

    im = ax.imshow(cm, interpolation='nearest', cmap=cmap, vmin=0, vmax=100, )    #热力图
    # contourf_ = ax.contourf(vmin=0, vmax=100)
    # ax = plt.pcolor(vmin=20, vmax=100)
    # cores = ax.contourf(vmin=0, vmax=40)
    clb = ax.figure.colorbar(im, ax=ax) # 侧边的颜色条带
    clb.ax.yaxis.set_major_locator(MultipleLocator(100))
    # clb.ax.yaxis.set_minor_locator(MultipleLocator(0.005))

    # cbar = plt.colorbar()


    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='Actual',
           xlabel='Predicted'
           )

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    fig.tight_layout()
    # plt.savefig('DGADARTS.jpg', dpi=300)
    pp = PdfPages('IOT混淆矩阵Exilir' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

plot_Matrix(['DoS','DDos','Normal','Recon','Theft'])