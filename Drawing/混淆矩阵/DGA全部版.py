import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams

def plot_Matrix(classes, title=None, cmap=plt.cm.YlGnBu):
    plt.rc('font', size='14')  # 设置字体样式、大小，这边调小了一点
    cNN_lstm = [[19787, 0, 4, 3, 0, 0, 1, 23, 21, 34, 47, 3,
                 2, 0, 24, 1, 11, 0],
                [0, 19827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0],
                [0, 0, 1232, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0],
                [11, 0, 0, 5905, 0, 34, 0, 0, 0, 0, 1, 0,
                 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2403, 3, 0, 6, 0, 1, 0, 0,
                 2, 0, 0, 0, 0, 0],
                [9, 0, 0, 57, 2, 1522, 0, 7, 0, 2, 70, 11,
                 0, 0, 0, 0, 16, 0],
                [2, 0, 0, 0, 0, 0, 2029, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0],
                [77, 0, 4, 8, 5, 18, 2, 1347, 0, 23, 50, 29,
                 10, 0, 0, 0, 33, 0],
                [80, 0, 0, 0, 0, 0, 0, 0, 966, 0, 0, 0,
                 0, 0, 0, 0, 1, 0],
                [39, 0, 0, 0, 1, 0, 0, 0, 0, 9036, 15, 0,
                 0, 0, 8, 0, 14, 0],
                [150, 0, 1, 336, 0, 56, 0, 0, 0, 0, 3297, 69,
                 2, 0, 0, 0, 229, 0],
                [4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 196, 1957,
                 0, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0,
                 7245, 0, 0, 0, 0, 0],
                [230, 0, 0, 119, 583, 60, 6, 73, 0, 61, 120, 44,
                 180, 0, 0, 0, 135, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 6062, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 855, 0, 0],
                [22, 0, 0, 0, 2, 0, 0, 2, 0, 3, 0, 0,
                 1, 0, 0, 0, 14986, 0],
                [1719, 0, 152, 0, 0, 0, 0, 0, 0, 21, 56, 0,
                 0, 0, 0, 0, 0, 0]]



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
    pp = PdfPages('DGA混淆矩阵全部cnn_lstm' + '.pdf')
    plt.savefig(pp, format='pdf', bbox_inches='tight')
    pp.close()
    plt.show()

plot_Matrix(['Alexa','Banjori',"Emotet","Flubot","Gameover","Murofet","Mydoom","Necurs","Ngioweb","Pykspa","Ramnit","Ranbyus","Rovnix","Shiotob","Simda","Symmi","Tinba","Viryt"
])