import requests
import csv
from pprint import pprint
from datetime import datetime, timedelta
from decouple import config
M_name = []
M_code = []
with open('movie.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)   
    for row in reader :
        M_name.append(row['감독명'])
        M_code.append(row['영화 대표코드']) 
    with open('director.csv', 'w', newline='', encoding='utf-8') as fnew:
        fieldnames = ('영화인 코드', '영화인명', '분야', '필모리스트')
        writer = csv.DictWriter(fnew, fieldnames=fieldnames)
        writer.writeheader()           
        #for i in M_name : #M_name   
        key = config('MY_KEY')                   
        base_url ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
        api_url = f'{base_url}?key={key}&peopleNm=봉준호' 
        response = requests.get(api_url)
        data = response.json()
        people_info = data['peopleListResult']['peopleList']
        people_Cd = people_info[0]['peopleCd']

        api_url2 = f'{base_url}?key={key}&peopleCd={people_Cd}'

        response2 = requests.get(api_url2)
        data1 = response2.json()
        people_info2 = data1['peopleInfoResult']['peopleInfo']
        people_Role = people_info2['repRoleNm']
        people_filmos = people_info2['filmos']
        len(people_filmos)  
        data2 = {
                '영화인 코드' : people_Cd,
                '영화인명' : M_name,
                '분야' : people_Role,
                '필모리스트' : ,
                }
        writer.writerow(data1)
