from bs4 import BeautifulSoup                   
import requests     
from openpyxl import Workbook


url =  "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"


data = requests.get(url).text          #get the url data

soup = BeautifulSoup(data, "html.parser")          #parse the data through beautiful soup to clean it up

table = soup.find('table')                      #find table in the cleaned url

wb=Workbook()                                            # create a workbook object
ws=wb.active                                             # use the active worksheet


for row in table.find_all('tr'):        # in html table row is represented by the tag <tr>

    cols = row.find_all('td')           # in html a column is represented by the tag <td>
    language = cols[1].getText()
    salary = cols[3].getText()
    print("{} ----> {}".format(language, salary))
    ws.append([str(language), str(salary)])


wb.save(r"D:/Programming/Language and salary.xlsx")  
