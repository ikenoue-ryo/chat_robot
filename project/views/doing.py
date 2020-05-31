from project.DB import db

def tenki_api():
     print('天気は晴れです')


def friends_api():
     print('誰のプロフィールをみたいですか？')
     persons = db.session.query(db.Person).all()
     for i, person in enumerate(persons, start=1):
          print(i, person.user_name)

     which_user = input()
     for person in persons:
          print(person.user_name, person.age, person.nickname, person.animal)

def others():
     print('考え中です。')