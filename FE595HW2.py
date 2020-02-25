import os
import pandas as pd
import requests
from bs4 import BeautifulSoup

def save_companys(url):
    for i in range(0,50):
        i = 0
        def save_company(url):
            file_content = requests.get(url).content
            soup = BeautifulSoup(file_content, 'html.parser')
            file_name = soup.select('li')[0].contents[0]
            with open(file_name.replace('Name: ', '') + ".html", "wb") as f:
                f.write(file_content)                
        result = save_company(url)
        results = []
        for result in results:
            if result not in results:
                results.append(result)
                i = i + 1
            else:
                i = i

def find_names(path):
    names = []
    for companys in os.listdir(path):
        if '.html' in companys:
            names.append(companys)
    return(names)

def find_purposes(path):
    def find_purpose(name, path):
        name = open(path + name, 'r')
        for line in name:
            if 'Purpose: ' in line:
                line = line.strip('\n')
                line = line.strip(' ')
                line = line.replace('<li>', '') 
                line = line.replace('Purpose:', '')
                purpose = line.replace('</li>', '')
                return(purpose)
    purposes = [find_purpose(name, path) for name in find_names(path)]
    return(purposes)

if __name__ == "__main__":
    url = 'http://18.207.92.139:8000/random_company'
    path = r'/Users/yuechenjiang/Desktop/FE595/FE595HW2/companys/'
    save_companys(url)
    names = find_names(path)
    purposes = find_purposes(path)   
    companys = pd.DataFrame()
    companys = pd.DataFrame({'Name':names,'Purpose':purposes})
    companys.to_csv("companys.csv",index=False)