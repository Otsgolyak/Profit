from bs4 import BeautifulSoup
import requests


data = []


def parser (unit):

    page_link = unit
    # fetch the content from url
    page_response = requests.get(page_link, timeout=5)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")
    
    
    # prices = page_content.find_all('a')
    #
    #
    # print(prices)
    f = open('text3.txt', 'a')
    for link in page_content.find_all('h2'):
        data = []
        res = str(link)
        if " - " in  res:
            final = res.split(' - ')
            final = str(final[1])
            final = final.split(' ')
            final = '.'.join(final)
            final = str(final)
            final = final[0:-5]
            # print(final)
            # data = data.append(final)
            # print("data: ", data)
            # print(final)
            f.write('https://' + final + '\n')
    
        else:
            res = res.split("-")
            res = res[2].split(' ')
            res = '.'.join(res)
            res = res[1: -5]
            res = str(res)
            # data += final
            # print ('data:', data)
            # print (res)
            f.write('https://' + res + '\n')

f = open('text2.txt', 'r')
a = f.read()

b = a.split('\n')
print(b)
for i in b:



    parser(i)

