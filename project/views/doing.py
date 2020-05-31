import requests
import os

from project.DB import db
from project.views import questions

def tenki_api():
     city_name = input('入力例: Tokyo\n')
     app_id = 'API KYE'
     URL = "https://api.openweathermap.org/data/2.5/weather?q={0},jp&units=metric&lang=ja&appid={1}".format(city_name, app_id)

     response = requests.get(URL)
     data = response.json()

     weather = data["weather"][0]["description"]  # 最高気温
     temp_max = data["main"]["temp_max"]  # 最低気温
     temp_min = data["main"]["temp_min"]  # 寒暖差
     diff_temp = temp_max - temp_min  # 湿度
     humidity = data["main"]["humidity"]

     context = {"天気": weather, "最高気温": str(temp_max) + "度", "最低気温": str(temp_min) + "度",
                "湿度": str(humidity) + "%"}
     print("--{0}'s Weather--".format(city_name))
     for k, v in context.items():
          print("{0}:{1}".format(k, v))


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


def others():
     print('考え中です。')