# importing all the libraries required
# BeautifulSoup package is used to structure the unstructured data
from bs4 import BeautifulSoup
import requests  # requests package is used to get the HTTP response requests
# pandas dataframe is being used to store the data in a dataframe and then move to excel
import pandas as pd
# urlopen package is used to open the url I am going to scrap te data
from urllib.request import urlopen

# Requesting website to download the HTML
url = 'http://csitgeu.in/wp/2021/05/02/notice-mini-project-evaluation-notice-for-4th-and-6th-semester/'
req = requests.get(url)
content = req.text
# printing the entire HTML on the command line
print(content)

# We see the data is not in structured format
# Using beautiful Soup package , we can structure the format using this package

soup = BeautifulSoup(content)
print(soup)

# After getting the structured data from the website in an HTML format, I studied the content and found out that the 6th sem notice
# is stored in a link

# I will repeat the same step to extract the information from the notice board link

url_notice = "http://csitgeu.in/wp/feed/"
req_notice = requests.get(url_notice)
content_notice = req_notice.text

soup_notice = BeautifulSoup(content_notice, "lxml")
print(soup_notice)

print(soup_notice.title.text)

# I am creating the empty output dictionary to store the output. I am extracting the innerText,href and title from the
# website and storing it in the pd(pandas) dataframe
output = []
for link in soup.find_all("a"):
    print("Inner Text: {}".format(link.text))
    HTML_to_table = {}
    HTML_to_table['InnerText'] = "{}".format(link.text)

    print("Title: {}".format(link.get("title")))
    HTML_to_table['Title'] = "{}".format(link.get("title"))

    print("href: {}".format(link.get("href")))
    HTML_to_table['href'] = "{}".format(link.get("href"))

    output.append(HTML_to_table.copy())

print(output)

df = pd.DataFrame(data=output)
print(df)
# moving the data from dataframe to excel for further analysis
df.to_excel('csitWebScrapping.xlsx')
