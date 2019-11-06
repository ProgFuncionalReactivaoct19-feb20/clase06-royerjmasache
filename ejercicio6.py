"""
	@royerjmasache
	Lectura y manejo de archivos
"""
# Importación de librería csv para lectura de archivos
import csv
# Uso de función para manejar el archivo
def linesDictionary(file):
	return csv.DictReader(file, delimiter="\t")
# Uso de sentencia with para manejar la apertura y cierre del archivo
with open("data/trabajadores.csv") as newFile:
	result = list(linesDictionary(newFile))
	# Uso de filter y función anónima para imprimir las listas con una longitud mayor a 10
	print(list(filter(lambda a: len(list(a.items())[2][1]) > 10, result)))
	# Imprensión de resultados en función de listas ordenadas con uso de sorted, función anónima y split
	print(sorted(result, key = lambda a: list(a.items())[1][1].split("-")[2]))


