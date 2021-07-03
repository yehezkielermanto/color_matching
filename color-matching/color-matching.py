import numpy as np
import pandas as pd
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

img = cv2.imread("color_ex_2.jpg")

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

clicked = False
r = g = b = xpos = ypos = 0

def check_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked,nilai_r,nilai_g,nilai_b
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        nilai_r = r
        nilai_b = b
        nilai_g = g

cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', mouse_click)


#gui input box
class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(422, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
  
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))
  
        # For displaying confirmation message along with user's info. 
        self.label = QtWidgets.QLabel(self.centralwidget)    
        self.label.setGeometry(QtCore.QRect(20, 20, 500, 111))
  
        # Keeping the text of label empty initially.       
        self.label.setText("")     
  
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hasil Kemungkinan"))
        nilai_r, done1 = QtWidgets.QInputDialog.getInt(
        self, 'Input Dialog', 'Masukkan nilai R:')  
        nilai_g, done2 = QtWidgets.QInputDialog.getInt(
        self, 'Input Dialog', 'Masukkan nilai G:')  
        nilai_b, done3 = QtWidgets.QInputDialog.getInt(
        self, 'Input Dialog', 'Masukkan nilai B:')  
          
    #def takeinputs(self):

  
        if done1 and done2 and done3:
             # Showing confirmation message along
             # with information provided by user. 
             self.label.setText('Warna Kemungkinan :'+check_color(nilai_r,nilai_g,nilai_b) + '\n' + ' R='+ str(nilai_r) +  ' G='+ str(nilai_g) +  ' B='+ str(nilai_b)+'\nBerikut hasil jadi pengecekan warna, tekan "esc" untuk menutup aplikasi')   
   
             # Hide the pushbutton after inputs provided by the use.
             self.pushButton.hide()      
                
               
               
if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow) 
    MainWindow.show()



while(1):
    cv2.imshow("Color Recognition",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display( Color name and RGB values )
        text = check_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()


