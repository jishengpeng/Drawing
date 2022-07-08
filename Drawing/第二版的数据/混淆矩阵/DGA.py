import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.YlGnBu):
    plt.rc('font', size='14')  # 设置字体样式、大小，这边调小了一点
    cNN_lstm = [[19654   ,  0    , 0   ,  2  ,   0   ,  1  ,   3   , 12    , 4 ,  25   , 30  ,   2,
      1   ,  7   ,  5 ,    0   ,  7 ,  155],
 [    1 ,20012   ,  0   ,  0   ,  0 ,    0  ,   0  ,   0  ,   0  ,   0 ,    0  ,   0,
      0  ,   0   ,  0  ,   0  ,   0  ,   0],
 [    0   ,  0 , 1195  ,   0   ,  0  ,   0  ,   0  ,   0   ,  0  ,   0  ,   0 ,    0,
      0   ,  0   ,  0  ,   0  ,   0   ,  0],
 [    2   ,  0  ,   0 , 5848  ,   0  ,  28   ,  0   ,  0   ,  0    , 0   ,158 ,    0,
      0  ,   0   ,  0 ,    0  ,   0   ,  0],
 [    0   ,  0  ,  0 ,   0 , 2373,    0  ,   0 ,   8 ,    0 ,    0 ,    1  ,   0,
      1   ,  0  ,  0 ,   0 ,    0,    0],
 [    1   ,  0  ,  0 ,  56 ,    0, 1541  ,   0 ,   4 ,   0 ,   0  ,  97  ,   9,
      0   ,  6  ,  0 ,   0 ,    9,    0],
 [    0   ,  0  ,  0 ,   0 ,    0,    0  ,2062 ,   0 ,   0 ,   0  ,   0   ,  0,
      0   ,  0  ,  0 ,   0 ,    0,    0],
 [   21  ,   0  ,  2 ,  10 ,    2,   12  ,   0 ,1441 ,   0 ,   9   , 46  ,  34,
      9   ,  3  ,  0 ,   0 ,   31,    0],
 [    7   ,  0  ,  0 ,   0 ,    0,    0  ,   0 ,   0 ,1055 ,   0  ,   0   ,  0,
      0   ,  0  ,  0 ,   0 ,    0,    0],
 [   40  ,   0  ,  0 ,   0 ,    0,    0  ,   0 ,  13 ,   0 ,9027   , 15   ,  0,
      0   , 17  ,  1 ,   0 ,   12,    5],
 [   90  ,   0  ,  3 , 266 ,    0,   63  ,   0 ,  20 ,   0 ,   0 , 3205  , 126,
      1   ,  4  ,  0 ,   0 ,  198,    0],
 [    1   ,  0  ,  0 ,   0 ,    0,    9  ,   0 ,   3 ,   0 ,   0  , 176 , 1994,
      0   ,  4  ,  0 ,   0 ,    0,    0],
 [    1  ,   0  ,  0 ,   0 ,    0,    0  ,   0 ,   2 ,   0 ,   0  ,   5   ,  0,
   7307  ,   0  ,  0 ,   0 ,    0,    0],
 [    3  ,   0  ,  0 ,   0 ,    0,    8  ,   0 ,   3 ,   0 ,   2  ,  23 ,    3,
      0  ,1517  ,  0 ,   0 ,    3,    0],
 [    0  ,   1  ,  0 ,   0 ,    0,    0  ,   0 ,   0 ,   0 ,   0  ,   0  ,   0,
      0  ,   0  ,6041,    0,     0,     0],
 [    0  ,   0  ,  0 ,   0 ,    0,    0  ,   0 ,   0 ,   0 ,   0  ,   0   ,  0,
      0  ,   0  ,  0 , 877 ,    0,    0],
 [   12  ,   0  ,  0 ,   1 ,    0,    0  ,   0 ,   2 ,   0 ,   0  ,  43   ,  0,
      0  ,   0  ,  0 ,   0 ,15073,    0],
 [  145  ,   0  ,  0 ,   0 ,    0,    0  ,   0 ,   0 ,   0 ,   1  ,   0   ,  0,
      0  ,   0  ,  0 ,   0 ,    0, 1762]]



    cm=np.array(cNN_lstm)
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
           ylabel='Actual',
           xlabel='Predicted'
           )

    # 将x轴上的lables旋转45度
    plt.setp(ax.get_xticklabels(), rotation=90, ha="center",rotation_mode="default")

    fig.tight_layout()
    # plt.savefig('DGADARTS.jpg', dpi=300)
    pp = PdfPages('DGA混淆矩阵全部Elixir' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

plot_Matrix(['Alexa','Banjori',"Emotet","Flubot","Gameover","Murofet","Mydoom","Necurs","Ngioweb","Pykspa","Ramnit","Ranbyus","Rovnix","Shiotob","Simda","Symmi","Tinba","Viryt"
])