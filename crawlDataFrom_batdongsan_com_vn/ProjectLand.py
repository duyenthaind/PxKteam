class ProjectLand:

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
        self.description = ''
        self.facade = ''
        self.wayIn = ''
        self.nameProject = ''
        self.keyWords = []
        self.address = ''
        self.size = ''

    def information(self):
        return f'''{self.date} - {self.images} - {self.acreage} - {self.contact} - {self.location} - \
{self.investor} - {self.juridical} - {self.price}
        '''
