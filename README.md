# pip install mahdix

## Print Something
```bash
from mahdix import p

print(p('YOUR TXT'))
```
## Get Current Time
```bash
from mahdix import time

print(time())
```
## Generate Text Logo
```bash
from mahdix import makelogo

logo = makelogo(text='Mahdi')
print(logo)
```
## Random Numbers
```bash
from mahdix import random7, random8, random9, random1_2, random1_3, random1_4, random10

print(random7())
print(random8())
print(random9())
print(random1_2())
print(random1_3())
print(random1_4())
print(random10())
```
## System Commands
```bash
from mahdix import sysT

sysT('YOUR COMMAND')
```
## HTTP Requests
```bash
from mahdix import rqg, rqp

response_get = rqg('https://example.com')
response_post = rqp('https://example.com', data={'key': 'value'})
```
## Random Choices
```bash
from mahdix import rc

print(rc([1, 2, 3, 4]))

```
## Base64 Encoding/Decoding
```bash
from mahdix import bsec, bsdc

encoded_data = bsec('Hello, World!')
decoded_data = bsdc(encoded_data)
```
## Colors
```bash
# ---[coloure]------

RED = mahdix.RED

GREEN = mahdix.GREEN

YELLOW = mahdix.YELLOW

BLUE=mahdix.BLUE

ORANGE =mahdix.ORANGE

LI_BLUE = Light_BLUE

LI_MAGENTA = Light_MAGENTA

LI_CYAN = Light_CYAN

LI_WHITE = Light_WHITE

Background colors

BG_BLACK = Background_BLACK

BG_RED = Background_RED

BG_GREEN = Background_GREEN 

```
## get any Facebook id created date
```bash
from mahdix import getyearid

# Example: cid = '100000000023456'
print(getyearid(cid))
```
## html_txt Function
The html_txt function fetches HTML content from the specified URL, using optional headers and data for the request.
```bash
from your_module import html_txt

url = 'https://example.com'
headers = {
    'User-Agent': 'Your User Agent',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
cookie = {'key': 'value'}  # Optional Cookes for POST requests
data = {'key': 'value'}  # Optional data for POST requests
parsed_html = html_txt(url, Headers=headers, Data=data,Cookie=cookie) # data for POST requests 
parsed_html = html_txt(url, Headers=headers,Cookie=cookie) #  for Get requests 
print(parsed_html)
```
### [Example of  html_txt function](https://github.com/Shuvo-BBHH/mahdix/tree/main/html_txt).

