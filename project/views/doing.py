import requests
import datetime
import locale
import json
import urllib.request

from project.DB import db
import settings

def tenki_api():
     city_name = input('どこの天気が知りたいですか？　(入力例:Tokyo)\n')
     app_id = settings.API_KEY
     URL = "https://api.openweathermap.org/data/2.5/weather?q={0},jp&units=metric&lang=ja&appid={1}".format(city_name, app_id)

     response = requests.get(URL)
     data = response.json()

     weather = data["weather"][0]["description"]  # 最高気温
     temp_max = data["main"]["temp_max"]  # 最低気温
     temp_min = data["main"]["temp_min"]  # 寒暖差
     diff_temp = temp_max - temp_min  # 湿度
     humidity = data["main"]["humidity"]
     # 日付と曜日の取得
     today = datetime.datetime.now()
     date_time = today.strftime("%Y年%m月%d日 ")
     locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
     now_w = "{0:%A}".format(today)
     day = date_time + now_w


     context = {"日付": day ,"天気": weather, "最高気温": str(temp_max) + "度", "最低気温": str(temp_min) + "度",
                "湿度": str(humidity) + "%"}
     print("--{0}'s Weather--".format(city_name))
     for k, v in context.items():
          print("{0}:{1}".format(k, v))

     if 20 <= int(temp_min):
          print('暑い日が続いていますね。')


def friends_api():
     print('誰のプロフィールをみたいですか？')
     persons = db.session.query(db.Person).all()
     for i, person in enumerate(persons, start=1):
          print(i, person.user_name)

     user_id = input()
     persons = db.session.query(db.Person).filter_by(id=user_id).first()
     context = {'名前：': persons.user_name, '年齢：': persons.age,
                'ニックネーム：': persons.nickname, '好きな動物：': persons.animal
                }
     for k, v in context.items():
          print('{0}:{1}'.format(k, v))


def gnavi_api():
     #レストラン検索APIのURL
     Url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
     # パラメータの設定
     params = {}
     params['keyid'] = settings.GNAVI_API_KEY
     params['freeword'] = 'ハンバーグ'
     params['hit_per_page'] = 3
     params['pref'] = 'PREF40'#福岡

     result_api = requests.get(Url, params)
     result_api = result_api.json()

     # 福岡県
     print(result_api['rest'][0]['code']['prefname'])
     print(result_api['rest'][0]['name'])
     print(result_api['rest'][0]['url'])
     print(result_api['rest'][0]['address'])


def others():
     print('考え中です。')