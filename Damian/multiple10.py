#calcular el importe de interes
#Declaracion
capital_inicial=0.0
interes_simple=0.0
importe_interes=0.0
import os

#Input
capital_inicial=float(os.sys.argv[1])
interes_simple=float(os.sys.argv[2])

#Processing
importe_interes=capital_inicial*interes_simple

if (importe_interes>0.0):
    print("el importe de interes es:",capital_inicial*interes_simple)
if(importe_interes>0.5):
    print("Muy bajo")
if(importe_interes>0.9):
    print("bajo")
if(importe_interes>1.5):
    print("Regular")
if(importe_interes>1.9):
    print("Bueno")
