from crawlDataFrom_batdongsan_com_vn.functionCrawl import *
from crawlDataFrom_batdongsan_com_vn.ProjectLand import ProjectLand
from crawlDataFrom_batdongsan_com_vn.Apartment import Apartment

urlApartmentOfHanoi = 'https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-noi/p'
urlProjectLandsOfHanoi = 'https://batdongsan.com.vn/ban-dat-nen-du-an-ha-noi/p'

# getAllLinkProjectLandsFromBDS_com_vn()

a = ProjectLand('20/10/2020', ['link1', 'link2'], 87, '0987654321', 'ha dong', 'VIN', 'yes', 1200000000)
# b = Apartment('20/10/2020', ['link1', 'link2'], 87, '0987654321', 'ha dong', 'VIN', 'yes', 1200000000)
# print(a.description())
# print(b.description())
c = ProjectLand()
print(a.description())
