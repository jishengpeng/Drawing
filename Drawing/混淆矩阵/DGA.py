import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.YlGnBu):
    plt.rc('font', size='18')  # 设置字体样式、大小
    #cm1是exilir,选取类别0，8，9，10，11，12
    cm1=[[19732   ,   2   , 15  ,  36   ,  1,1    ],
    [    2    ,1064   ,  0    , 0   ,  0,0  ],
    [   22      ,0 , 9043 ,   11   ,  0,0  ],
    [   42    ,    0  ,   1 , 3584  ,81,1  ],
    [    0   ,   0   ,  0  , 128  ,2078,0  ],
    [    0   ,  0    , 0  ,   6  ,   0,7437   ]]

    lstm = [[19385,43, 84, 112, 7,4, ],
            [120,  876, 0, 0, 0, 0],
            [85,  0, 9040, 15, 0, 0],
            [161, 0, 3, 3325, 76, 0],
            [6, 0, 0, 182, 1880,0],
            [4,  0, 0, 15, 0,7234]]

    bilstm = [[19780,  0, 52, 67, 2,4],
              [1022,  0, 3, 0, 1,0],
              [43,  0, 8031, 15, 0,0],
              [161, 0, 0, 2852, 2,296],
              [5,  0, 1, 273, 1874,0],
              [1, 0, 0, 0, 0,7350]]

    cnn_lstm = [[19787,  21, 34, 47, 3,2],
                [80, 966, 0, 0, 0,0],
                [39, 0, 9036, 15, 0,0],
                [150,  0, 0, 3297, 69,2],
                [4,  0, 0, 196, 1957,0],
                [3,0, 0, 15, 0,7245]]

    cm=np.array(lstm)
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
    # rotation_mode = "anchor"
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode = "anchor")

    fig.tight_layout()
    # plt.savefig('DGADARTS.jpg', dpi=300)
    pp = PdfPages('DGA混淆矩阵lstm' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

plot_Matrix(['Alexa','Ngioweb','Pykspa','Ramnit','Ranbyus','Rovnix'])