import requests
import csv
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
M_code = []
with open('boxoffice.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)   
    for row in reader :
        M_code.append(row['영화 대표코드']) 
    with open('movie.csv', 'w', newline='', encoding='utf-8') as fnew:
        fieldnames = ('영화 대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉연도', '상영시간', '장르', '감독명')
        writer = csv.DictWriter(fnew, fieldnames=fieldnames)
        writer.writeheader()
        movie_genres = ''
        movie_GradeNm = ''
        movie_Director= ''            
        for i in M_code : #M_code
            movie_genres = ''
            key = config('MY_KEY')                   
            base_url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
            api_url = f'{base_url}?key={key}&movieCd={i}' 
            response = requests.get(api_url)
            data = response.json()

            #값 추출
            movie_info = data['movieInfoResult']['movieInfo']
            movie_Cd = movie_info['movieCd']
            movie_Nm = movie_info['movieNm']
            movie_NmEn = movie_info['movieNmEn']
            movie_NmOg = movie_info['movieNmOg']

            #비어있을때 예외처리
            if movie_info['audits'] != [] :
                movie_GradeNm = movie_info['audits'][0]['watchGradeNm']                         
            movie_openDt = movie_info['openDt']
            movie_ShowTime = movie_info['showTm']
            for i in movie_info['genres'] :
                movie_genres += i['genreNm'] + ' '
            #비어있을때 예외처리    
            if movie_info['directors'] != [] :
                movie_Director = movie_info['directors'][0]['peopleNm']    
            data1 = {
                    '영화 대표코드' : movie_Cd,
                    '영화명(국문)' : movie_Nm,
                    '영화명(영문)' : movie_NmEn,
                    '영화명(원문)' : movie_NmOg,
                    '관람등급' : movie_GradeNm,
                    '개봉연도' : movie_openDt,
                    '상영시간' : movie_ShowTime +'분',
                    '장르' : movie_genres,
                    '감독명' : movie_Director,
                    }
            writer.writerow(data1)




