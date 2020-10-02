from crawlDataFrom_batdongsan_com_vn.functionCrawl import *

url = 'https://batdongsan.com.vn/ban-dat-nen-du-an-duong-vanh-dai-3-5-xa-van-canh-1-prj-khu-do-thi-van-canh/-dich-vu-4-5-ha-3-5-lo-dep-gia-hoi-pr26731587'



page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

print(handlingProjectLand(url).location)





