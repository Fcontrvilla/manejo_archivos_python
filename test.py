
"""
file = open("archivo.txt", "r" , encoding="utf-8")
for linea in file:
    print(linea)
file.close()


file = open("archivo.txt", "r", encoding = "utf-8")
lineas = file.readline()
print

"""
import time
import datetime




try:
    edad = int(input("ingrese la edad"))
except Exception as e:
    with open(f"error.log", "w", encoding = "utf-8") as log:
        #log.write(f"el error es:{e}")
        log.write(f"el error es:{round(time.time())}, {e}\n")
    