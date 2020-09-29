from crawlDataFrom_batdongsan_com_vn.functionCrawl import *

url = 'https://batdongsan.com.vn/ban-dat-nen-du-an-duong-tay-thang-long-thi-tran-phung-prj-the-phoenix-garden/chinh-chu-can-ban-xay-biet-thu-doi-thong-thephoenix-200m2-mat-tien-10m-nhin-cong-vien-pr27205803'
projectLand = handlingProjectLand(url)

print(projectLand.address)


# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')
#
# print(soup.find('div', class_="des-product").text.strip())

