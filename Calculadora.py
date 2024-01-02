import sys
from PyQt5 import  QtWidgets, uic
from PyQt5.QtCore import *


def obter_numero1():
    try:
        N1=float(Telacalc.N1txt.text())
        return N1
    except ValueError:
        print("Por favor, insira um número valido")

    
def obter_numero2():
    try:
        N2=float(Telacalc.N2txt.text())
        return N2
    except ValueError:
        print("Por favor, insira um número valido")



def RealizarSoma():
    numero1= obter_numero1()
    numero2= obter_numero2()
    if numero1 is not None and numero2 is not None:
        resultado= numero1  + numero2
        Telacalc.Resultado.setText(str(resultado))     
    
def RealizarSub():
    numero1= obter_numero1()
    numero2= obter_numero2()
    resultado= numero1  - numero2
    Telacalc.Resultado.setText(str(resultado))   

def RealizarMult():
    numero1= obter_numero1()
    numero2= obter_numero2()
    resultado= numero1  * numero2
    Telacalc.Resultado.setText(str(resultado))   

def RealizarDiv():
    numero1= obter_numero1()
    numero2= obter_numero2()
    resultado= numero1  / numero2
    Telacalc.Resultado.setText(str(resultado))    





app=QtWidgets.QApplication(sys.argv)

Telacalc=uic.loadUi('Calc.ui')
Telacalc.Somar.clicked.connect(RealizarSoma)
Telacalc.Subtrair.clicked.connect(RealizarSub)
Telacalc.Multiplicar.clicked.connect(RealizarMult)
Telacalc.Dividir.clicked.connect(RealizarDiv)
Telacalc.show()

sys.exit(app.exec_())

    



