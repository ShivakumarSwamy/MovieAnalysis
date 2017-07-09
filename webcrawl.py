import requests
from bs4 import BeautifulSoup

class WebCrawl:
    # Intialising the boxOfficeResult
    def __init__(self):
        self.boxOfficeResult = 'N/A'
        
    # Web Crawling the IMDB page to get the Box Office  
    def extractBoxOfficeByIMDB(self, imdbid):
        try:
            urlIMDB = 'http://www.imdb.com/title/' + imdbid + '/'
            requestUrlTextIMDB = requests.get(urlIMDB).text
            soup = BeautifulSoup(requestUrlTextIMDB,'lxml')
            
            # check whether div with id 'titleDetails' exists
            if soup.find('div', id="titleDetails") is not None:
                # if exists, find all div with class 'txt-block'
                for div in soup.find('div', id="titleDetails").find_all('div', class_='txt-block'):
                    # Check for Gross: in each div
                    if 'Gross:' in div.text:
                        boxofficeIMDB = ''
                        for x in div.text.split()[1].split('$')[1].split(','):
                            boxofficeIMDB += x
                        self.boxOfficeResult = boxofficeIMDB
            else:
                print ('WARNING......')
                print ('WRONG IMDB ID: ' + imdbid)
                        
        except requests.exceptions.RequestException:
            print ('URL ERROR')
        
        return self.boxOfficeResult
    
    # Web Crawling the TMDB page to get the Box Office
    def extractBoxOfficeByTMDB(self, tmdbid):
        try:
            urlTMDB = 'https://www.themoviedb.org/movie/' + tmdbid
            requestUrlTextTMDB = requests.get(urlTMDB).text
            soup = BeautifulSoup(requestUrlTextTMDB,'lxml')
            
            # check whether section with class 'facts left_column' exists
            if soup.find('section', class_='facts left_column') is not None:
                #if exists, find all the paragraph tags in section
                for paragraphTag in soup.find('section', class_='facts left_column').find_all('p'):
                    # Check for Revenue $ in each paragraph tag
                    if 'Revenue $' in paragraphTag.text:
                        boxofficeTMDB = ''
                        for x in paragraphTag.text.split()[1].split('$')[1].split(','):
                            boxofficeTMDB += x
                        self.boxOfficeResult = boxofficeTMDB
            else:
                print ('WARNING......')
                print ('WRONG TMDB ID: ' + tmdbid)
                
        except requests.exceptions.RequestException:
            print ('URL ERROR')
          
        return self.boxOfficeResult