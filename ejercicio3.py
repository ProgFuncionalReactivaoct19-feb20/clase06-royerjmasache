"""
	@royerjmasache
	Manejo de archivos con uso de with
"""
import csv

# Uso de método para leer archivo
def lines(file):
	return csv.reader(file, delimiter=";")
# Uso de with para manejar el archivo
with open("data/data-estudiantes.csv") as newFile:
	print(list(lines(newFile)))
	
