import tkinter as tk 

from CocheTipo import Cochef

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

coche1=Cochef("SF90 Stradale", "Moderno", 1000, 1570, 800, 3990, "V8", "6.1L/100km", "4 ruedas", "Automático", 8, 450000, 450000)
coche2=Cochef("F40", "Clásico", 478, 1254, 577, 2936, "V8", "8.5L/100km", "Trasera", "Manual", 5, 400000, "Entre 2 y 3 millones")
coche3=Cochef("LaFerrari", "Moderno", 963, 1585, 900, 6262, "V12 con sistema KERS", "14.2L/100km", "Trasera", "Automático", 7, "1.300.000", "Entre 2 y 3")
coche4=Cochef("250 GTO", "Clásico", 300, 880, 294, 2953, "V12", "22L/100km", "Trasera", "Manual", 5, 18000, "Más de 65 millones")
coche5=Cochef("812 Competizione", "Moderno", 830, 1487, 692, 6496, "V12", "16.9L/100km", "Trasera", "Automático", 7, 500000, 500000)
coche6=Cochef("Purosangue", "Moderno", 725, 2033, 716, 6496, "V12", "17.3L/100km", "4 ruedas", "Automático", 8, 500000, 500000)
coche7=Cochef("166 inter", "Clásico", 125, 1000, "null", 1995, "V12", "16.7L/100km", "Trasera", "Manual", 5, 13500, "Más de 4 millones")
coche8=Cochef("Roma", "Moderno", 620, 1570, 760, 3855, "V8 biturbo", "10.8L/100km", "Trasera", "Automático", 8, 220000, 300000)
coche9=Cochef("Testarossa", "Clásico", 390, 1470, 490, 4943, "V12", "13.5L/100km", "Trasera", "Manual", 5, 125000, "Entre 50.000 y 150.000")
coche10=Cochef("458", "Moderno", 570, 1380, 540, 4497, "V8", "13.4L/100km", "Trasera", "Manual", 7, 210000, 230000)
coche11=Cochef("488 pista", "Moderno", 760, 1280, 770, 3902, "V8", "11.4L/100km", "Trasera", "Automático", 7, 300000, 350000)


listaCoches=[coche1, coche2, coche3, coche4, coche5, coche6, coche7, coche8, coche9, coche10, coche11]


window = tk.Tk()
window.title("Concesionario")
window.geometry("500x500")

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

lblparMotor=tk.Label(frmInfoCoches, text="Par Motor: ")
lblparMotor.grid(column="1", row="5")
lblparMotorData=tk.Label(frmInfoCoches, text=listaCoches[0].parMotor)
lblparMotorData.grid(column="2", row="5")

lblcc=tk.Label(frmInfoCoches, text="Cilindrada en cc: ")
lblcc.grid(column="1", row="6")
lblccData=tk.Label(frmInfoCoches, text=listaCoches[0].cc)
lblccData.grid(column="2", row="6")

lblmotor=tk.Label(frmInfoCoches, text="Posición del Motor en N/m: ")
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

frmBotones=tk.Frame(window, padx=20, pady=20)
frmBotones.pack()

btnSiguenteCoche=tk.Button(window, text=("Siguiente"), command=siguienteCoche)
btnSiguenteCoche.pack()

window.mainloop()