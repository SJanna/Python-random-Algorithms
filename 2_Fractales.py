from PyQt5 import QtCore, QtGui, QtWidgets
from turtle import*
from random import randint
import turtle

#Dibujo con turtle del Box Fractal
def avance(r,n):
  if n==0:
    forward(r/1.5)
  else:
    color(randint(0,255),randint(0,255),randint(0,255))#Color aleatorio
    avance(r/3,n-1)
    right(90)
    avance(r/3,n-1)
    left(90)
    avance(r/3,n-1)
    left(90)
    avance(r/3,n-1)
    right(90)
    avance(r/3,n-1)
def curve(r,n):
  begin_fill()
  avance(r,n)
  right(90)
  avance(r,n)
  right(90)
  avance(r,n)
  right(90)
  avance(r,n)
  right(90)
  #color(0,0,0)#Desactivado Color de fondo fijo
  end_fill()

  
#Dibujo con turtle del H Fractal  
def h_tree(order, center, size):
    draw_turtle(center, size)
    if order > 0:
        ep1, ep2, ep3, ep4 = get_endpoints(center, size)
        color(randint(0,255),randint(0,255),randint(0,255))#Color aleatorio
        h_tree(order - 1, (ep1, ep2), size / 2)
        h_tree(order - 1, (ep1, ep4), size / 2)
        h_tree(order - 1, (ep3, ep2), size / 2)
        h_tree(order - 1, (ep3, ep4), size / 2)
        
def draw_turtle(center, size):
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()

    turtle.forward(size / 2)  # lado derecho
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.right(180)
    turtle.forward(size)

    turtle.penup()
    turtle.goto(center)
    turtle.pendown()

    turtle.right(90)  # lado izquierdo
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(180)
    turtle.forward(size)
    turtle.right(90)  

def get_endpoints(center, size):
    ep1 = center[0] + size / 2
    ep2 = center[1] + size / 2
    ep3 = center[0] - size / 2
    ep4 = center[1] - size / 2

    return ep1, ep2, ep3, ep4

#Función generadora del H Fractal 
def mainFractal2():
    turtle.hideturtle()
    screen=Screen()
    #screen.tracer(False)
    colormode(255) #Color aleatorio
    speed(0)
    e=numinput("H Fractal", "Digíte n",1,minval=0,maxval=100)
    h_tree(e, (0, 0), 300)
    #turtle.done()

#Función generadora del Box Fractal  
def mainFractal1():
    wn = turtle.Screen()
    #Barras de desplazamiento
    screen = Screen()
    wn.screensize(30_00, 30_00)
    screen.tracer(False)#Elimina el dibujo paso a paso   
    colormode(255)#Color aleatorio
    hideturtle()#Adorno
    x=500
    e=numinput("Box Fractal", "Digíte n",1,minval=0,maxval=100)
    area=(5/9)**e*100 #Calculo del %área sombreada
    turtle.write((area,'% del area sombreada'), move = False, align = "left", font = ("Times", 13, "normal"))
    curve(x,e)



#Interfaz gráfica generada por PyQt5 adaptada al código    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 70, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 170, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickme)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Box Fractal"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fractal H"))
        self.pushButton.setText(_translate("MainWindow", "GENERAR"))

    def clickme(self): #Función encargada de mostrar el Fractal que se escoge en la UI
        turtle.clear()
        if(self.comboBox.currentIndex()==0):
            MainWindow.close()
            mainFractal1()
            turtle.update()
            MainWindow.show()
        else:
            MainWindow.close()
            mainFractal2()
            turtle.update()
            MainWindow.show()
#Main                            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
