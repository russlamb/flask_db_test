from app import db


class MyText(db.Model):
    """
    SQL Alchemy data model for storing session id and text
    """
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(32), index=True, unique=True)
    session_text = db.Column(db.Text())

    def __repr__(self):
        return '<MyText {}>'.format(self.session_id)

