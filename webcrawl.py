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
 
#tmdb
    def extractBoxOfficeByTMDB(tmdbid):
        boxOfficeResultTMDB = 'N/A'
        try:
            urlTMDB = urllib.request.urlopen('https://www.themoviedb.org/movie/' + 'tmdbid').read()      
#soup = BeautifulSoup(url)
            soup = BeautifulSoup(urlTMDB,'lxml')
            for i in soup.find_all('section', class_='facts left_column'):
                for p_tag in i.find_all('p'):
                    if 'Revenue' in p_tag.text:
                        rev = p_tag.text
                        print(rev)   
                    for x in rev.split()[1].split('$')[1].split(','):
                        boxofficeTMDB += x
                boxOfficeResulTMDB = boxofficeTMDB
        except requests.exceptions.RequestException:
            print ('URL Error')
        
        return boxOfficeResultTMDB
 
    
                        
            