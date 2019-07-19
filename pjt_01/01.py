import requests
import csv
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    #저장할 필드의 이름을 저장한다.
    fieldnames = ('영화 대표코드', '영화명', '해당일 누적관객수')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    #필드 이름을 csv 파일 최상단에 지정

    writer.writeheader()
    movie_lists =[]
    for i in range(50):
        targetDt = datetime(2019, 7, 13) - timedelta(weeks=i)
        targetDt = targetDt.strftime('%Y%m%d')
        print(targetDt)
        key = config('MY_KEY')                   
        base_url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
        api_url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb=0' 
        response = requests.get(api_url)
        data = response.json()
    #Dictionary를 순회하며 key값에 맞는 value를 한줄씩 작성 
        for movie_info in data.get("boxOfficeResult").get("weeklyBoxOfficeList"):
            movie_Cd = movie_info['movieCd']
            movie_Name = movie_info['movieNm']
            movie_Num = movie_info['audiAcc']
            if movie_Name not in movie_lists :
                movie_lists.append(movie_Name)
                data1 = {
                    '영화 대표코드' : movie_Cd,
                    '영화명' : movie_Name,
                    '해당일 누적관객수' :f'({targetDt})  ' + movie_Num ,
                }
                writer.writerow(data1)