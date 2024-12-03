class Cochef:
    def __init__(self, modelo, tipo, CV, peso, parMotor, cc, motor, consumo, traccion, cambio, velocidades, precioOg, precioActual, añoFabricacion):
        self.modelo=modelo
        self.tipo=tipo
        self.CV=CV
        self.peso=peso
        self.parMotor=parMotor
        self.cc=cc
        self.motor=motor
        self.consumo=consumo
        self.traccion=traccion
        self.cambio=cambio
        self.velocidades=velocidades
        self.precioOg=precioOg
        self.precioActual=precioActual
        self.añoFabricacion=añoFabricacion
    
    global cont

class CochefHibrido (Cochef):
    def __init__(self, modelo, tipo, CV, peso, parMotor, cc, motor, consumo, traccion, cambio, velocidades, precioOg, precioActual, añoFabricacion, CVsMotor, CVsElectricos, nºBaterias):
        Cochef.__init__(self, modelo, tipo, CV, peso, parMotor, cc, motor, consumo, traccion, cambio, velocidades, precioOg, precioActual, añoFabricacion)
        self.CVsMotor=CVsMotor
        self.CVsElectricos=CVsElectricos
        self.nºBaterias=nºBaterias

