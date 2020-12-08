from xml.dom import minidom

DOMTree = minidom.parse("cars.xml")
collection = DOMTree.documentElement

cars = collection.getElementsByTagName("car")

for car in cars:
    name = car.getElementsByTagName("name")[0]
    print("Nazwa samochodu : ", name.childNodes[0].data)
    year = car.getElementsByTagName("year")[0]
    print("Rok produkcji : ", year.childNodes[0].data)
    color = car.getElementsByTagName("color")[0]
    print("Kolor samochodu : ", color.childNodes[0].data, "\n")
