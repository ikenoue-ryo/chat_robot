from project.models import robot
from project.DB import db

def question_to_you():
    question_robot = robot.Question_Robot()
    question_robot.auto_greeting()
    #DBにuser_nameがなければ新規ユーザーなので質問する処理
    persons = db.session.query(db.Person).all()
    for person in persons:
        if not question_robot.user_name in person.user_name:
            question_robot.some_question()
        else:
            break
        break


def what_are_you_doing():
    doing_robot = robot.Doing_Robot()
    doing_robot.hearing()