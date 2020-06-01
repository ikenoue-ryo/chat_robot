import datetime
import locale

from project.DB import db
from project.views import console, questions, doing


DEFAULT_ROBOT_NAME = 'Roboko'

class Robot(object):
    def __init__(self, robot_name=DEFAULT_ROBOT_NAME, user_name=''):
        self.robot_name = robot_name
        self.user_name = user_name

    def auto_greeting(self):
        while True:
            #日付と曜日の取得
            today = datetime.datetime.now()
            date_time = today.strftime("%Y年%m月%d日 ")
            locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
            now_w = "{0:%A}".format(today)
            day = date_time + now_w

            #あいさつ
            if 4 <= today.hour <= 10:
                greeting = 'おはよう！'
            elif 10 < today.hour <= 18:
                greeting = 'こんにちは！'
            else:
                greeting = 'こんばんは！'


            # ロボットの挨拶と入力待ち受け
            template = console.get_file_path('greeting.txt')
            user_name = input(template.substitute({
                'robot_name': self.robot_name,
                'user_name': self.user_name,
                'time': day,
                'greeting': greeting
            }))
            # 入力文字の大文字化
            if user_name:
                self.user_name = user_name.title()
                persons = db.session.query(db.Person).filter_by(user_name=self.user_name)
                for person in persons:
                    if self.user_name == person.user_name:
                        print(self.user_name +'さん、おかえりなさい\n')
                        break
                    break
                break

class Question_Robot(Robot):
    def __init__(self):
        super().__init__(robot_name=DEFAULT_ROBOT_NAME)


    def some_question(self):
        while True:
            answer = input('質問に答えますか？ [yes/no]\n')
            if answer == 'y' or answer == 'yes':
                user_login = input('あなたの名前をもう一度教えてください\n')
                user_login = user_login.title()
                if user_login == self.user_name:
                    questions.some_questions(user_login)
                    break
                else:
                    print('名前が正しくありません。')
                    break
            if answer == 'n' or answer == 'no':
                break
            break


class Doing_Robot(Robot):

    def hearing(self):
        print('なにをしたいですか？ [数字を入力]\n')
        while True:
            template = console.get_file_path('wants.txt')
            want = input(template.substitute({
                'robot_name': self.robot_name,
                'user_name': self.user_name,
            }))

            if want == '1':
                doing.tenki_api()
                break
            if want == '2':
                doing.friends_api()
                break
            if want == '3':
                doing.gnavi_api()
                break
            if want == '4':
                doing.others()
                break