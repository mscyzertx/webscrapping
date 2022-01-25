from email import header
import imp
from bs4  import BeautifulSoup
import requests

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'}
url='https://www.reddit.com/r/college/'
response=requests.get(url,headers=headers)

# print(response.content)
soup = BeautifulSoup(response.content, 'lxml')

crawl_data = soup.find_all('div', class_= {'_1poyrkZ7g36PawDueRza-J _11R7M_VOgKO1RJyRSRErT3'})


num = 0
for crawl_post in crawl_data:
        title = crawl_post.find('h3')
        num+=1
        print(f"Title{num}", title.text)
    

        description = crawl_post.findAll('p')
        for para in description:
            print(para.text)
            print('\n')