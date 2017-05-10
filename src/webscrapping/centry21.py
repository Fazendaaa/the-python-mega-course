"""Webscrapping centry21 website"""
# pylint: disable=multiple-imports
import requests, pandas
from bs4 import BeautifulSoup

BASE_URL = 'http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='
REQ = requests.get(BASE_URL+'0.html')
SOUP = BeautifulSoup(REQ.content, 'html.parser')
N_PAGE = int(SOUP.find_all('a', {'class': 'Page'})[-1].text)
ARRAY = []

for page in range(0, 10*N_PAGE, 10):
    REQ = requests.get(BASE_URL+str(page)+'.html')
    SOUP = BeautifulSoup(REQ.content, 'html.parser')
    ALL = SOUP.find_all('div', {'class': 'propertyRow'})

    for item in ALL:
        dic = {}

        try:
            dic['Price'] = item.find('h4', {'class': 'propPrice'}).text.strip()
        # pylint: disable=broad-except
        except Exception:
            dic['Price'] = None

        try:
            addresses = item.find_all('span', {'class': 'propAddressCollapse'})
            dic['Address'] = addresses[0].text
            dic['Locality'] = addresses[1].text
        # pylint: disable=broad-except
        except Exception:
            dic['Address'] = None
            dic['Locality'] = None

        try:
            dic['Beds'] = item.find('span', {'class': 'infoBed'}).find('b').text
        # pylint: disable=broad-except
        except Exception:
            dic['Beds'] = None

        try:
            dic['Area'] = item.find('span', {'class': 'infoSqFt'}).find('b').text
        # pylint: disable=broad-except
        except Exception:
            dic['Area'] = None

        try:
            dic['Full Baths'] = item.find('span', {'class': 'infoValueFullBath'}).find('b').text
        # pylint: disable=broad-except
        except Exception:
            dic['Full Baths'] = None

        try:
            dic['Half Baths'] = item.find('span', {'class': 'infoValueHalfBath'}).find('b').text
        # pylint: disable=broad-except
        except Exception:
            dic['Half Baths'] = None

        for column in item.find_all('div', {'class': 'columnGroup'}):
            feature_gp = column.find_all('span', {'class': 'featureGroup'})
            feature_nm = column.find_all('span', {'class': 'featureName'})
            for group, name in zip(feature_gp, feature_nm):
                dic['Lot Size'] = (name.text.replace(',', '') if 'Lot Size' in group.text else None)

        ARRAY.append(dic)

DF = pandas.DataFrame(ARRAY)
DF.to_csv('../output/centry21.csv')
