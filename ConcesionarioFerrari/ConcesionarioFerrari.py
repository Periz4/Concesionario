import tkinter as tk 

from CocheTipo import Cochef
from CocheTipo import CochefHibrido

def siguienteCoche():

    if Cochef.cont < len(listaCoches)-1:
        Cochef.cont=Cochef.cont + 1
    else:
        Cochef.cont=0

    lblModeloData.config(text=listaCoches[Cochef.cont].modelo)
    lblTipoData.config(text=listaCoches[Cochef.cont].tipo)
    lblCVData.config(text=listaCoches[Cochef.cont].CV)
    lblPesoData.config(text=listaCoches[Cochef.cont].peso)
    lblparMotorData.config(text=listaCoches[Cochef.cont].parMotor)
    lblccData.config(text=listaCoches[Cochef.cont].cc)
    lblmotorData.config(text=listaCoches[Cochef.cont].motor)
    lblconsumoData.config(text=listaCoches[Cochef.cont].consumo)
    lblTraccionData.config(text=listaCoches[Cochef.cont].traccion)
    lblcambioData.config(text=listaCoches[Cochef.cont].cambio)
    lblvelocidadesData.config(text=listaCoches[Cochef.cont].velocidades)
    lblprecioOgData.config(text=listaCoches[Cochef.cont].precioOg)
    lblprecioActualData.config(text=listaCoches[Cochef.cont].precioActual)
    lblañoFabricacionData.config(text=listaCoches[Cochef.cont].añoFabricacion)
    if type(listaCoches[Cochef.cont]) == CochefHibrido:
        lblCVsMotorData.config(text=listaCoches[Cochef.cont].CVsMotor)
        lblCVsElectricosData.config(text=listaCoches[Cochef.cont].CVsElectricos)
        lblnºBateriasData.config(text=listaCoches[Cochef.cont].nºBaterias)
    else:
        lblCVsMotorData.config(text="No corresponde")
        lblCVsElectricosData.config(text="No corresponde")
        lblnºBateriasData.config(text="No corresponde")
        


coche1=CochefHibrido("SF90 Stradale", "Moderno", 1000, 1570, 800, 3990, "V8", "6.1L/100km", "4 ruedas", "Automático", 8, "450.000", "450.000", 2019, 780, 220, 1)
coche2=Cochef("F40", "Clásico", 478, 1254, 577, 2936, "V8", "8.5L/100km", "Trasera", "Manual", 5, "400.000", "Entre 2 y 3 millones", 1987)
coche3=Cochef("LaFerrari", "Moderno", 963, 1585, 900, 6262, "V12 con sistema KERS", "14.2L/100km", "Trasera", "Automático", 7, "1.300.000", "Entre 2 y 3 millones", 2013)
coche4=Cochef("250 GTO", "Clásico", 300, 880, 294, 2953, "V12", "22L/100km", "Trasera", "Manual", 5, "18.000", "Más de 65 millones", 1962)
coche5=Cochef("812 Competizione", "Moderno", 830, 1487, 692, 6496, "V12", "16.9L/100km", "Trasera", "Automático", 7, "500.000", "500.000", 2017)
coche6=Cochef("Purosangue", "Moderno", 725, 2033, 716, 6496, "V12", "17.3L/100km", "4 ruedas", "Automático", 8, "500.000", "500.000", 2022)
coche7=Cochef("166 inter", "Clásico", 125, 1000, "No hay datos", 1995, "V12", "16.7L/100km", "Trasera", "Manual", 5, 13500, "Más de 4 millones", 1948)
coche8=Cochef("Roma", "Moderno", 620, 1570, 760, 3855, "V8 biturbo", "10.8L/100km", "Trasera", "Automático", 8, "220.000", "300.000", 2019)
coche9=Cochef("Testarossa", "Clásico", 390, 1470, 490, 4943, "V12", "13.5L/100km", "Trasera", "Manual", 5, "125.000", "Entre 50.000 y 150.000", 1984)
coche10=Cochef("458", "Moderno", 570, 1380, 540, 4497, "V8", "13.4L/100km", "Trasera", "Manual", 7, "210.000", "230.000", 2009)
coche11=Cochef("488 pista", "Moderno", 760, 1280, 770, 3902, "V8", "11.4L/100km", "Trasera", "Automático", 7, "300.000", "350.000", 2015)
coche12=CochefHibrido("296 gtb", "Moderno", 830, 1470, 1055, 2992, "V6", "9.5L/100km", "Trasera", "Automático", 8, "250.000", "270.000", 2022, 663, 167, 1)
Cochef.cont=0

listaCoches=[coche1, coche2, coche3, coche4, coche5, coche6, coche7, coche8, coche9, coche10, coche11, coche12]


window = tk.Tk()
window.title("Concesionario")
window.geometry("500x425")

lblTitulo=tk.Label(window, text="Concesionario Ferrari")
lblTitulo.pack()

frmInfoCoches=tk.Frame(window)
frmInfoCoches.pack()

