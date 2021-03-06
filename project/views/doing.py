import requests
import datetime
import locale
import json
import urllib.request
import termcolor
import time

from project.DB import db
from project.views import city_search
from apiclient.discovery import build
import settings

YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def tenki_api(user_name):
    where = termcolor.colored('どこの天気が知りたいですか？　(入力例:Tokyo)\n', 'blue', attrs=['bold'])
    city_name = input(where)
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
        print('暑い日が続いていますね。\n')


    persons = db.session.query(db.Person).filter_by(user_name=user_name)
    for person in persons:
        if person.family == 0 :
            #ユーザーの追加情報を取得
            another_question = termcolor.colored('ところで、' + user_name + 'さんは何人家族ですか？\n', 'blue', attrs=['bold'])
            family = input(another_question)
            thank_you = termcolor.colored('ありがとうございます！\n', 'blue', attrs=['bold'])
            print(thank_you)
            db.add_save(user_name, family)


def friends_api():
    who = termcolor.colored('誰のプロフィールをみたいですか？\n', 'blue', attrs=['bold'])
    print(who)
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


def gnavi_api(user_name):
    #レストラン検索APIのURL
    Url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
    # パラメータの設定
    params = {}
    params['keyid'] = settings.GNAVI_API_KEY
    params['hit_per_page'] = 3
    #都道府県コードを取ってきて検索
    live = termcolor.colored('お住いの都道府県を入力してください (例：東京都)\n', 'blue', attrs=['bold'])
    city = input(live)
    params['pref'] = city_search.search(city)
    #キーワード検索
    keyword = termcolor.colored('キーワードを入力してください (例：焼肉)\n', 'blue', attrs=['bold'])
    freeword = input(keyword)
    params['freeword'] = freeword

    result_api = requests.get(Url, params)
    result_api = result_api.json()

    print('********************************')
    print(city + 'の' + freeword + 'の検索結果を表示します。')
    print('********************************')
    #3件表示
    for count in range(3):
      # print(result_api['rest'][count]['code']['prefname'])
      print(result_api['rest'][count]['name'])
      print(result_api['rest'][count]['url'])
      print(result_api['rest'][count]['address']+ '\n')
    print('ぜひ行ってみてください。\n')


    #家族の人数が分かっていれば個室の提案をする
    persons = db.session.query(db.Person).filter_by(user_name=user_name)
    for person in persons:
        if person.family != 0:
            time.sleep(3)
            persons = db.session.query(db.Person).filter_by(user_name=user_name)
            for person in persons:
                talk = termcolor.colored('そういえば、' + user_name + 'さんは' + str(person.family) + '人家族でしたね。\n個室を探しておきました。\n', 'blue', attrs=['bold'])
                print(talk)
            params['private_room'] = 1
            result_api = requests.get(Url, params)
            result_api = result_api.json()

            print('********************************')
            print('「個室あり」 の検索結果を表示します。')
            print('********************************')
            #3件表示
            for count in range(3):
              # print(result_api['rest'][count]['code']['prefname'])
              print(result_api['rest'][count]['name'])
              print(result_api['rest'][count]['url'])
              print(result_api['rest'][count]['address']+ '\n')


def search_youtube():
    key = termcolor.colored('Youtubeから再生数が多い動画を検索します。\nキーワードを入力してください\n', 'blue', attrs=['bold'])
    key_word = input(key)

    search_response = youtube.search().list(
    part='snippet',
    #検索したい文字列を指定
    q=key_word,
    #視聴回数が多い順に取得
    order='viewCount',
    type='video',
    ).execute()

    print('********************************')
    print(key_word + '　の検索結果を表示します。')
    print('********************************')
    # 3件表示
    for count in range(3):
        # print(search_response['items'][0])
        print('チャンネル名：', search_response['items'][count]['snippet']['channelTitle'])
        print('動画タイトル：', search_response['items'][count]['snippet']['title'])
        print('https://www.youtube.com/watch?v=' + search_response['items'][count]['id']['videoId'] + '\n')
    print('動画をお楽しみください。\n')



def others():
    think = termcolor.colored('考え中です。\n', 'blue', attrs=['bold'])
    print(think)