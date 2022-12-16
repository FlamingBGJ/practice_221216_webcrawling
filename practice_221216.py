# xml을 dict 형태로 저장하는 라이브러리 설치
!pip install xmltodict
# !conda install xmltodict

# 필수 라이브러리 불러오기
import requests
import json
import xmltodict
import getpass
import pandas as pd

# 영화진흥위원회 오픈API 정보 저장 
# https://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do

DATE = "20221214"
params = {"key": API_KEY, "targetDt":DATE}

response = requests.get(daily_box, params=params)
movie_info = json.loads(response.text)


movie_info["boxOfficeResult"]["showRange"]
movie_info["boxOfficeResult"]["boxofficeType"]

pd.json_normalize(movie_info["boxOfficeResult"]["dailyBoxOfficeList"])

# 영화 제목으로 영화 코드를 불러오는 함수를 만들어 보자ss
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.xml

def movie_code(movieNm):
    movie_name2code_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
    params = {"key": API_KEY, "movieNm":movieNm}
    response = requests.get(movie_name2code_url, params)
    movie_info = json.loads(response.text)
    for i in movie_info["movieListResult"]["movieList"]:
        print(i["movieCd"])


# 영화 코드로 영화 정보중 배우를 불러오는 함수를 만들어 보세요
movie_code("미니언즈2")

movie_code2info_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
params = {"key": API_KEY}
response = requests.get(movie_code2info_url, params)
movie_info = json.loads(response.text)
print(movie_info["movieInfoResult"]["movieInfo"]["actors"])

def movie_info(movieCd):
    movie_code2info_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    params = {"key": API_KEY, "movieCd":movieCd}
    response = requests.get(movie_code2info_url, params)
    movie_info = json.loads(response.text)
    print(movie_info["movieInfoResult"]["movieInfo"]["actors"])
movie_info(20205362)

# 네이버 api를 이용해 papago 서비스를 사용
# 네이버 로그인 개발자 페이지 -> 키발급 -> papapgo 서비스 
# https://developers.naver.com/docs/papago/papago-nmt-example-code.md#python

import getpass

import os
import sys
import urllib.request
encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)