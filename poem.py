import requests
from bs4 import BeautifulSoup
import threading

URL = "https://www.aldiwan.net/authers-1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Get the list of authors' URLs
author_urls = []
for i in soup.find_all('div', class_="col-lg-4 col-md-6 col-12 py-3 p-0 p-md-3 float-right d-flex"):
    x = i.find('a')
    y = 'https://www.aldiwan.net/' + x.get('href')
    author_urls.append(y)

print("Total Authors:", len(author_urls))

# Function to scrape author information
def scrape_author_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    div_element = soup.find('div', class_="bet-1 row pt-0 px-5 pb-4 justify-content-center")
    if div_element is not None:
        print("\n-------------------------------")
        h3_elements = div_element.find_all('h3')
        for h3 in h3_elements:
            print(h3.getText())

# Create threads for each author URL
threads = []
for author_url in author_urls:
    thread = threading.Thread(target=scrape_author_info, args=(author_url,))
    thread.start()
    threads.append(thread)
print(threads)
# Wait for all threads to complete
for thread in threads:
    thread.join()
    



# Continue with the rest of the code after all threads have finished