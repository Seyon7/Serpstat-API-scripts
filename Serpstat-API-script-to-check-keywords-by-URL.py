from requests_html import HTMLSession

session = HTMLSession()
pages = []


def read_func(filename):
    with open(filename, 'r') as url_list:
        temp_list = url_list.readlines()
        for url in temp_list:
            url = str(url)[:-2]
            pages.append(url)


read_func('urls')

method = 'url_keywords'
token = 'de1fa4769e26a8e9556d63de12e69fec'
search_engine = 'g_ua'

num = len(pages)
elem = 0

with open('result.txt', 'a') as file:
    while num != elem:
        page = pages[elem]
        api_url = f'http://api.serpstat.com/v3/{method}?query={page}&token={token}&se={search_engine}'
        response = session.get(api_url)
        data = response.json()
        try:
            print(page + "\t" + str(data['result']['total']))
            file.write(page + ";" + str(data['result']['total']) + "\n")
        except KeyError:
            print(page + '\t' + '0')
            file.write(page + ';' + "0" + '\n')
        elem = elem + 1

