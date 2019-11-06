"""
	@royerjmasache
	Uso de .map para manejar archivo .csv
"""
# Importación de librería csv
import csv
# Método para leer y delimitar el archivo
def lines(file):
	return csv.reader(file, delimiter=";")
# Uso de with para manejar el archivo
with open("data/data-estudiantes.csv") as newFile:
	# Uso de .map para iterar  y filter para filtrar los resultados
	print(list(map(lambda a: a[1], filter(lambda a: a[1] != "email", lines(newFile)))))
