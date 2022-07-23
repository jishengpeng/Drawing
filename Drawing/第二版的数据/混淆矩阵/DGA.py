import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.YlGnBu):
    plt.rc('font', size='14')  # 设置字体样式、大小，这边调小了一点
    Loong=[[19732   ,  0  ,   0   ,  1   ,  0   ,  0 ,    0   ,11   ,  2   , 15  ,  36   ,  1,
      1    , 5    , 3    , 0  ,   6  , 135],
 [    0 ,19926    , 0   ,  0 ,    0  ,   0   ,  0    , 0    , 0 ,    0   ,  0 ,    0,
      0   ,  0    , 0  ,   0   ,  0    , 0],
 [    0  ,   0 , 1165   ,  0   ,  0   ,  0    , 0  ,   0    ,0     ,0    , 0   ,  0,
      0    , 0     ,0   ,  0  ,   0  ,   0],
 [    0   ,  0  ,   0 , 5856   ,  0  ,  20   ,  0  ,   0 ,    0    , 0  ,  75   ,  0,
      0   ,  0   ,  0   ,  0 ,    0  ,   0],
 [    0  ,   0   ,  0   ,  0 , 2367   ,  0  ,   0  ,   5  ,   0   ,  0,     0   ,  0,
      2   ,  0   ,  0  ,   0  ,   0   ,  0],
 [    0   ,  0   ,  0  ,  50  ,   0  ,1627  ,   0  ,   2  ,   0 ,    0    ,67   ,  6,
      0   ,  1   ,  0   ,  0  ,   3   ,  0],
 [    0   ,  0   ,  0   ,  0   ,  0  ,   0 , 2009   ,  0   ,  0  ,   0   ,  0   ,  0,
      0    , 0   ,  0  ,   0  ,   0   ,  0],
 [   21   ,  0   ,  0  ,   7  ,   1   , 12  ,   0 , 1479  ,   0  ,   8   , 43  ,  28,
      1   ,  1   ,  1   ,  0  ,  14    , 0],
 [    2    , 0   ,  0   ,  0   ,  0  ,   0   ,  0   ,  0  ,1064   ,  0    , 0   ,  0,
      0   ,  0    , 0  ,   0   ,  0     ,0],
 [   22   ,  0   ,  0    , 0   ,  0   ,  0  ,   0    , 6     ,0 , 9043 ,   11   ,  0,
      0   ,  9   ,  0  ,   0   ,  7   ,  4],
 [   42    , 0   ,  4 ,  185  ,   0  ,  46  ,   0  ,  19  ,   0  ,   1 , 3584  ,81,
      1   ,  3   ,  0  ,   0  , 147 ,    0],
 [    0   ,  0   , 0  ,   0   ,  0   ,  6    , 0   ,  6  ,   0   ,  0  , 128  ,2078,
      0  ,   1   ,  0   ,  0   ,  0   ,  0],
 [    0   ,  0  ,   0    , 0   ,  0    , 0    , 0   ,  2    , 0    , 0  ,   6  ,   0,
   7437   ,  0  ,   0    , 0   ,  0   ,  0],
 [    3   ,  0  ,   0   ,  0   ,  0   ,  5    , 0   ,  4   ,  0  ,   3   , 23   ,  2,
      0  ,1566  ,   0   ,  0   ,  5  ,   0],
 [    0  ,   0  ,   0   ,  0   ,  0  ,   0   ,  0    , 0   ,  0  ,   0  ,   0    , 0,
      0  ,   0 , 6132   ,  0   ,  0   ,  0],
 [    0   ,  0   ,  0    , 0 ,    0   ,  0  ,   0    , 0  ,   0     ,0  ,   0   ,  0,
      0   ,  0    , 0   ,856 ,    0  ,   0],
 [   11   ,  0   ,  0    , 0    , 0   ,  0   ,  0     ,1     ,0  ,   1  ,  25   ,  0,
      0   ,  1    , 0   ,  0 ,14889   ,  0],
 [   78   ,  0   ,  0   ,  0   ,  0  ,   0   ,  0   ,  0  ,   0   ,  0  ,   0   ,  0,
      0   ,  0   ,  0 ,    0  ,   0,  1835]]



    cm=np.array(Loong)
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
    clb.ax.yaxis.set_major_locator(MultipleLocator(20))
    # clb.ax.yaxis.set_minor_locator(MultipleLocator(0.005))

    # cbar = plt.colorbar()


    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True Class',
           xlabel='Predicted Class'
           )

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=90, ha="center",rotation_mode="default")

    fig.tight_layout()
    # plt.savefig('DGADARTS.jpg', dpi=300)
    pp = PdfPages('DGA混淆矩阵全部Loong' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

plot_Matrix(['Alexa','Banjori',"Emotet","Flubot","Gameover","Murofet","Mydoom","Necurs","Ngioweb","Pykspa","Ramnit","Ranbyus","Rovnix","Shiotob","Simda","Symmi","Tinba","Viryt"
])