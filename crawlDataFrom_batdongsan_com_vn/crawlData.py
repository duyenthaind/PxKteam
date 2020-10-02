from crawlDataFrom_batdongsan_com_vn.functionCrawl import *
from crawlDataFrom_batdongsan_com_vn.ProjectLand import ProjectLand
from crawlDataFrom_batdongsan_com_vn.Apartment import Apartment

urlApartmentOfHanoi = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-noi/p'
urlProjectLandsOfHanoi = 'https://batdongsan.com.vn/ban-dat-nen-du-an-ha-noi/p'

links = getAllLinkApartmentsFromBDS_com_vn(endPage=2)

apartments = []

for link in links:
    apartments.append(handlingApartment(link))

for apartment in apartments:
    print(apartment.tileProduct)
