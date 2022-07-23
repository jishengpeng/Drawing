import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.Blues):
    plt.rc('font', size='16')  # 设置字体样式、大小，这边调小了一点
    Loong=[[19780 ,    3,   0 ,    6 ,   2  ,  0   , 0  , 0  , 0 ,  52   ,67  ,   2,
      4,    0 ,   39 ,   0 ,   28 ,   0],
 [    1,20031 ,    0 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  0,    0 ,   0,
      0,    0 ,    0 ,   0 ,    0 ,   0],
 [    0,    0 , 1182 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  0,    0 ,   0,
      0,    0 ,    0 ,   0 ,    0 ,   0],
 [    9,    0 ,    0 ,5962 ,    0 ,   0  ,   0  ,  0  ,  0 ,  0,    0 ,   0,
      0,    0 ,    0 ,   0 ,    1 ,   0],
 [    0,    0 ,    0 ,   0 , 2316 ,   0  ,   0  ,  0  ,  0 ,  0,    3 ,   0,
      2,    0 ,    0 ,   0 ,    0 ,   0],
 [    4,    0 ,  131 , 477 ,  129 ,   0  ,   0  ,  0  ,  0 ,112,  379 , 304,
    118,    0 ,    0 ,   0 ,   35 ,   0],
 [  376,    0 ,  221 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,437, 1000 ,   0,
      0,    0 ,    1 ,   0 ,    0 ,   0],
 [  215,    1 ,  109 ,  97 ,  138 ,   0  ,   0  ,  0  ,  0 ,100,  541 , 207,
    122,    0 ,    3 ,   0 ,  137 ,   0],
 [ 1022,    0 ,    1 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  3,    0 ,   1,
      0,    0 ,    3 ,   0 ,    2 ,   0],
 [   43,    0 ,    0 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,8031,   15,    0,
      0,    0 ,   14 ,   0 ,  979 ,   0],
 [  161,    0 ,    1 , 348 ,    0 ,   0  ,   0  ,  0  ,  0 ,  0, 2852 ,   2,
    296,    0 ,    0 ,   0 ,  339 ,   0],
 [    5,    0 ,    0 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  1,  273 ,1874,
      0,    0 ,    0 ,   0 ,    0 ,   0],
 [    1,    0 ,    0 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  0,    0 ,   0,
   7350,    0 ,    0 ,   0 ,    0 ,   0],
 [  148,    0 ,   14 , 299 ,    0 ,   0  ,   0  ,  0  ,  0 ,188,  476 , 125,
      0,    0 ,    1 ,   0 ,  254 ,   0],
 [    3,    0 ,    0 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  2,    0 ,   0,
      0,    0 , 6026 ,   0 ,    0 ,   0],
 [  450,    3 ,    0 ,  80 ,   15 ,   0  ,   0  ,  0  ,  0 , 77,   74 ,  66,
     78,    0 ,    0 ,   0 ,   11 ,   0],
 [   15,    0 ,    4 ,   1 ,    0 ,   0  ,   0  ,  0  ,  0 ,  0,    0 ,   1,
      0,    0 ,    0 ,   0 ,15033 ,   0],
 [ 1971,    5 ,    0 ,   0 ,    0 ,   0  ,   0  ,  0  ,  0 ,  3,   12 ,   0,
      0,    0 ,    0 ,   0 ,    0 ,    0]]



    cm=np.array(Loong)
    # 按行进行归一化
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
    # print("Normalized confusion matrix")
    str_cm = cm.astype(np.str).tolist()
    # print(str_cm)

    fig, ax = plt.subplots(figsize=(4.5 , 3.5 )) #fig表示窗口,ax表示坐标系

    im = ax.imshow(cm, interpolation='nearest', cmap=cmap, vmin=0, vmax=100, )    #热力图
    # contourf_ = ax.contourf(vmin=0, vmax=100)
    # ax = plt.pcolor(vmin=20, vmax=100)
    # cores = ax.contourf(vmin=0, vmax=40)
    clb = ax.figure.colorbar(im, ax=ax) # 侧边的颜色条带
    clb.ax.yaxis.set_major_locator(MultipleLocator(20))
    # clb.ax.yaxis.set_minor_locator(MultipleLocator(0.005))

    # cbar = plt.colorbar()


    tmp=np.array([0,2,4,6,8,10,12,14,16])
    tmp1=np.array([1,3,5,7,9,11,13,15,17])
    # np.arange(cm.shape[1])

    ax.set(xticks=tmp,
           yticks=tmp,
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True Class',
           xlabel='Predicted Class'
           )

    # ax.tick_params(labelsize=16)

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=60, ha="center",rotation_mode="default")

    fig.tight_layout()
    # plt.savefig('DGADARTS.jpg', dpi=300)
    pp = PdfPages('CM_DGA_BiLSTM' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()
    # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

plot_Matrix(['1','3','5','7','9','11','13','15','17'])