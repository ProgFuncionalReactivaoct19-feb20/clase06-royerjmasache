"""
	@royerjmasache
	Manejo de archivo
"""
# Importación de librería
import csv
# Uso de método para leer  el archivo
def linesDictionary(file):
	return csv.DictReader(file, delimiter=";")
# Uso de with para manejar el archivo
with open("data/data-estudiantes.csv") as newFile:
	result = list(linesDictionary(newFile))
	print(list(map(lambda a: "%s %s" % (list(a.items())[0][1].split(" ")[1], list(a.items())[1][1].split(".")[0]), result)))