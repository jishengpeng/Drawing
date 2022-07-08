import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
COLORS = sns.color_palette("Paired")

DGA1=[306,55,31,42]
DGA2=[0,55*17,31*17,42*17]
DGAlabel=["Loong","BiLSTM","LA_Mul07","R-CNN"]

DNS1=[1340,116,128,95]
DNS2=[0,116*11,128*26,95*26]
DNSlabel=["Loong","LSTM","CNN","DNN"]

IOT1=[571,213,124,119]
IOT2=[0,213*17,124*26,119*17]
IOTLabel=["Loong","DNN","CNN","RNN"]

total=["Loong","BiLSTM","LA_Mul07","CNNLSTM","Loong","LSTM","CNN","DNN","Loong","DNN","CNN","RNN"]




label1 = [0.1,0.2,0.3,0.4]
label2 = [0.6,0.7,0.8,0.9]
label3=[1.1,1.2,1.3,1.4]


width=0.1
fig, ax = plt.subplots(figsize=(6.5,3.5))

ax.bar(label1,DGA1, width,label='DGA Family Train',ec=COLORS[9], hatch=HATCH[2] * 4)
ax.bar(label1,DGA2, width,bottom=DGA1,label='DGA Family Design',ec=COLORS[1],hatch=HATCH[1] * 4)
ax.bar(label2,DNS1, width, label='DNS Tunnel Train',ec=COLORS[5], hatch=HATCH[2] * 4)
ax.bar(label2,DNS2, width,bottom=DNS1,label='DNS Tunnel Design',ec=COLORS[2],hatch=HATCH[1] * 4)
ax.bar(label3,IOT1, width, label='IOT Attack Train', ec=COLORS[7], hatch=HATCH[2] * 4)
ax.bar(label3,IOT2, width,bottom=IOT1,label='IOT Attack Design',ec=COLORS[10],hatch=HATCH[1] * 4)

ax.set_xticks([0.1,0.2,0.3,0.4,0.6,0.7,0.8,0.9,1.1,1.2,1.3,1.4])
ax.set_xticklabels(total,fontsize =8,rotation =20)


ax.set_ylabel('Minutes',fontsize=15)

ax.legend()

pp = PdfPages('时间对比.pdf')
plt.savefig(pp, format='pdf', bbox_inches='tight')
pp.close()

plt.show()