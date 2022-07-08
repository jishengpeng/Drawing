import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

HATCH = ['+', 'x', '/', 'o', '|', '\\', '-', 'O', '.', '*']
COLORS = sns.color_palette("Paired")

# Traffic Service(ISCX):
ISCX1 = [769, 124, 107, 75]
ISCX2 = [0, 124 * 15, 107 * 35, 75 * 35]
ISCXlabel = ['Loong', 'FSNet', 'APPNet', 'BGRUA']
# Traffic Application(UNIBS):
UNIBS1 = [456, 124, 107, 274]
UNIBS2 = [0, 124 * 15, 107 * 35, 274 * 17]
UNIBSlabel = ['Loong', 'FSNet', 'APPNet', 'ConvLSTM']
# Anomaly(UNSW-NB15):
UNSW1 = [266, 38, 31, 45]
UNSW2 = [0, 38 * 26, 31 * 26, 45 * 17]
UNSWlabel = ['Loong', 'DeepLSTM', 'FFDNN', 'LuNet']

total=['Loong', 'FSNet', 'APPNet', 'BGRUA','Loong', 'FSNet', 'APPNet', 'ConvLSTM','Loong', 'DeepLSTM', 'FFDNN', 'LuNet']




label1 = [0.1,0.2,0.3,0.4]
label2 = [0.6,0.7,0.8,0.9]
label3=[1.1,1.2,1.3,1.4]


width=0.1
fig, ax = plt.subplots(figsize=(6.5,3.5))

ax.bar(label1,ISCX1, width,label='Traffic Service Train',ec=COLORS[9], hatch=HATCH[2] * 4)
ax.bar(label1,ISCX2, width,bottom=ISCX1,label='Traffic Service Design',ec=COLORS[1],hatch=HATCH[1] * 4)
ax.bar(label2,UNIBS1, width, label='Traffic Application Train',ec=COLORS[5], hatch=HATCH[2] * 4)
ax.bar(label2,UNIBS2, width,bottom=UNIBS1,label='Traffic Application Design',ec=COLORS[2],hatch=HATCH[1] * 4)
ax.bar(label3,UNSW1, width, label='Anomaly Train', ec=COLORS[7], hatch=HATCH[2] * 4)
ax.bar(label3,UNSW2, width,bottom=UNSW1,label='Anomaly Design',ec=COLORS[10],hatch=HATCH[1] * 4)

ax.set_xticks([0.1,0.2,0.3,0.4,0.6,0.7,0.8,0.9,1.1,1.2,1.3,1.4])
ax.set_xticklabels(total,fontsize =8,rotation =20)

plt.ylim(0,9000)
ax.set_ylabel('Minutes',fontsize=15)

ax.legend()

pp = PdfPages('时间对比2.pdf')
plt.savefig(pp, format='pdf', bbox_inches='tight')
pp.close()

plt.show()