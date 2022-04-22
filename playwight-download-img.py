from playwright.sync_api import sync_playwright
import requests

def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.shutterstock.com/search/sad+cops")
    images = page.query_selector_all("img")
    for i in images:
        alt = i.get_attribute("alt")
        src = i.get_attribute("src")
        if src:
            download_file(src)
    # links = page.query_selector_all("a")
    # for l in links:
    #     print(l.text_content())

    browser.close()