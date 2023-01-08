
from optparse import Values
import scipy.spatial as cg
import PySimpleGUI as com
import tkinter as tk
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class interfaz:

    def __init__(self,ancho,alto):
        #colocación de los atributos de la clase
        self.ancho = ancho
        self.alto = alto
        self.iniciar_interfaz()

        
    def iniciar(self):
        return True
        


    def iniciar_interfaz(self):
        Dim_opc=[0.3*self.ancho,0.3*self.alto]
        Opciones=[
        [com.Frame('Opciones',[[com.Button('Puntos')],
        [com.Button('Graficar')],
        [com.Button('Cascara')],
        [com.Button('Voronoi')],
        [com.Button('Dealunay')],
        [com.Exit('Salir')]]
        ,size=(Dim_opc[0],Dim_opc[1]))]
        ]
        layout=[[com.Column(Opciones)]]
        ventana=com.Window('proyecto Geometria computacional',layout)
        while True:
            event, Values= ventana.read()
            if(event == com.WIN_CLOSED or event == 'Salir'):
                com.popup('Hasta luego')
                break
            else:
                if(event == 'Puntos'):
                    try:
                       #obtención de la cantidad de puntos a realizar operaciones
                       cant_tx=com.popup_get_text("¿Cuantos puntos desea gráficar?")
                       #Conversion de texto a entero
                       cant=(int)(cant_tx)
                       #creación del plano para la colocación de los puntos
                       plt.figure()
                       plt.xlim(0,self.ancho)
                       plt.ylim(0,self.alto)
                       plt.grid(True)
                       plt.title("Selección de puntos")
                       #obtención de los puntos a realizar operaciones
                       pts = np.asarray(plt.ginput(cant, timeout=-1))
                       #print(pts)
                       plt.close()
                       com.popup("Puntos guardados exitosamente")
                       ventana.refresh()
                       
                    except:
                        com.popup("Error al almacenar los datos, intente de nuevo")
                        ventana.refresh()
                elif(event == 'Dealunay'):
                    try:
                        triang=cg.Delaunay(pts)
                        plt.title("Triangulación de Delaunay")
                        plt.xlim(0,self.ancho)
                        plt.ylim(0,self.alto)
                        plt.triplot(pts[:,0],pts[:,1],triang.simplices.copy())
                        plt.plot(pts[:,0],pts[:,1],'o')
                        plt.show()
                        ventana.refresh()
                    except:
                        com.popup("Puntos insuficientes")
                        ventana.refresh()
                elif(event == 'Cascara'):
                    try:
                        plt.title("Cascara convexa")
                        plt.xlim(0,self.ancho)
                        plt.ylim(0,self.alto)
                        cascara=cg.ConvexHull(pts)
                        plt.plot(pts[:,0],pts[:,1],'o')
                        for simplex in cascara.simplices:
                            plt.plot(pts[simplex,0],pts[simplex,1],'k-')
                        plt.show()
                        ventana.refresh()
                    except:
                        com.popup("Puntos insuficientes")
                        ventana.refresh()
                elif(event == 'Voronoi'):
                    try:
                        voron=cg.Voronoi(pts)
                        Figura=cg.voronoi_plot_2d(voron)
                        plt.xlim(0,self.ancho)
                        plt.ylim(0,self.alto)
                        plt.show()
                        ventana.refresh()
                    except:
                        com.popup("Puntos insuficientes")
                        ventana.refresh()
                elif(event == 'Graficar'):
                    try:
                        plt.scatter(pts[:,0],pts[:,1])
                        plt.xlim(0,self.ancho)
                        plt.ylim(0,self.alto)
                        plt.show()
                        ventana.refresh()
                    except:
                        com.popup("No se han seleccionado puntos")
                        ventana.refresh()

                else:
                    com.popup("Error inesperado, cerrando la aplicación")
                    ventana.close()
        ventana.close()
        



def ObtenerDimensiones():
    try:
        dim=tk.Tk()
        ancho=dim.winfo_screenwidth()
        alto=dim.winfo_screenheight()
        return interfaz(ancho,alto)
    except Exception as exc:
        return interfaz(1000,1000)
def main():
    a=ObtenerDimensiones()
    if (a.iniciar()):
        None
    else:
        None

if __name__ != 'main': #se refiere al nombre del archivo
    main()
