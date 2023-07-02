import urllib.parse
import requests

main_api = "https://mapquestapi.com/directions/v2/route?"
key = "b5y2XWKHKVfsjwQTU6HXqWPiprEA2x35"

while True:
    origen = input("Ciudad de Origen (Ingrese S para salir): ")
    if origen == "s":
        break

    destino = input("Ciudad de Destino (Ingrese S para salir): ")
    if destino == "s":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": origen, "to": destino})
    print("URL: " + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("-----------------------------------")
        print("----------------------------------------------")
        print("En dirección desde " + origen + " hasta " + destino)
        print("Tiempo de viaje: " + json_data["route"]["formattedTime"])

        # Cálculo de distancia en kilómetros
        distancia_km = json_data["route"]["distance"] * 1.61
        print("Kilómetros: " + str("{:.1f}".format(distancia_km)))

        # Cálculo de combustible
        combustible_litros = distancia_km / 10
        print("Combustible requerido: " + str("{:.1f}".format(combustible_litros)) + " litros")

        print("----------------------------------------------")
        print("-----------------------------------")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str("{:.1f}".format(each["distance"] * 1.61)) + "km)")
        print("-----------------------------------\n")
