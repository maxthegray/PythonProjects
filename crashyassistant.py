import requests
from bs4 import BeautifulSoup
import os
import datetime
from appscript import app, mactypes
from applescript import tell


url = 'https://thechainsaw.com/business/shailushai-what-is-the-cat-smurf-trend-on-tiktok/'
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',
}

r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

on = 1

while on > 0:
	
	i = 0
	
	downloads_folder = os.path.expanduser('~/Downloads')

	for img in soup.findAll('img'):
	    i = i + 1
	    image_temp = img.get('src')
	
	    if image_temp and 'jpg' in image_temp:
	        if image_temp.startswith('/'):
	            image_path = "https://thechainsaw.com" + image_temp
	        else:
	            image_path = image_temp
	
	        file_path_i = os.path.join(downloads_folder, "shalushai_{}.png".format(i))
	        timestamp = datetime.datetime.now().strftime("%H-%M-%S-%MS")
	        file_path_timestamp = os.path.join(downloads_folder, "shalushai_{}_{}.png".format(i, timestamp))
	
	        response = requests.get(url=image_path)
	        if response.status_code == 200:
	            with open(file_path_i, 'wb') as f_i:
	                f_i.write(response.content)
	                
	            response = requests.get(url=image_path)
	            if response.status_code == 200:
	                with open(file_path_timestamp, 'wb') as f_timestamp:
	                    f_timestamp.write(response.content)
