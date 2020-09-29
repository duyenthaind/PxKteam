from crawlDataFrom_batdongsan_com_vn.Apartment import Apartment
from crawlDataFrom_batdongsan_com_vn.ProjectLand import ProjectLand
from crawlDataFrom_batdongsan_com_vn.miniFunction import addAttributesToObject
from bs4 import BeautifulSoup
import urllib.request


def getListLinkApartmentOrProjectLandFromURL(url):
    '''
    :param url: url of the page
    :return: list url of apartments from the page
    '''
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    apartments = soup.find_all('div', class_="vip0 product-item clearfix") + \
                 soup.find_all('div', class_="vip0 vipaddon product-item clearfix") + \
                 soup.find_all('div', class_="vip1 vipaddon product-item clearfix") + \
                 soup.find_all('div', class_="vip1 product-item clearfix") + \
                 soup.find_all('div', class_="vip2 product-item clearfix") + \
                 soup.find_all('div', class_="vip2 vipaddon product-item clearfix") + \
                 soup.find_all('div', class_="vip3 vipaddon product-item clearfix") + \
                 soup.find_all('div', class_="vip3 product-item clearfix") + \
                 soup.find_all('div', class_="vip4 product-item clearfix") + \
                 soup.find_all('div', class_="vip4 vipaddon product-item clearfix") + \
                 soup.find_all('div', class_="vip5 vipaddon product-item clearfix") + \
                 soup.find_all('div', class_="vip5 product-item clearfix")
    for i in range(len(apartments)):
        apartments[i] = 'https://batdongsan.com.vn' + apartments[i].find(class_="product-main").find('a').get('href')
    return apartments


def getAllLinkApartmentsFromBDS_com_vn(urlApartmentOfHanoi='https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-noi/p',
                                       endPage=810):
    '''
    :param endPage:
    :param urlApartmentOfHanoi: default = "https://batdongsan.com.vn/ban-can-ho-chung-cu-ha-noi/p"
    :return: list all links of apartments
    '''

    listLinkApartments = []
    startPage = 1
    while startPage <= endPage:
        try:
            listLinkApartments += getListLinkApartmentOrProjectLandFromURL(urlApartmentOfHanoi
                                                                           + str(startPage))
            startPage += 1
        except:
            continue
    return listLinkApartments


def getAllLinkProjectLandsFromBDS_com_vn(urlProjectLandsOfHanoi='https://batdongsan.com.vn/ban-dat-nen-du-an-ha-noi/p',
                                         endPage=43):
    '''
    :param endPage:
    :param urlApartmentOfHanoi: default = "https://batdongsan.com.vn/ban-dat-nen-du-an-ha-noi/p"
    :return: list all links of project lands
    '''

    listLinkProjectLands = []
    startPage = 1
    while startPage <= endPage:
        try:
            listLinkProjectLands += getListLinkApartmentOrProjectLandFromURL(urlProjectLandsOfHanoi
                                                                             + str(startPage))
            print(len(listLinkProjectLands))
            startPage += 1
        except:
            continue
    return listLinkProjectLands


def handlingApartment(ApartmentUrl):
    '''
    :param ApartmentUrl: url of an apartment
    :return: object Apartment
    '''

    page = urllib.request.urlopen(ApartmentUrl)
    soup = BeautifulSoup(page, 'html.parser')
    apartment = Apartment()
    apartment = addAttributesToObject(soup, apartment)
    return apartment


def handlingProjectLand(ProjectLandUrl):
    '''
    :param ProjectLandUrl: url of a project land
    :return: object ProjectLand
    '''

    page = urllib.request.urlopen(ProjectLandUrl)
    soup = BeautifulSoup(page, 'html.parser')
    projectLand = ProjectLand()
    projectLand = addAttributesToObject(soup, projectLand)
    return projectLand
