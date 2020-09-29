class Apartment:

    def __init__(self):
        self.tileProduct = ''
        self.date = ''
        self.images = []
        self.acreage = ''
        self.contact = ''
        self.location = ''
        self.investor = ''
        self.juridical = ''
        self.price = ''
        self.numBedroom = ''
        self.directionHome = ''
        self.directionBalcony = ''
        self.service = ''
        self.furniture = ''
        self.numBathroom = ''
        self.description = ''
        self.facade = ''
        self.wayIn = ''
        self.nameProject = ''
        self.keyWords = []
        self.address = ''
        self.size = ''

    def information(self):
        return f'''{self.date} - {self.images} - {self.acreage} - {self.contact} - {self.location} - \
{self.investor} - {self.juridical} - {self.price} - {self.numBedroom} - {self.numBathroom} - {self.directionHome} - \
{self.directionBalcony} - {self.service} - {self.furniture}'''