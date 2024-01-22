import requests
from bs4 import BeautifulSoup
import json
import concurrent.futures

def getRequest(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def findAuthURL(soup):
    auth_url_list = []
    for i in soup.find_all('div', class_="col-lg-4 col-md-6 col-12 py-3 p-0 p-md-3 float-right d-flex"):
        x = i.find('a')
        y = 'https://www.aldiwan.net/'+ x.get('href')
        auth_url_list.append(y)
    return auth_url_list

def getPoems(soup, auth_url_list):
    poem_list = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(getRequest, url) for url in auth_url_list]
        for future in concurrent.futures.as_completed(futures):
            try:
                auth_soup = future.result()
                for i in auth_soup.find_all('div', class_="col-sm-12 col-md"):
                    urlElement = i.find('a')
                    poemUrl = 'https://www.aldiwan.net/'+ urlElement.get('href')
                    poem_list.append(poemUrl)
            except Exception as e:
                print(f"Error occurred: {e}")
    return poem_list

def returnPoemInfo(soup):
    poem_info = []
    content = soup.find('div', class_="tips row content mt-3 justify-content-center")
    if content is not None:
        #retrive poem informaiton 
        a = content.find_all('a')
        #retrive auther name
        h2_elements = soup.find('h2', class_="text-center h3 mt-3 mb-0")
        poem_info.append(h2_elements.get_text().strip('\n'))
        for i in a:
            raw_text = i.getText()
            poem_info.append(raw_text)
    return poem_info

def getPoemLines(h4_elements):
    s = ''
    for br in h4_elements:
        raw_text = br.getText()
        bidi_text = ' ' + raw_text
        s += bidi_text + '**'
    return s

def getPoemLines1(h3_elements):
    s = ''
    for h3 in h3_elements:
        raw_text = h3.getText()
        bidi_text = ' ' + raw_text
        s += bidi_text + '**'
    return s

def writePoem(list):
    poem_data = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(getRequest, url): url for url in list}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                soup = future.result()
                div_element = soup.find('div', class_="bet-1 row pt-0 px-5 pb-4 justify-content-center")
                s = ''
                poem_info = returnPoemInfo(soup)
                print("\n-------------------------------")
                h3_elements = div_element.find_all('h3')
                if h3_elements == []:
                    h4_elements = div_element.find('h4')
                    s = getPoemLines(h4_elements)
                else:
                    s = getPoemLines1(h3_elements)

                poem_data.append((s, poem_info))
            except Exception as e:
                print(f"Error occurred while processing URL: {url}. Exception: {e}")

    with open('poemtext', 'a', encoding='utf-8') as file:
        for poem in poem_data:
            poem_dict = {poem[0]: poem[1]}
            json.dump(poem_dict, file)
            file.write('\n')

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, 41):
            URL = f"https://www.aldiwan.net/authers-1?page={i}"
            print(URL)
            soup = getRequest(URL)
            auth_list = findAuthURL(soup)
            future = executor.submit(getPoems, soup, auth_list)
            futures.append(future)
        
        for future in concurrent.futures.as_completed(futures):
            try:
                poem_list = future.result()
                writePoem(poem_list)
            except Exception as e:
                print(f"Error occurred: {e}")

main()
