import requests
import re
from bs4 import BeautifulSoup
import os

# 다운로드할 웹사이트 URL
url = "https://generated.photos/faces/elderly"

# 이미지를 저장할 폴더 생성
if not os.path.exists("images_old"):
    os.makedirs("images_old")

# 웹사이트 HTML 가져오기  
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 모든 jpg 이미지 URL 찾기
img_urls = []
for img in soup.find_all("img"):
    img_url = img.attrs.get("src")
    if img_url:
        if re.search(r'\.jpg$', img_url):
            img_urls.append(img_url)

# 이미지 다운로드
for img_url in img_urls:
    filename = re.search(r'/([\w_-]+[.](jpg))$', img_url)
    if not filename:
         print("정규식과 매칭되지 않습니다.")
         continue
    with open("images_old/" + filename.group(1), 'wb') as f:
        response = requests.get(img_url)  # 절대경로로 바로 requests.get()
        f.write(response.content)