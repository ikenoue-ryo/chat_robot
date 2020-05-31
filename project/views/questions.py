from project.DB import db

user_info = {}

def some_questions(user_login):
    #user_nameにはRyoが入る
    user_info['user_name'] = user_login
    user_info['age'] = input('あなたは何歳ですか？ [ 0~100 ]\n')
    user_info['nickname'] = input('ニックネームは何ですか？ [ 例：たけし ]\n')
    user_info['animal'] = input('好きな動物は何ですか？ [ 例：ねこ ]\n')
    print('質問は以上です。ありがとうございました。\n')
    db.save(user_info)
    return user_info
