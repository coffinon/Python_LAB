import xml.sax


class CarsHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.name = ""
        self.year = ""
        self.color = ""

    def startElement(self, tag, attributes):
        self.current = tag

    def characters(self, content):
        if self.current == "name":
            self.name = content
            print("Nazwa samochodu : ", self.name)
        elif self.current == "year":
            self.year = content
            print("Rok produkcji : ", self.year)
        elif self.current == "color":
            self.color = content
            print("Kolor samochodu : ", self.color, "\n")

    def endElement(self, name):
        self.current = ""


handler = CarsHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("cars.xml")