lblModelo=tk.Label(frmInfoCoches, text="Modelo: ")
lblModelo.grid(column="1", row="1")
lblModeloData=tk.Label(frmInfoCoches, text=listaCoches[0].modelo)
lblModeloData.grid(column="2", row="1")

lblTipo=tk.Label(frmInfoCoches, text="Tipo: ")
lblTipo.grid(column="1", row="2")
lblTipoData=tk.Label(frmInfoCoches, text=listaCoches[0].tipo)
lblTipoData.grid(column="2", row="2")

lblCV=tk.Label(frmInfoCoches, text="Caballos: ")
lblCV.grid(column="1", row="3")
lblCVData=tk.Label(frmInfoCoches, text=listaCoches[0].CV)
lblCVData.grid(column="2", row="3")

lblPeso=tk.Label(frmInfoCoches, text="Peso en kg: ")
lblPeso.grid(column="1", row="4")
lblPesoData=tk.Label(frmInfoCoches, text=listaCoches[0].peso)
lblPesoData.grid(column="2", row="4")

lblparMotor=tk.Label(frmInfoCoches, text="Par Motor en N/m: ")
lblparMotor.grid(column="1", row="5")
lblparMotorData=tk.Label(frmInfoCoches, text=listaCoches[0].parMotor)
lblparMotorData.grid(column="2", row="5")

lblcc=tk.Label(frmInfoCoches, text="Cilindrada en cc: ")
lblcc.grid(column="1", row="6")
lblccData=tk.Label(frmInfoCoches, text=listaCoches[0].cc)
lblccData.grid(column="2", row="6")

lblmotor=tk.Label(frmInfoCoches, text="Posición del Motor: ")
lblmotor.grid(column="1", row="7")
lblmotorData=tk.Label(frmInfoCoches, text=listaCoches[0].motor)
lblmotorData.grid(column="2", row="7")

lblconsumo=tk.Label(frmInfoCoches, text="Consumo: ")
lblconsumo.grid(column="1", row="8")
lblconsumoData=tk.Label(frmInfoCoches, text=listaCoches[0].consumo)
lblconsumoData.grid(column="2", row="8")

lblTraccion=tk.Label(frmInfoCoches, text="Tracción: ")
lblTraccion.grid(column="1", row="9")
lblTraccionData=tk.Label(frmInfoCoches, text=listaCoches[0].traccion)
lblTraccionData.grid(column="2", row="9")

lblcambio=tk.Label(frmInfoCoches, text="Cambio: ")
lblcambio.grid(column="1", row="10")
lblcambioData=tk.Label(frmInfoCoches, text=listaCoches[0].cambio)
lblcambioData.grid(column="2", row="10")

lblvelocidades=tk.Label(frmInfoCoches, text="Velocidades: ")
lblvelocidades.grid(column="1", row="11")
lblvelocidadesData=tk.Label(frmInfoCoches, text=listaCoches[0].velocidades)
lblvelocidadesData.grid(column="2", row="11")

lblprecioOg=tk.Label(frmInfoCoches, text="Precio Original en €: ")
lblprecioOg.grid(column="1", row="12")
lblprecioOgData=tk.Label(frmInfoCoches, text=listaCoches[0].precioOg)
lblprecioOgData.grid(column="2", row="12")

lblprecioActual=tk.Label(frmInfoCoches, text="Precio Actual en €: ")
lblprecioActual.grid(column="1", row="13")
lblprecioActualData=tk.Label(frmInfoCoches, text=listaCoches[0].precioActual)
lblprecioActualData.grid(column="2", row="13")

lblañoFabricacion=tk.Label(frmInfoCoches, text="Se fabricó en: ")
lblañoFabricacion.grid(column="1", row="14")
lblañoFabricacionData=tk.Label(frmInfoCoches, text=listaCoches[0].añoFabricacion)
lblañoFabricacionData.grid(column="2", row="14")

lblCVsMotor=tk.Label(frmInfoCoches, text="CV's de combustión: ")
lblCVsMotor.grid(column="1", row="15")
lblCVsMotorData=tk.Label(frmInfoCoches, text=listaCoches[0].CVsMotor)
lblCVsMotorData.grid(column="2", row="15")

lblCVsElectricos=tk.Label(frmInfoCoches, text="CV's Eléctricos: ")
lblCVsElectricos.grid(column="1", row="16")
lblCVsElectricosData=tk.Label(frmInfoCoches, text=listaCoches[0].CVsElectricos)
lblCVsElectricosData.grid(column="2", row="16")

lblnºBaterias=tk.Label(frmInfoCoches, text="Número de baterías")
lblnºBaterias.grid(column="1", row="17")
lblnºBateriasData=tk.Label(frmInfoCoches, text=listaCoches[0].nºBaterias)
lblnºBateriasData.grid(column="2", row="17")

frmBotones=tk.Frame(window, padx=20, pady=20)
frmBotones.pack()

btnSiguenteCoche=tk.Button(window, text=("Siguiente"), command=siguienteCoche)
btnSiguenteCoche.pack()

window.mainloop()