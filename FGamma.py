#Programa realizado en Python 3.9
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.special

#Definición de variables

bandera = True
bandera2 = True
baja=False
alta=False
rgb=True
grises=False
gam=0.0;
salir=False
path=""
def gamma(rgb,grises,gamma,alta,baja,path):
    if(rgb):
        img = cv2.imread(path)
    if(grises):
        img = cv2.imread(path, 0)
    if(baja):
        gamma=gamma*0.01
    else:
        gamma=(gamma*0.01)+1
    #Formula de transformación Gamma g(x,y) = c f(x,y)γ  c es una constante de bits 0-255
    x = np.array(range(256))
    #c = 255/máximo de (f(x,y)γ)
    c = 255/np.power(255, gamma)
    #y es lo que vamos a graficar
    y =  c * np.power(x, gamma)

    #Definimos valores originales
    gamma1 = 1.0
    c1 = 255/np.power(255, gamma1)
    y1 =  c1 * np.power(x, gamma1)
    #Mostramos la grafica de Corrección
    plt.figure()
    plt.title('Imagen Original vs Correción Gamma')
    plt.plot(x, y, label = '$\gamma = '+str(gamma)+'$')
    plt.plot(x, y1, label = '$\gamma = 1.0$')
    plt.legend(loc='upper left')
    plt.xlabel('Grado Intensidad en Entrada')
    plt.ylabel('Grado Intensidad en Salida')
    plt.show()

    #calculamos la transformacion gamma, con la formulita
    salida = np.array(c * np.power(img, gamma), dtype = 'uint8')

    cv2.imshow('Imagen Modificada = '+str(gamma), salida)
    cv2.imshow('Imagen Original', img)
    cv2.waitKey(0)
    hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist_full)
    plt.title("Histograma Original")
    plt.show()

    hist_full = cv2.calcHist([salida],[0],None,[256],[0,256])
    plt.plot(hist_full)
    plt.title("Histograma Modificado")
    plt.show()
    
    #Evaluamos la funcion gamma con Scipy
    b = str(gamma).split(".")
    entero = int(b[0])
    decimal = int(b[1])
    if(entero==0):
        gamma2=100+(decimal*10)
    else:
        gamma2=(entero*100)+(decimal*10)
    #Imprimimos grafica de funcion gamma
    print(gamma2)
    x = np.linspace(-10, 10, gamma2)
    y = scipy.special.gamma(x)
    plt.figure(num=1)
    plt.title("Grafica F. Gamma")
    plt.plot(x,y,'b-')
    plt.xlim((-10,10))
    plt.ylim((-10,10))
    plt.grid('on')
    plt.show()
    cv2.destroyAllWindows()
    
def menu():
    global salir,path
    while bandera:   
        print ("Aplicación de método F. Gamma para correción gamma de una imagen")
        path=input("Ingrese la ruta de la imagen: ")
        print("---------------------------------------------------------------")
        while bandera2:
            global baja,alta,rgb,grises
            print ("Eliga el trabajo a realizar")
            print ("1-Mejorar Zonas Oscuras RGB")
            print ("2-Mejorar Zonas Oscuras B/N")
            print ("3-Mejorar Zonas Claras RGB")
            print ("4-Mejorar Zonas Claras B/N")
            print ("5-Salir")
            opcion_menu=int(input("Digite su opción:  "))
            if(opcion_menu == 1):
                print("La imagen será tratada en RGB")
                baja=True
                break
            elif(opcion_menu == 2):
                print("La imagen será tratada en escala de grises")
                baja=True
                rgb=False
                grises=True
                break
            elif(opcion_menu == 3):
                print("La imagen será tratada en RGB")
                alta=True
                break
            elif(opcion_menu == 4):
                print("La imagen será tratada en escala de grises")
                alta=True
                rgb=False
                grises=True
                break
            elif(opcion_menu == 5):
                salir=True
                break
            else:
                print("Error, digite una opción válida")
                print("-------------------------------------------")
        if(salir):
            break
        while bandera2:  
            print ("Del 1 al 100, ingrese el valor de Gamma a modificar en la imagen")
            gamm=float(input("Puede tener hasta 2 decimales:  "))
            if(gamm > 100.00):
                print("Error, digite un valor válido")
                print("-------------------------------------------")
            else:
                break
        gamma(rgb,grises,gamm,alta,baja,path)
            
menu()

