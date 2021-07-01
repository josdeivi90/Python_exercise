EMPTY = "-"
TORRE = "TORRE"
CABALLO = "CABALLO"
ARFIL = "ARFIL"
PEON = "PEON"
REY = "REY"
REINA = "REINA"
tablero = []

for i in range(8):
    fila = [EMPTY for i in range(8)]
    tablero.append (fila)
    

#Torres
tablero[0][0] = TORRE
tablero[0][7] = TORRE
tablero[7][0] = TORRE
tablero[7][7] = TORRE

#caballos
tablero[0][1] = CABALLO
tablero[0][6] = CABALLO
tablero[7][1] = CABALLO
tablero[7][6] = CABALLO

#Arfiles
tablero[0][2] = ARFIL
tablero[0][5] = ARFIL
tablero[7][2] = ARFIL
tablero[7][5] = ARFIL

#DAMA Y REY
tablero[0][3] = REINA
tablero[0][4] = REY
tablero[7][3] = REY
tablero[7][4] = REINA

#PEONES
for i in range(0,8):
    tablero[1][i] = PEON
    tablero[6][i] = PEON











print(tablero)