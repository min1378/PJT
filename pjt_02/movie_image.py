import requests
import csv
Thumb_url = []
M_code = []

# movie_naver.csv에서 영화 썸네일 이미지의 URL과 영진위 영화 대표코드를 읽어온다.
with open('movie_naver.csv', 'r' , newline='', encoding='utf-8') as fr :
    reader = csv.DictReader(fr)   
    for row in reader :
        Thumb_url.append(row['영화 썸네일 이미지의 URL'])
        M_code.append(row['영진위 영화 대표코드'])

# for문을 활용하여 image파일의 이름을 영진위 영화 대표코드로 하고 저장한다.
for i in range(len(M_code)) :
    with open(f'images/{M_code[i]}.jpg', 'wb') as f:
        response = requests.get(Thumb_url[i])
        f.write(response.content)








