from project.models import robot

def question_to_you():
    question_robot = robot.Question_Robot()
    question_robot.auto_greeting()
    question_robot.some_question()


def what_are_you_doing():
    doing_robot = robot.Doing_Robot()
    doing_robot.hearing()