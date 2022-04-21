import requests
from bs4 import BeautifulSoup

cookies = {
    'MUID': '3F5376C768B161AE24E6678069D66026',
    'MUIDB': '3F5376C768B161AE24E6678069D66026',
    'SRCHD': 'AF=NOFORM',
    'SRCHUID': 'V=2&GUID=EE1379022EBA433B8966673DB380DF85&dmnchg=1',
    'MicrosoftApplicationsTelemetryDeviceId': 'ae33a6cb-eb71-4f57-b13f-0b0d6bed7823',
    '_RwBf': 'ilt=5&ihpd=1&ispd=0&rc=0&rb=0&gb=0&rg=200&pc=0&mtu=0&rbb=0&g=0&cid=&clo=0&v=1&l=2022-02-11T08:00:00.0000000Z&lft=00010101&aof=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2022-02-11T18:17:06.7197599+00:00&rwred=0',
    '_UR': 'QS=0&TQS=0',
    'MSCC': '1',
    'SUID': 'M',
    '_SS': 'SID=309CBF50F6CC644F2C87AE2FF7AB65CF',
    '_HPVN': 'CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wNC0wN1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6N30=',
    'SRCHUSR': 'DOB=20220210&T=1649371644000',
    'ipv6': 'hit=1649375245609&t=4',
    'ai_session': 'c5i6oOL8QLLgEchJSFZKjl|1649371646428|1649371646428',
    '_EDGE_S': 'SID=309CBF50F6CC644F2C87AE2FF7AB65CF&mkt=pt-pt',
    'SRCHHPGUSR': 'SRCHLANG=en&BRW=XW&BRH=S&CW=1792&CH=450&SW=1792&SH=1120&DPR=2&UTC=60&DM=0&HV=1649371646&WTS=63784968444',
}

headers = {
    'authority': 'www.bing.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'MUID=3F5376C768B161AE24E6678069D66026; MUIDB=3F5376C768B161AE24E6678069D66026; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=EE1379022EBA433B8966673DB380DF85&dmnchg=1; MicrosoftApplicationsTelemetryDeviceId=ae33a6cb-eb71-4f57-b13f-0b0d6bed7823; _RwBf=ilt=5&ihpd=1&ispd=0&rc=0&rb=0&gb=0&rg=200&pc=0&mtu=0&rbb=0&g=0&cid=&clo=0&v=1&l=2022-02-11T08:00:00.0000000Z&lft=00010101&aof=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2022-02-11T18:17:06.7197599+00:00&rwred=0; _UR=QS=0&TQS=0; MSCC=1; SUID=M; _SS=SID=309CBF50F6CC644F2C87AE2FF7AB65CF; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMi0wNC0wN1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6N30=; SRCHUSR=DOB=20220210&T=1649371644000; ipv6=hit=1649375245609&t=4; ai_session=c5i6oOL8QLLgEchJSFZKjl|1649371646428|1649371646428; _EDGE_S=SID=309CBF50F6CC644F2C87AE2FF7AB65CF&mkt=pt-pt; SRCHHPGUSR=SRCHLANG=en&BRW=XW&BRH=S&CW=1792&CH=450&SW=1792&SH=1120&DPR=2&UTC=60&DM=0&HV=1649371646&WTS=63784968444',
    'referer': 'https://www.bing.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"100.0.4896.60"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"11.6.4"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'x-autosuggest-contentwidth': '596',
}

letters = "abcdefghijklmnopqrstuvwxyz"
for l in letters:
    for l2 in letters:
        params = {
            'pt': 'page.home',
            'mkt': 'pt-pt',
            'qry': 'why do i ' + l + l2,
            'asv': '1',
            'cp': '8',
            'msbqf': 'false',
            'cvid': '0C61B75F78374929951E1C15E10544B0',
        }

        response = requests.get('https://www.bing.com/AS/Suggestions', headers=headers, params=params, cookies=cookies)
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("li")
        for i in items:
            print(i.text.strip())