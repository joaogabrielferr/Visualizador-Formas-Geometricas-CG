#Trabalho Pratico 3 Computacao Grafica
#Joao Gabriel Ferreira


from PyQt5 import QtCore, QtGui, QtWidgets,QtGui,Qt
from random import seed
from random import randint
from os import write
from Classes import *
import xml.etree.ElementTree as XML
import sys
from PyQt5.QtWidgets import QMessageBox
import math
from Clipping import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VIEWPORT = QtWidgets.QGraphicsView(self.centralwidget)
        self.VIEWPORT.setGeometry(QtCore.QRect(10, 30, 721, 511))
        self.VIEWPORT.setObjectName("VIEWPORT")
        self.Listaobjetos = QtWidgets.QListWidget(self.centralwidget)
        self.Listaobjetos.setGeometry(QtCore.QRect(920, 30, 256, 321))
        self.Listaobjetos.setObjectName("Listaobjetos")
        self.Labelobjetos = QtWidgets.QLabel(self.centralwidget)
        self.Labelobjetos.setGeometry(QtCore.QRect(920, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Labelobjetos.setFont(font)
        self.Labelobjetos.setObjectName("Labelobjetos")
        self.Aumentaescala = QtWidgets.QPushButton(self.centralwidget)
        self.Aumentaescala.setGeometry(QtCore.QRect(740, 30, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Aumentaescala.setFont(font)
        self.Aumentaescala.setObjectName("Aumentaescala")
        self.Diminuiescala = QtWidgets.QPushButton(self.centralwidget)
        self.Diminuiescala.setGeometry(QtCore.QRect(850, 30, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Diminuiescala.setFont(font)
        self.Diminuiescala.setObjectName("Diminuiescala")
        self.Labelviewport = QtWidgets.QLabel(self.centralwidget)
        self.Labelviewport.setGeometry(QtCore.QRect(10, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Labelviewport.setFont(font)
        self.Labelviewport.setObjectName("Labelviewport")
        self.Sobe = QtWidgets.QPushButton(self.centralwidget)
        self.Sobe.setGeometry(QtCore.QRect(800, 30, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Sobe.setFont(font)
        self.Sobe.setObjectName("Sobe")
        self.Esquerda = QtWidgets.QPushButton(self.centralwidget)
        self.Esquerda.setGeometry(QtCore.QRect(750, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Esquerda.setFont(font)
        self.Esquerda.setObjectName("Esquerda")
        self.Direita = QtWidgets.QPushButton(self.centralwidget)
        self.Direita.setGeometry(QtCore.QRect(850, 80, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Direita.setFont(font)
        self.Direita.setObjectName("Direita")
        self.Desce = QtWidgets.QPushButton(self.centralwidget)
        self.Desce.setGeometry(QtCore.QRect(800, 130, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Desce.setFont(font)
        self.Desce.setObjectName("Desce")
        self.Inputponto = QtWidgets.QTextEdit(self.centralwidget)
        self.Inputponto.setGeometry(QtCore.QRect(920, 390, 131, 31))
        self.Inputponto.setObjectName("Inputponto")
        self.Botaoaddponto = QtWidgets.QPushButton(self.centralwidget)
        self.Botaoaddponto.setGeometry(QtCore.QRect(1070, 390, 101, 31))
        self.Botaoaddponto.setObjectName("Botaoaddponto")
        self.Inputreta = QtWidgets.QTextEdit(self.centralwidget)
        self.Inputreta.setGeometry(QtCore.QRect(890, 430, 161, 31))
        self.Inputreta.setObjectName("Inputreta")
        self.Botaoaddreta = QtWidgets.QPushButton(self.centralwidget)
        self.Botaoaddreta.setGeometry(QtCore.QRect(1070, 430, 101, 31))
        self.Botaoaddreta.setObjectName("Botaoaddreta")
        self.Inputpoligono = QtWidgets.QTextEdit(self.centralwidget)
        self.Inputpoligono.setGeometry(QtCore.QRect(760, 470, 291, 31))
        self.Inputpoligono.setObjectName("Inputpoligono")
        self.Botaoaddpoligono = QtWidgets.QPushButton(self.centralwidget)
        self.Botaoaddpoligono.setGeometry(QtCore.QRect(1070, 470, 101, 31))
        self.Botaoaddpoligono.setObjectName("Botaoaddpoligono")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1010, 350, 161, 23))
        self.pushButton.setObjectName("pushButton")
        self.rotacionaesquerda = QtWidgets.QPushButton(self.centralwidget)
        self.rotacionaesquerda.setGeometry(QtCore.QRect(740, 130, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rotacionaesquerda.setFont(font)
        self.rotacionaesquerda.setObjectName("rotacionaesquerda")
        self.rotacionadireita = QtWidgets.QPushButton(self.centralwidget)
        self.rotacionadireita.setGeometry(QtCore.QRect(850, 130, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rotacionadireita.setFont(font)
        self.rotacionadireita.setObjectName("rotacionadireita")
        self.cliparObjetos = QtWidgets.QRadioButton(self.centralwidget)
        self.cliparObjetos.setGeometry(QtCore.QRect(740, 220, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cliparObjetos.setFont(font)
        self.cliparObjetos.setObjectName("cliparObjetos")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(740, 270, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mensagemalgo = QtWidgets.QLabel(self.centralwidget)
        self.mensagemalgo.setGeometry(QtCore.QRect(750, 330, 151, 81))
        self.mensagemalgo.setObjectName("mensagemalgo")
        self.algo1 = QtWidgets.QPushButton(self.centralwidget)
        self.algo1.setGeometry(QtCore.QRect(740, 290, 171, 23))
        self.algo1.setObjectName("algo1")
        self.algo2 = QtWidgets.QPushButton(self.centralwidget)
        self.algo2.setGeometry(QtCore.QRect(740, 320, 171, 23))
        self.algo2.setObjectName("algo2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ################################################################

        self.CLIPAR = False
        self.algoritmo1 = True

        #objeto representando a window
        self.window = Window(0,0,0,0)

        #objetos na window
        self.pontoswindow = []
        self.retaswindow = []
        self.poligonoswindow = []

        #objetos na viewport
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        #valores do viewport
        self.vpminx = 0
        self.vpminy = 0
        self.vpmaxx = 0
        self.vpmaxy = 0

        #valores da window
        self.wminx = 0
        self.wminy = 0
        self.wmaxx = 0
        self.wmaxy = 0  

        self.contadorpontos = 1
        self.contadorretas = 1
        self.contadorpoligonos = 1

        #cria cena para a Graphics View
        self.cena = QtWidgets.QGraphicsScene()

        if len(sys.argv) > 1:
            #arquivo xml foi passado como entrada
            tree = XML.parse(sys.argv[1])
            dados = tree.getroot()
            #pega valores do viewport
            for viewport in dados.findall("viewport"):
                for vpmin in viewport.findall("vpmin"):
                    self.vpminx = float(vpmin.get("x"))
                    self.vpminy = float(vpmin.get("y"))
                for vpmax in viewport.findall("vpmax"):
                    self.vpmaxx = float(vpmax.get("x"))
                    self.vpmaxy = float(vpmax.get("y"))


            #Seta os valores da viewport
            self.cena.setSceneRect(self.vpminx,self.vpminy,self.vpmaxx,self.vpmaxy)
            #self.cena.setSceneRect(1,1,1080,720)

            #coloca a cena no graphics view
            self.VIEWPORT.setScene(self.cena)
            caneta = QtGui.QPen(QtCore.Qt.green)
            bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
            bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
            bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
            bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

            #pega valores da window
            for window in dados.findall("window"):
                for wmin in window.findall("wmin"):
                    self.wminx = wmin.get("x")
                    self.wminy = wmin.get("y")
                for wmax in window.findall("wmax"):
                    self.wmaxx = wmax.get("x")
                    self.wmaxy = wmax.get("y")
            #seta valores para a window
            self.window = Window(float(self.wminx),float(self.wminy),float(self.wmaxx),float(self.wmaxy))
            #pega todos os pontos do arquivo xml
            for ponto in dados.findall("ponto"):
                x = ponto.get("x")
                y = ponto.get("y")
                z = ponto.get("z")
                p = Ponto(float(x),float(y),float(z))
                obj = []
                obj.append(p)
                obj.append("ponto {}".format(self.contadorpontos))
                self.pontoswindow.append(obj)
                self.contadorpontos = self.contadorpontos + 1
        

            #pega todas as retas do arquivo xml
            for reta in dados.findall("reta"):
                r = Reta()
                for ponto in reta.findall("ponto"):
                    x = ponto.get("x")
                    y = ponto.get("y")
                    z = ponto.get("z")
                    p = Ponto(float(x),float(y),float(z))
                    r.addponto(p)
                obj = []
                obj.append(r)
                obj.append("reta {}".format(self.contadorretas))
                self.retaswindow.append(obj)
                self.contadorretas = self.contadorretas + 1

            #pega todos os poligonos do arquivo xml
            for pol in dados.findall("poligono"):
                poligono = Poligono()
                for ponto in pol.findall("ponto"):
                    x = ponto.get("x")
                    y = ponto.get("y")
                    z = ponto.get("z")
                    p = Ponto(float(x),float(y),float(z))
                    poligono.addponto(p)
                obj = []
                obj.append(poligono)
                obj.append("poligono {}".format(self.contadorpoligonos))
                self.poligonoswindow.append(obj)
                self.contadorpoligonos = self.contadorpoligonos + 1
            

            #passa todos os pontos para as coordenadas da viewport
            self.windowparaviewport()

            #coloca todos os pontos na tela
            self.paraviewport()
        else:
            self.wminx = 0.0
            self.wminy = 0.0
            self.wmaxx = 20.0
            self.wmaxy = 20.0
            self.vpminx = 0.0
            self.vpminy = 0.0
            self.vpmaxx = 640.0
            self.vpmaxy = 480.0
            #seta valores para a window
            self.window = Window(float(self.wminx),float(self.wminy),float(self.wmaxx),float(self.wmaxy))
            #Seta os valores da viewport
            self.cena.setSceneRect(self.vpminx,self.vpminy,self.vpmaxx,self.vpmaxy)
            #coloca a cena no graphics view
            self.VIEWPORT.setScene(self.cena)
            caneta = QtGui.QPen(QtCore.Qt.green)
            bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
            bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
            bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
            bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)


        self.Botaoaddponto.clicked.connect(self.Addponto)
        self.Botaoaddreta.clicked.connect(self.addreta)
        self.Botaoaddpoligono.clicked.connect(self.addpoligono)
        self.Aumentaescala.clicked.connect(self.maisescala)
        self.Diminuiescala.clicked.connect(self.menosescala)
        self.Esquerda.clicked.connect(self.vaiesquerda)
        self.Direita.clicked.connect(self.vaidireita)
        self.Desce.clicked.connect(self.vaibaixo)
        self.Sobe.clicked.connect(self.vaicima)
        self.pushButton.clicked.connect(self.deletaobjeto)
        self.rotacionaesquerda.clicked.connect(self.rotacionaesq)
        self.rotacionadireita.clicked.connect(self.rotacionadir)
        self.cliparObjetos.clicked.connect(self.ativaclip)
        self.algo1.clicked.connect(self.trocaAlgo1)
        self.algo2.clicked.connect(self.trocaAlgo2)

        #self.Listaobjetos.itemSelectionChanged.connect(self.Marcaselecionado)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #passa ponto x,y da window para viewport
    def transf(self,x,y):
        nx = ((x - self.window.xwmin)/(self.window.xwmax - self.window.xwmin))*(self.vpmaxx - self.vpminx)
        ny = (1-((y - self.window.ywmin)/(self.window.ywmax - self.window.ywmin)))*(self.vpmaxy - self.vpminy)
        return (nx,ny)

    def transfponto(self,ponto):
        x = ponto.x
        y = ponto.y
        z = ponto.z
        nx,ny = self.transf(x,y)
        p = Ponto(nx,ny,z)
        return p 


    def windowparaviewport(self):
        #passa todos os pontos para as coordenadas da viewport
        for ponto in self.pontoswindow:
            p = self.transfponto(ponto[0])
            obj = []
            obj.append(p)
            obj.append(ponto[1])
            self.pontosvp.append(obj)

        #passa os pontos da reta para o sistema de coordenadas de viewport
        for reta in self.retaswindow:
            r = Reta()
            for ponto in reta[0].pontos:
                p = self.transfponto(ponto)
                r.addponto(p)
            obj = []
            obj.append(r)
            obj.append(reta[1])
            self.retasvp.append(obj)

        #passa os pontos do poligono para o sistema de coordenadas de viewport
        for pol in self.poligonoswindow:
            po = Poligono()
            for ponto in pol[0].pontos:
                p = self.transfponto(ponto)
                po.addponto(p)
            obj = []
            obj.append(po)
            obj.append(pol[1])
            self.poligonosvp.append(obj)
            

    #coloca os pontos na graphic view
    def paraviewport(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        #coloca os objetos na graphics view
        bluepen = QtGui.QPen(QtCore.Qt.blue)
        bluepen.setWidth(3)
        for ponto in self.pontosvp:
            p = ponto[0]
            x = int(p.x)
            y = int(p.y)

            #clipa ponto
            if self.CLIPAR == True:
                c = codigo(x,y,self.vpminx,self.vpmaxx,self.vpminy,self.vpmaxy) 
                if c == 0:
                    elipse = self.cena.addEllipse(x,y, 2, 2, bluepen)
                    item = QtWidgets.QListWidgetItem()
                    item.setText(ponto[1])
                    self.Listaobjetos.addItem(item)
            else:
                elipse = self.cena.addEllipse(x,y, 2, 2, bluepen)
                item = QtWidgets.QListWidgetItem()
                item.setText(ponto[1])
                self.Listaobjetos.addItem(item)

        redpen = QtGui.QPen(QtCore.Qt.red)
        for reta in self.retasvp:
            p = []
            for ponto in reta[0].pontos:
                x = int(ponto.x)
                y = int(ponto.y)
                p.append(x)
                p.append(y)

            #clipa reta:
            a,b = cohen_sutherland(p[0],p[1],p[2],p[3],self.vpminx,self.vpmaxx,self.vpminy,self.vpmaxy)
            if self.CLIPAR == True:
                if a[0] != float('inf'):
                    reta1 = self.cena.addLine(a[0],a[1],b[0],b[1],redpen)
                    item = QtWidgets.QListWidgetItem()
                    item.setText(reta[1])
                    self.Listaobjetos.addItem(item)
            else:
                reta1 = self.cena.addLine(p[0],p[1],p[2],p[3],redpen)
                item = QtWidgets.QListWidgetItem()
                item.setText(reta[1])
                self.Listaobjetos.addItem(item)

        
        blackpen = QtGui.QPen()
        for poligono in self.poligonosvp:
    
            pol = []
            for ponto in poligono[0].pontos:
                pol.append(ponto)

            #clipa poligono:
            if self.CLIPAR == True:
                                
                polygon = []
                # for i in range(len(pol)):
                #     p = Ponto(0.0,0.0,0.0)
                #     polygon.append(p)
                tam_poligono = len(pol)

                for i in range(len(pol)):
                    polygon.append(pol[i])
                
                janela = []
                # for i in range(len(pol)):
                #     p = Ponto(0.0,0.0,0.0)
                #     janela.append(p)

                tam_janela = 4
                #janela[0] = Ponto(float(self.vpminx),float(self.vpminy),0.0)
                janela.append(Ponto(float(self.vpminx),float(self.vpminy),0.0))
                # janela[1] = Ponto(float(self.vpminx),float(self.vpmaxy),0.0)
                janela.append(Ponto(float(self.vpminx),float(self.vpmaxy),0.0))
                # janela[2] = Ponto(float(self.vpmaxx),float(self.vpmaxy),0.0)
                janela.append(Ponto(float(self.vpmaxx),float(self.vpmaxy),0.0))
                # janela[3] = Ponto(float(self.vpmaxx),float(self.vpminy),0.0)
                janela.append(Ponto(float(self.vpmaxx),float(self.vpminy),0.0))
                #ordena pontos do poligono em sentido horário
                #polygon = polygon[0:tam_poligono]

                polygon = ordenaSentidoHorario(polygon)
                
                
                # print("antes de clipar:",end = "")
                # for i in range(len(polygon)):
                #     print("(",polygon[i].x,",",polygon[i].y,")",end = "")
                # print("\n")

                if self.algoritmo1 == True:
                    polygon,tam_poligono = sutherland_hodgman(polygon,tam_poligono,janela,tam_janela)
                else:
                    polygon = clipaPoligonos(polygon,self.vpminx,self.vpmaxx,self.vpminy,self.vpmaxy)

                
                tam_poligono = len(polygon)
                if tam_poligono < 1:continue
                #polygon = polygon[0:tam_poligono]
                # print("apos clipagem:",end = "")
                # for i in range(tam_poligono):
                #     print("(",polygon[i].x,',',polygon[i].y,')',end = "")
                # print("TAMANHO DO POLIGONO:",tam_poligono)
                for i in range(0,tam_poligono-1):
                    poligono1 = self.cena.addLine(int(polygon[i].x),int(polygon[i].y),int(polygon[i+1].x),int(polygon[i+1].y),blackpen)
                poligono1 = self.cena.addLine(int(polygon[(tam_poligono)-1].x),int(polygon[(tam_poligono)-1].y),int(polygon[0].x),int(polygon[0].y),blackpen)
            else:
                for i in range(0,len(pol)-1):
                    poligono1 = self.cena.addLine(int(pol[i].x),int(pol[i].y),int(pol[i+1].x),int(pol[i+1].y),blackpen)
                poligono1 = self.cena.addLine(int(pol[len(pol)-1].x),int(pol[len(pol)-1].y),int(pol[0].x),int(pol[0].y),blackpen)
            
            item = QtWidgets.QListWidgetItem()
            item.setText(poligono[1])
            self.Listaobjetos.addItem(item)
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)


    def Addponto(self):
        txt = self.Inputponto.toPlainText()
        self.Inputponto.setPlainText("")
        txt = txt.replace(" ","")
        num1 = ""
        idx = 1
        while txt[idx] != ',':
            num1 += txt[idx]
            idx = idx + 1
        x = float(num1)
        idx = idx + 1
        num2 = ""
        while txt[idx] != ')':
            num2 += txt[idx]
            idx = idx + 1
        y = float(num2)
        print(num1,' ',num2)
        ponto = Ponto(float(x),float(y),0.0)
        obj = []
        obj.append(ponto)
        obj.append("ponto {}".format(self.contadorpontos))
        self.contadorpontos = self.contadorpontos + 1
        self.pontoswindow.append(obj)
        self.Listaobjetos.clear()
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []
        self.windowparaviewport()
        self.paraviewport()

        # bluepen = QtGui.QPen(QtCore.Qt.blue)
        # bluepen.setWidth(3)
        # elipse = self.cena.addEllipse(x,y, 2, 2, bluepen)


    def addreta(self):
        txt = self.Inputreta.toPlainText()
        self.Inputreta.setPlainText("")
        txt = txt.replace(" ","")
        num1 = ""
        idx = 1
        p = []
        while idx < len(txt):
            num = ""
            while txt[idx] != ',':
                num += txt[idx]
                idx = idx + 1
            p.append(int(num))
            idx = idx + 1
            num = ""
            while txt[idx] != ')':
                num += txt[idx]
                idx = idx + 1
            p.append(int(num))
            idx += 2
        
        reta = Reta()
        p1 = Ponto(float(p[0]),float(p[1]),0.0)
        p2 = Ponto(float(p[2]),float(p[3]),0.0)
        reta.addponto(p1)
        reta.addponto(p2)
        obj = []
        obj.append(reta)
        obj.append("reta {}".format(self.contadorretas))
        self.contadorretas+=1
        self.retaswindow.append(obj)
        self.Listaobjetos.clear()
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []
        self.windowparaviewport()
        self.paraviewport()


    def addpoligono(self):
        txt = self.Inputpoligono.toPlainText()
        self.Inputpoligono .setPlainText("")
        txt = txt.replace(" ","")
        num1 = ""
        idx = 1
        p = []
        while idx < len(txt):
            num = ""
            while txt[idx] != ',':
                num += txt[idx]
                idx = idx + 1
            p.append(int(num))
            idx = idx + 1
            num = ""
            while txt[idx] != ')':
                num += txt[idx]
                idx = idx + 1
            p.append(int(num))
            idx += 2
        
        
        
        poligono = Poligono()
        for i in range(0,len(p) - 1,2):
            p1 = Ponto(float(p[i]),float(p[i+1]),0.0)
            poligono.addponto(p1)
        obj = []
        obj.append(poligono)
        obj.append("poligono {}".format(self.contadorpoligonos))
        self.contadorpoligonos+=1
        self.poligonoswindow.append(obj)
        self.Listaobjetos.clear()
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []
        self.windowparaviewport()
        self.paraviewport()

    #multiplica duas matrizes
    def matmul(self,A, B):
        result = []
        for m in range(0, len(A)): 
            rows = []
            for i in range(0, len(B[0])): 
                columns = 0
                for j in range (0, len(B)): 
                    columns += A[m][j] * B[j][i]
                rows.append(columns) 
            result.append(rows) 
        return result


    def maisescala(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

        #matrix de escala
        mat = [ [1.1 , 0 , 0],[0 , 1.1 , 0], [0 , 0 , 1]]
        matpontos = []

        for ponto in self.pontoswindow:
            matpontos = [ [ponto[0].x],[ponto[0].y],[1]]
            r = self.matmul(mat,matpontos)
            ponto[0].x = r[0][0]
            ponto[0].y = r[1][0]

        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]    

        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()


    def menosescala(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

        #matrix de escala
        mat = [ [0.9 , 0 , 0],[0 , 0.9 , 0], [0 , 0 , 1]]
        matpontos = []

        for ponto in self.pontoswindow:
            matpontos = [ [ponto[0].x],[ponto[0].y],[1]]
            r = self.matmul(mat,matpontos)
            ponto[0].x = r[0][0]
            ponto[0].y = r[1][0]

        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]    

        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()

    
    #rotaciona para a window para a esquerda
    def rotacionaesq(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)
        mat = [ [math.cos(-0.1), -math.sin(-0.1),0],[math.sin(-0.1),math.cos(-0.1),0],[0,0,1]]
        matpontos = []
        for ponto in self.pontoswindow:
            matpontos = [ [ponto[0].x],[ponto[0].y],[1]]
            r = self.matmul(mat,matpontos)
            ponto[0].x = r[0][0]
            ponto[0].y = r[1][0]

        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]    

        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()


    #rotaciona para a window para a diretia
    def rotacionadir(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)
        mat = [ [math.cos(0.1), -math.sin(0.1),0],[math.sin(0.1),math.cos(0.1),0],[0,0,1]]
        matpontos = []
        for ponto in self.pontoswindow:
            matpontos = [ [ponto[0].x],[ponto[0].y],[1]]
            r = self.matmul(mat,matpontos)
            ponto[0].x = r[0][0]
            ponto[0].y = r[1][0]

        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                matpontos = [[ponto.x],[ponto.y],[1]]
                r = self.matmul(mat,matpontos)
                ponto.x = r[0][0]
                ponto.y = r[1][0]    

        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()



    def vaiesquerda(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

        for ponto in self.pontoswindow:
            ponto[0].x = ponto[0].x - 0.1
        
        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                ponto.x = ponto.x - 0.1
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                ponto.x = ponto.x - 0.1
        
        
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()
    
    def atualizacena(self):
        self.cena.clear()
        #coloca os objetos na graphics view
        bluepen = QtGui.QPen(QtCore.Qt.blue)
        bluepen.setWidth(3)
        for ponto in self.pontosvp:
            p = ponto[0]
            x = int(p.x)
            y = int(p.y)

            #clipa ponto
            if self.CLIPAR == True:
                c = codigo(x,y,self.vpminx,self.vpmaxx,self.vpminy,self.vpmaxy) 
                if c == 0:
                    elipse = self.cena.addEllipse(x,y, 2, 2, bluepen)
            else:
                elipse = self.cena.addEllipse(x,y, 2, 2, bluepen)

        redpen = QtGui.QPen(QtCore.Qt.red)
        for reta in self.retasvp:
            p = []
            for ponto in reta[0].pontos:
                x = int(ponto.x)
                y = int(ponto.y)
                p.append(x)
                p.append(y)

            #clipa reta:
            a,b = cohen_sutherland(p[0],p[1],p[2],p[3],self.vpminx,self.vpmaxx,self.vpminy,self.vpmaxy)
            if self.CLIPAR == True:
                if a[0] != float('inf'):
                    reta1 = self.cena.addLine(a[0],a[1],b[0],b[1],redpen)
            else:
                reta1 = self.cena.addLine(p[0],p[1],p[2],p[3],redpen)


        
        blackpen = QtGui.QPen()
        for poligono in self.poligonosvp:
    
            pol = []
            for ponto in poligono[0].pontos:
                pol.append(ponto)

            #clipa poligono:
            if self.CLIPAR == True:
                                
                polygon = []
                tam_poligono = len(pol)

                for i in range(len(pol)):
                    polygon.append(pol[i])
                
                janela = []

                tam_janela = 4
                #janela[0] = Ponto(float(self.vpminx),float(self.vpminy),0.0)
                janela.append(Ponto(float(self.vpminx),float(self.vpminy),0.0))
                # janela[1] = Ponto(float(self.vpminx),float(self.vpmaxy),0.0)
                janela.append(Ponto(float(self.vpminx),float(self.vpmaxy),0.0))
                # janela[2] = Ponto(float(self.vpmaxx),float(self.vpmaxy),0.0)
                janela.append(Ponto(float(self.vpmaxx),float(self.vpmaxy),0.0))
                # janela[3] = Ponto(float(self.vpmaxx),float(self.vpminy),0.0)
                janela.append(Ponto(float(self.vpmaxx),float(self.vpminy),0.0))
                #ordena pontos do poligono em sentido horário
                #polygon = polygon[0:tam_poligono]

                polygon = ordenaSentidoHorario(polygon)
                

                if self.algoritmo1 == True:
                    polygon,tam_poligono = sutherland_hodgman(polygon,tam_poligono,janela,tam_janela)
                else:
                    polygon = clipaPoligonos(polygon,self.vpminx,self.vpmaxx,self.vpminy,self.vpmaxy)

                
                tam_poligono = len(polygon)
                if tam_poligono < 1:continue

                for i in range(0,tam_poligono-1):
                    poligono1 = self.cena.addLine((polygon[i].x),(polygon[i].y),(polygon[i+1].x),(polygon[i+1].y),blackpen)
                poligono1 = self.cena.addLine((polygon[(tam_poligono)-1].x),(polygon[(tam_poligono)-1].y),(polygon[0].x),(polygon[0].y),blackpen)
            else:
                for i in range(0,len(pol)-1):
                    poligono1 = self.cena.addLine((pol[i].x),(pol[i].y),(pol[i+1].x),(pol[i+1].y),blackpen)
                poligono1 = self.cena.addLine((pol[len(pol)-1].x),(pol[len(pol)-1].y),(pol[0].x),(pol[0].y),blackpen)
            
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)
            
    
    def vaidireita(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

        for ponto in self.pontoswindow:
            ponto[0].x = ponto[0].x + 0.1
        
        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                ponto.x = ponto.x + 0.1
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                ponto.x = ponto.x + 0.1
        
        
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()

    
    def vaibaixo(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

        for ponto in self.pontoswindow:
            ponto[0].y = ponto[0].y - 0.1
        
        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                ponto.y = ponto.y - 0.1
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                ponto.y = ponto.y - 0.1
        
        
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()


    def vaicima(self):
        self.cena.clear()
        self.Listaobjetos.clear()
        caneta = QtGui.QPen(QtCore.Qt.green)
        bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
        bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
        bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
        bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

        for ponto in self.pontoswindow:
            ponto[0].y = ponto[0].y + 0.1
        
        for reta in self.retaswindow:
            for ponto in reta[0].pontos:
                ponto.y = ponto.y + 0.1
        
        for poligono in self.poligonoswindow:
            for ponto in poligono[0].pontos:
                ponto.y = ponto.y + 0.1
        
        
        self.pontosvp = []
        self.retasvp = []
        self.poligonosvp = []

        self.windowparaviewport()
        self.paraviewport()


    def deletaobjeto(self):
        selecionado = self.Listaobjetos.currentItem()
        if selecionado is not None:
            nome = selecionado.text()
            idx = 0
            if nome[0] == 'r':
                
                for reta in self.retaswindow:
                    if reta[1] == nome:
                        break
                    else:
                        idx+=1

                self.retaswindow.pop(idx)

            elif nome[0:5] == 'ponto':
                
                for ponto in self.pontoswindow:
                    if ponto[1] == nome:
                        break
                    else:
                        idx+=1

                self.pontoswindow.pop(idx)
            else:
                
                for pol in self.poligonoswindow:
                    if pol[1] == nome:
                        break
                    else:
                        idx+=1
                
                self.poligonoswindow.pop(idx)

            self.cena.clear()
            self.pontosvp = []
            self.retasvp = []
            self.poligonosvp = []

            self.Listaobjetos.clear()
            caneta = QtGui.QPen(QtCore.Qt.green)
            bordaesquerda = self.cena.addLine(self.vpminx,self.vpminy,self.vpminx,self.vpmaxy,caneta)
            bordabaixo = self.cena.addLine(self.vpminx,self.vpminy,self.vpmaxx,self.vpminy,caneta)
            bordadireita = self.cena.addLine(self.vpmaxx,self.vpminy,self.vpmaxx,self.vpmaxy,caneta)
            bordacima = self.cena.addLine(self.vpminx,self.vpmaxy,self.vpmaxx,self.vpmaxy,caneta)

            self.windowparaviewport()
            self.paraviewport()

    def ativaclip(self):
        if self.cliparObjetos.isChecked():
            self.CLIPAR = True
        else: self.CLIPAR = False  
        self.windowparaviewport()
        self.atualizacena()
    
    def trocaAlgo1(self):
        self.algoritmo1 = True
        self.algo1.setText("SutherlandHodgman(selecionado)")
        self.algo2.setText("ClipaPoligonos")

    def trocaAlgo2(self):
        self.Algoritmo1 = False
        self.algo1.setText("SutherlandHodgman")
        self.algo2.setText("ClipaPoligonos(selecionado)")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Labelobjetos.setText(_translate("MainWindow", "Objetos:"))
        self.Aumentaescala.setText(_translate("MainWindow", "Zoom out"))
        self.Diminuiescala.setText(_translate("MainWindow", "Zoom in"))
        self.Labelviewport.setText(_translate("MainWindow", "Viewport"))
        self.Sobe.setText(_translate("MainWindow", "↑"))
        self.Esquerda.setText(_translate("MainWindow", "←"))
        self.Direita.setText(_translate("MainWindow", "→"))
        self.Desce.setText(_translate("MainWindow", "↓"))
        self.Botaoaddponto.setText(_translate("MainWindow", "Add Ponto"))
        self.Botaoaddreta.setText(_translate("MainWindow", "Add reta"))
        self.Botaoaddpoligono.setText(_translate("MainWindow", "Add poligono"))
        self.pushButton.setText(_translate("MainWindow", "Deletar objeto"))
        self.rotacionaesquerda.setText(_translate("MainWindow", "↺"))
        self.rotacionadireita.setText(_translate("MainWindow", "↻"))
        self.cliparObjetos.setText(_translate("MainWindow", "Clipar objetos"))
        self.label.setText(_translate("MainWindow", "Algoritmo de Clipagem:"))
        self.mensagemalgo.setText(_translate("MainWindow", "Algoritmo criado utilizando\n"
" o algoritmo cohen-sutherland\n"
" para clipagem de retas  "))
        self.algo1.setText(_translate("MainWindow", "SutherlandHodgman(selecionado)"))
        self.algo2.setText(_translate("MainWindow", "ClipaPoligonos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
