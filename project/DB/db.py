import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///pro_sqlite3.db')
# engine = sqlalchemy.create_engine('sqlite:///:memory:')

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_name = sqlalchemy.Column(sqlalchemy.String(20))
    age = sqlalchemy.Column(sqlalchemy.Integer)
    family = sqlalchemy.Column(sqlalchemy.Integer, default=0, nullable=True)
    nickname = sqlalchemy.Column(sqlalchemy.String(20))
    animal = sqlalchemy.Column(sqlalchemy.String(20))

#Baseを継承しているテーブルを一括して作成する
#metadataはDBのいろんな情報を保持しているオブジェクト
Base.metadata.create_all(engine)

#セッションを作成(DBとPythonコードを紐づける)
#セッションを作るクラスを作成
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()


def save(user_info):

    user_info = Person(
        user_name = user_info['user_name'],
        age = user_info['age'],
        nickname = user_info['nickname'],
        animal = user_info['animal'],
    )
    session.add(user_info)
    session.commit()

    # テーブルからデータをqueryで取り出す
    persons = session.query(Person).all()
    print('---DB出力結果---')
    for person in persons:
        print(person.id, person.user_name, person.age, person.nickname, person.family, person.animal)
    print('---DB出力結果---\n')


#会話の中の質問から新たにユーザー情報を取得する
def add_save(user_name, family):

    user = session.query(Person).filter_by(user_name=user_name).first()
    user.family = family

    session.add(user)
    session.commit()
    # テーブルからデータをqueryで取り出す
    persons = session.query(Person).all()
    print('---DB出力結果---')
    for person in persons:
        print(person.id, person.user_name, person.age, person.nickname, person.family, person.animal)
    print('---DB出力結果---')


#コマンド
# sqlite3 pro_sqlite3.db
# .tables
# select * from users;