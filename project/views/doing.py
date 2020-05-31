from project.DB import db
from project.views import questions

def tenki_api():
     print('天気は晴れです')


def friends_api():
     print('誰のプロフィールをみたいですか？')
     persons = db.session.query(db.Person).all()
     for i, person in enumerate(persons, start=1):
          print(i, person.user_name)

     user_id = input()
     # for person in persons:
     #      print(person.user_name, person.age, person.nickname, person.animal)
     persons = db.session.query(db.Person).filter_by(id=user_id).first()
     print('名前：'+ persons.user_name + '\n',
          '年齢：'+ persons.age + '\n',
          'ニックネーム：'+ persons.nickname + '\n',
          '好きな動物：'+ persons.animal + '\n',
     )

def others():
     print('考え中です。')