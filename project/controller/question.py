from project.models import robot
from project.DB import db

def question_to_you():
    question_robot = robot.Question_Robot()
    question_robot.auto_greeting()
    #DBにuser_nameがなければ新規ユーザーなので質問する処理
    persons = db.session.query(db.Person).all()
    all_user = []
    for person in persons:
        all_user.append(person.user_name)
    if not question_robot.user_name in all_user:
        question_robot.some_question()

    #何がしたいか聞く
    question_robot.hearing()
