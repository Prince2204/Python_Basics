import requests
import bs4

result=requests.get("https://webscraper.io/test-sites/e-commerce/allinone")

print("type of result is: ",type(result))

#print(result.text)
print("Using beautiful soup to format the result")
soup=bs4.BeautifulSoup(result.text,"html.parser")

#print(soup)

paragraphs=soup.select("p")
print(paragraphs[5].getText())