
#----------------[sending Request use Url Cookes And headers]-------------
cookies = {
    'key': 'Valu',
    'key': 'Valu',
}
headers = {
    'authority': 'github.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"ddd8cf3e0d50d847b6e21617adbb2871"',
    'referer': 'https://github.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.1 Safari/537.67',
}

sop=html_txt('https://github.com/Shuvo-BBHH/mahdix_PIP',Headers=headers,Cookie=cookies)

print(sop)# Getting only Html all Elements 
print(sop.text)# Getting only Html
