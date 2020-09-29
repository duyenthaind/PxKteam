import re


def getDate(soup):
    return soup.find('span', class_="sp3").text


def getTileProduct(soup):
    return soup.find('h1', class_="tile-product").text.strip()


def getDescription(soup):
    return soup.find('div', class_="des-product").text.strip()


def addAttributesToObject(soup, object):
    try: object.date = getDate(soup)
    except: pass
    try: object.tileProduct = getTileProduct(soup)
    except: pass
    try: object.description = getDescription(soup)
    except: pass
    try: object.keyWords = getKeyWords(soup)
    except: pass
    try: object.images = getImages(soup)
    except: pass

    row1s = soup.find_all('div', class_="row-1")
    for row1 in row1s:
        if row1.find('span', class_="r1").text == 'Địa chỉ:':
            try: object.address = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Nội thất:':
            try: object.furniture = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Pháp lý:':
            try: object.juridical = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Chủ đầu tư:':
            try: object.investor = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Hướng nhà:':
            try: object.directionHome = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Hướng ban công:':
            try: object.directionBalcony = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Số phòng ngủ:':
            try: object.numBedroom = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Số toilet:':
            try: object.numBathroom = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Mặt tiền:':
            try: object.facade = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Đường vào:':
            try: object.wayIn = row1.find('span', class_="r2").text
            except: pass
        elif row1.find('span', class_="r1").text == 'Tên dự án:':
            try: object.nameProject = row1.find('span', class_="r2").text.strip()
            except: pass
        elif row1.find('span', class_="r1").text == 'Quy mô:':
            try: object.size = row1.find('span', class_="r2").text.strip()
            except: pass

    lis = soup.find('ul', class_="short-detail-2 clearfix pad-16").find_all('li')
    for li in lis:
        if li.find('span', class_="sp1").text == 'Mức giá:':
            try: object.price = li.find('span', class_="sp2").text
            except: pass
        elif li.find('span', class_="sp1").text == 'Diện tích:':
            try: object.acreage = li.find('span', class_="sp2").text
            except: pass

    phoneNumber = re.compile(r'''(\d{10})[0-9]?''', re.VERBOSE)
    try: object.contact = phoneNumber.findall(object.description)
    except: pass

    return object


def getKeyWords(soup):
    keyWords = soup.find('ul', class_="ul-round clearfix").find_all('li')
    for i in range(len(keyWords)):
        keyWords[i] = keyWords[i].text
    return keyWords


def getImages(soup):
    images = soup.find_all('div', style="margin-right: 8px;")
    for i in range(len(images)):
        images[i] = images[i].find('img').get('src-lazy')
    return images
