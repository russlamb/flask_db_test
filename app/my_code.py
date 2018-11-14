import string
import random
from app.models import MyText
from app import db

def random_string(N):
    """
    Get random string with length N
    :param N: integer
    :return: string of length N
    """

    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def clear_my_text(session_id):
    my_text = MyText.query.filter_by(session_id=session_id).first()
    if my_text:
        db.session.delete(my_text)
        db.session.commit()

def save_my_text(session_id, session_text):
    my_text = MyText(session_id=session_id,session_text=session_text)

    db.session.add(my_text)
    db.session.commit()

def get_my_text(session_id):
    my_text = MyText.query.filter_by(session_id=session_id).first()
    return my_text.session_text
