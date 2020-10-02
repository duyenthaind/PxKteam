class ProjectLand:

    def __init__(self):
        self.tileProduct = ''
        self.date = ''
        self.images = []
        self.acreage = ''
        self.contact = ''
        self.location = [21.0413055419922, 105.732070922852]
        self.investor = ''
        self.juridical = ''
        self.price = ''
        self.description = ''
        self.facade = ''
        self.wayIn = ''
        self.nameProject = ''
        self.keyWords = []
        self.address = ''
        self.size = ''
        self.farCenter = 0

    def information(self):
        return f'''{self.date} - {self.images} - {self.acreage} - {self.contact} - {self.location} - \
{self.investor} - {self.juridical} - {self.price}
        '''
