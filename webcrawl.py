import requests
from bs4 import BeautifulSoup

class WebCrawl:
    def extractBoxOfficeByIMDB(imdbid):
        boxOfficeResultIMDB = 'N/A'
        try:
            urlIMDB = 'http://www.imdb.com/title/' + imdbid + '/'
            requestUrlTextIMDB = requests.get(urlIMDB).text
            soup = BeautifulSoup(requestUrlTextIMDB,'lxml')
            # find the div which has Gross:
            for i in soup.find('div', id="titleDetails").find_all('div', class_='txt-block'):
                # Check for Gross: in each div
                if 'Gross:' in i.text:
                    boxofficeIMDB = ''
                    for x in i.text.split()[1].split('$')[1].split(','):
                        boxofficeIMDB += x
                    boxOfficeResultIMDB = boxofficeIMDB
        except requests.exceptions.RequestException:
            print ('URL Error')
        
        return boxOfficeResultIMDB