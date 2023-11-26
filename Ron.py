import requests
from bs4 import BeautifulSoup
import re
import datetime
#from dateutil.relativedelta import relativedelta


URL ="https://m.imdb.com/chart/moviemeter/"

#URL = "https://www.technomarket.bg/"

result = requests.get(URL)
###testing if the HTML is correctly generated
soup = BeautifulSoup(result.text, 'html.parser')
print(soup) 
######################################################
""" 

class Crawler:
        def __init__ (self,url) -> None:
            self.url=url
                
        def get_html(self,url):
            try:
                  r=requests.get(url)
            except requests.Requests(Exception):
                  r=requests.get(url,verify=False)
            except Exception as e:
                  print(f"Cannot get {url}:{str(e)}!")
                  exit(-1)
            r.encoding = "utf-8"
            print(r.text)
            if r.ok:    
                  return(r.text)
            else:
                print("no success response from server")
                exit

                  
        def run(self):
             html=self.get_html(self.url)
             self.scraper = Scraper(html)
            #print(html)


class Scraper:
        def __init__ (self,html):
                self.html=html
                self.soup=BeautifulSoup(html, "html.parser")

        def gettitles(self):
              titleselector = '#listContainerScrollable div.ipc-title'
              divtitles = self.soup.select(titleselector)
              for title in divtitles:
                    print(title)



if __name__=="__main__":
    crawler = Crawler(URL)
    crawler.run()
 """