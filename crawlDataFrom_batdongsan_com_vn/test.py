from crawlDataFrom_batdongsan_com_vn.functionCrawl import *

url = 'https://batdongsan.com.vn/ban-dat-nen-du-an-duong-vanh-dai-3-5-xa-van-canh-1-prj-khu-do-thi-van-canh/-dich-vu-4-5-ha-3-5-lo-dep-gia-hoi-pr26731587'

import math

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')


def farCenter(location):
    hoankiem = list(map(lambda x: math.radians(x), [21.028889, 105.8525]))
    location = list(map(lambda x: math.radians(x), location))
    return 6378 * math.acos((math.sin(location[0]) * math.sin(hoankiem[0]))
                            + (math.cos(location[0]) * math.cos(hoankiem[0]) * math.cos(hoankiem[1] - location[1])))



location = handlingProjectLand(url).location
print(farCenter(location))




