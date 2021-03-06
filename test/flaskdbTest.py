from pybo.models import Question, Answer
from datetime import datetime
from pybo import db


# question1 = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())
# question2 = Question(subject='플라스크 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())

question1 = Question(subject='질문1', content='질문1 입니다.', create_date=datetime.now())
question2 = Question(subject='질문2', content='질문2 입니다.', create_date=datetime.now())

db.session.add(question1)
db.session.add(question2)
db.session.commit()

answer1 = Answer(question=Question.query.get(1), content='저도 잘 모르겠네요 ㅜㅜ', create_date=datetime.now())
answer2 = Answer(question=Question.query.get(2), content='네 자동으로 생성됩니다.', create_date=datetime.now())

db.session.add(answer1)
db.session.add(answer2)
db.session.commit()

# RuntimeError: No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.

