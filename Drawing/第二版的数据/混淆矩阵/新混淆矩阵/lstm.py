import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.Blues):

    plt.rc('font', size='18')  # 设置字体样式、大小，这边调小了一点
    Loong=[[19385   , 6   ,  1   ,   8  ,  3   ,  14   , 9  ,  22    ,43   , 84 ,  112 ,    7,
      4   , 12  , 51 ,    0 ,   38  , 223],
 [    2, 19877  ,  0 ,    0 ,    0  ,   0  ,   0  ,  0   ,  0    , 0,     0   ,  0,
      0  ,  0  ,  1  ,   0  ,   0   ,  0],
 [    0  ,   0 ,1236 ,    0 ,    0  ,   0  ,   0  ,  0   ,  0   ,  0  ,  0  ,   0,
      0  ,   0 ,   0 ,    0 ,    0  ,   0],
 [   11  ,   0 ,   0 , 5872 ,    0  ,  12  ,   0  ,  1    , 0   ,  1  ,  28     ,0,
      0  ,   0 ,   0 ,    0 ,    0  ,   0],
 [    3  ,   0 ,   0 ,    0 , 2420  ,   0  ,   0  ,  5   ,  0    , 0    , 0  ,   0,
      3  ,   0 ,   0 ,    1 ,    0  ,   0],
 [    7  ,   1 ,   0 ,   95 ,    1  ,1469  ,   0  ,  0    , 0   ,  2   ,118  ,  11,
      0  ,   5 ,   0 ,    0 ,   17  ,   0],
 [   12  ,   0 ,   0 ,    0 ,    0  ,   0  ,1907  ,  3    , 0  ,   0  ,   1 ,    0,
      0  ,   0 ,   0 ,    0 ,    0  ,   0],
 [   65  ,   0 ,   1 ,   14 ,    8  ,  22  ,   2 , 1378  ,   0   , 24   , 52  ,  43,
      7  ,   1 ,   0 ,    0 ,   33  ,   0],
 [  120  ,   1 ,   0 ,    0 ,    0  ,   0  ,   1  ,   0  , 876  ,   0   ,  0    , 0,
      0  ,   0 ,   1 ,    0 ,    0  ,   0],
 [   85  ,   2 ,   0 ,    0 ,    0  ,   9  ,   2   ,  2   ,  0  ,9040  ,  15  ,   0,
      0  ,  10 ,  26 ,    0 ,   27  ,   3],
 [  161  ,   0 ,   3 ,  329 ,    0  ,  46  ,   1  ,   8  ,   0   ,  3  ,3325 ,   76,
      0  ,   1 ,   1 ,    0 ,  227  ,   0],
 [    6  ,   0 ,   0 ,    0 ,    0  ,  20  ,   1     ,7 ,    0  ,   0  , 182  ,1880,
      0  ,   1 ,   0 ,    0 ,    0  ,   0],
 [    4  ,   0 ,   0 ,    0 ,    0  ,   0  ,   0   ,  9 ,   0   ,  0   , 15  ,   0,
   7234  ,   0 ,   0 ,    0 ,    0  ,   0],
 [   25  ,   0 ,   0 ,    4 ,    0  ,  26  ,   3  ,   1   ,  0  ,  21 ,   40 ,    0,
      2  ,1516 ,   0 ,    0 ,   14  ,   0],
 [   32  ,   1 ,   0 ,    0 ,    0  ,   0  ,   0  ,   0   ,  0   , 11   ,  0   ,  0,
      0  ,   0 ,5946 ,    0 ,    0  ,   0],
 [    0  ,   0 ,   0 ,    0 ,    0  ,   0  ,   0   ,  0  ,   0  ,   0   ,  0  ,   0,
      0  ,   0 ,   0 ,  862 ,    0  ,   0],
 [   57  ,   0 ,   0 ,    3 ,    0  ,   1  ,   0   ,  3  ,   1   ,  5   ,  6   ,  0,
      0  ,   3 ,   0 ,    0 ,14924  ,   0],
 [  271  ,   0 ,   0 ,    0 ,    0  ,   0  ,   0  ,   0  ,   0 ,    0   ,  0   ,  0,
      0  ,   0 ,   0 ,    0 ,    0  ,1604]]



    cm=np.array(Loong)
    # 按行进行归一化
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    print("Normalized confusion matrix")
    str_cm = cm.astype(np.str).tolist()
    print(str_cm)

    fig, ax = plt.subplots(figsize=(4.5 , 3.5 )) #fig表示窗口,ax表示坐标系

    im = ax.imshow(cm, interpolation='nearest', cmap=cmap, vmin=0, vmax=100, )    #热力图
    # contourf_ = ax.contourf(vmin=0, vmax=100)
    # ax = plt.pcolor(vmin=20, vmax=100)
    # cores = ax.contourf(vmin=0, vmax=40)
    clb = ax.figure.colorbar(im, ax=ax) # 侧边的颜色条带
    clb.ax.yaxis.set_major_locator(MultipleLocator(20))
    # clb.ax.yaxis.set_minor_locator(MultipleLocator(0.005))

    # cbar = plt.colorbar()

    tmp = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
    ax.set(xticks=tmp,
           yticks=tmp,
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True Class',
           xlabel='Predicted Class'
           )

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=60, ha="center",rotation_mode="default")

    fig.tight_layout()
    # plt.savefig('DGADARTS.jpg', dpi=300)
    pp = PdfPages('CM_DGA_lA_Mul07' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

plot_Matrix(['1','3','5','7','9','11','13','15','17'])