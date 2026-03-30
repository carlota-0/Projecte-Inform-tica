from airport import *


# Para comprobar la función que comprueba si un aeropuerto es de la zona Schengen o no
'''
airport = Airport ("LEBL", 41.297445, 2.0832941)
print(IsSchengenAirport(airport.ICAO))
'''

# Para comprobar la función que define un aeropuerto de la zona Schengen en la variable
'''
airport = Airport ("LEBL", 41.297445, 2.0832941)
SetSchengen(airport)
print(airport.Schengen)
'''

# Para comprobar la función qur imprimir aeropuertos por consola
'''
airport = Airport ("LEBL", 41.297445, 2.0832941)
print(PrintAirport(airport))
'''

# Para comprobar la función de carga del archivo
'''
file = "Airports.txt"
aeropuertos = LoadAirports(file)
for i in range(len(aeropuertos)):
    print(PrintAirport(aeropuertos[i]))
'''

# Para comprobar la función de guardado de archivos de la zona Schengen
''' 
file = "Airports.txt"
output = "Schengen.txt"
aeropuertos = LoadAirports(file)
a = SaveSchengenAirports(aeropuertos, output)
'''

# Para comprobar la función de añadido de aeropuertos
''' 
file = "Airports.txt"
aeropuertos = LoadAirports(file)
airport = Airport ("LEBL", 41.297445, 2.0832941)
AddAirport(aeropuertos, airport)
print(PrintAirport(aeropuertos[-1]))
'''

# Para comprobar la función de supresión de aeropuertos
'''
file = "Airports.txt"
aeropuertos = LoadAirports(file)
airport = Airport ("LEBL", 41.297445, 2.0832941)
RemoveAirport(aeropuertos, airport.ICAO)
for i in range(len(aeropuertos)):
    print(PrintAirport(aeropuertos[i]))
'''

# Para comprobar la función del grafico de aeropuertos
''' 
file = "Airports.txt"
aeropuertos = LoadAirports(file)
airport = Airport ("LEBL", 41.297445, 2.0832941)
RemoveAirport(aeropuertos, airport.ICAO)
for i in range(len(aeropuertos)):
    print(PrintAirport(aeropuertos[i]))
'''

# Para comprobar la función del arhivo KML
''' 
file = "Airports.txt"
aeropuertos = LoadAirports(file)
MapAirports(aeropuertos)
'''
