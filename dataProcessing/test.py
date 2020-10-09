import pandas as pd
import csv

reader = csv.DictReader(open("/Users/khanhkd/Desktop/Github_kieuduykhanh/PxKteam/crawlDataFrom_batdongsan_com_vn/data_crawl_from_web/apartments.csv"))





def dataProcess(reader_csv):
    '''
    clean data
    :param reader_csv:
    :return:
    '''
    apartments = []
    for raw in reader:
        apartments.append(raw)
    for i in range(len(apartments)):
        try: apartments[i]['acreage'] = float(apartments[i]['acreage'].replace(' m²', '').strip())
        except: pass

        try: apartments[i]['facade'] = float(apartments[i]['facade'].replace(' (m)', '').strip())
        except: pass

        try: apartments[i]['wayIn'] = float(apartments[i]['wayIn'].replace(' (m)', '').strip())
        except: pass

        try: apartments[i]['numBathroom'] = float(apartments[i]['numBathroom'].replace(' (phòng)', '').strip())
        except: pass

        try: apartments[i]['numBedroom'] = float(apartments[i]['numBedroom'].replace(' (phòng)', '').strip())
        except: pass

        try:
            if apartments[i]['price'].endswith('tỷ'):
                apartments[i]['price'] = float(apartments[i]['price'].replace('tỷ', '').strip()) * 1000000000
            elif apartments[i]['price'].endswith('triệu/m²'):
                apartments[i]['price'] = float(apartments[i]['price'].replace('triệu/m²', '').strip()) * apartments[i]['acreage'] * 1000000
            elif apartments[i]['price'].endswith('triệu'):
                apartments[i]['price'] = float(apartments[i]['price'].replace('triệu', '').strip()) * 1000000
            elif apartments[i]['price'].lower().strip() == 'thỏa thuận':
                apartments[i]['price'] = ''
        except Exception as exp:
            pass

        try:
            if apartments[i]['directionHome'].lower() == 'đông':
                apartments[i]['directionHome'] = 1
            elif apartments[i]['directionHome'].lower() == 'tây':
                apartments[i]['directionHome'] = 2
            elif apartments[i]['directionHome'].lower() == 'nam':
                apartments[i]['directionHome'] = 3
            elif apartments[i]['directionHome'].lower() == 'bắc':
                apartments[i]['directionHome'] = 4
            elif apartments[i]['directionHome'].lower() == 'tây-bắc':
                apartments[i]['directionHome'] = 5
            elif apartments[i]['directionHome'].lower() == 'đông-bắc':
                apartments[i]['directionHome'] = 6
            elif apartments[i]['directionHome'].lower() == 'tây-nam':
                apartments[i]['directionHome'] = 7
            elif apartments[i]['directionHome'].lower() == 'đông-nam':
                apartments[i]['directionHome'] = 8

        except: pass


    return apartments

# apartments = dataProcess(reader)
#
# df = pd.DataFrame(apartments)
# print(df['nameProject'].unique())
#
# df.to_csv('test.csv')

# test = pd.read_csv('test.csv')
#
# test = test.drop(['Unnamed: 0'], axis=1)
#
# print(test)


# for i in range(len(apartments)):
#     print(apartments[i]['price'], apartments[i]['acreage'])


# a = '2.8 tỷ'
#
# a = float(a.replace('tỷ', '').strip()) * 1000000000
#
# print(a)












dff = pd.read_csv('/Users/khanhkd/Desktop/Github_kieuduykhanh/PxKteam/crawlDataFrom_batdongsan_com_vn/data_crawl_from_web/projectLands.csv')
df = pd.read_csv('/Users/khanhkd/Desktop/Github_kieuduykhanh/PxKteam/crawlDataFrom_batdongsan_com_vn/data_crawl_from_web/apartments.csv')
# print('juridical')
# print(df['juridical'].unique())

print(df.info())



