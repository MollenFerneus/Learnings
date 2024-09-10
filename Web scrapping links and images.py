from bs4 import BeautifulSoup                   
import requests                            


url = "http://www.ibm.com"

data  = requests.get(url).text 

soup = BeautifulSoup(data,"html.parser")


for link in soup.find_all('a'):                     # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

for link in soup.find_all('img'):                    # in html image is represented by the tag <img>   
    print(link.get('src'))




    
