import requests
from bs4 import BeautifulSoup

cookies = {
    'session-id': '138-3406418-2441158',
    'ubid-main': '133-7065184-3792526',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'USD',
    'sp-cdn': '"L5Z9:PT"',
    'skin': 'noskin',
    'session-token': 'mPSDkygpnryzvRxz4NsKch3m6waSqaQFWT8FS6WV38sP3nnKfFjOP6mAGkFZS0WH0MjS1U/scLVepZs5XCF1yBTEDIOwCo9brXw9GCXOXbNU8m4vleOYf1fxdpv2oIKHKbpZJUXnGLJuM76Tdu3Z4aqIk/39RPkmmqIymL7uC4O/aXcJi1oc3rqWjtZSgdNA',
    'csm-hit': 'tb:s-QEX3KNWVTZEGQPB64NBK|1649370002566&t:1649370003661&adb:adblk_no',
}

headers = {
    'authority': 'www.amazon.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'session-id=138-3406418-2441158; ubid-main=133-7065184-3792526; session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:PT"; skin=noskin; session-token=mPSDkygpnryzvRxz4NsKch3m6waSqaQFWT8FS6WV38sP3nnKfFjOP6mAGkFZS0WH0MjS1U/scLVepZs5XCF1yBTEDIOwCo9brXw9GCXOXbNU8m4vleOYf1fxdpv2oIKHKbpZJUXnGLJuM76Tdu3Z4aqIk/39RPkmmqIymL7uC4O/aXcJi1oc3rqWjtZSgdNA; csm-hit=tb:s-QEX3KNWVTZEGQPB64NBK|1649370002566&t:1649370003661&adb:adblk_no',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '2',
    'ect': '4g',
    'referer': 'https://www.amazon.com/s?k=acab&crid=246SL34V8LD9W&sprefix=acab%2Caps%2C176&ref=nb_sb_noss_2',
    'rtt': '150',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '2',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-viewport-width': '1792',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'viewport-width': '1792',
}

params = {
    'k': 'clubbing outfits',
    'page': 2,
    'crid': '2YIYE54RC2H5B',
    'sprefix': 'clubbing outfit,aps,143',
    'ref': 'nb_sb_noss',
}

response = requests.get('https://www.amazon.com/s', headers=headers, params=params, cookies=cookies)

html = response.text
soup = BeautifulSoup(html, "html.parser")

titles = soup.select("h2")
for t in titles:
    print(t.text.strip())
