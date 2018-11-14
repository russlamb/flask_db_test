import uuid

from flask import render_template, session

from app import app
from app.my_code import random_string, save_my_text, get_my_text, clear_my_text


@app.route('/')
@app.route('/index')
def index():
    """
    Create a unique id (uuid), if it doesn't exist, and save it in the browser cookies.
    Generate a random string and save that in the database.
    display the UID in a webpage
    :return: Flask template
    """
    # NOTE: For testing
    # clear uid out of cookies
    # if "uid" in session:
    #    session.pop("uid")

    # create uuid and store in cookies
    if "uid" not in session:
        session["uid"] = str(uuid.uuid4())

    session_id = str(session["uid"])

    # generate random string
    session_text = random_string(10)

    # save to database with this session id
    clear_my_text(session_id)  # clear out existing data
    save_my_text(session_id, session_text)  #
    return render_template('index.html', title='Home', session_id=session_id)


@app.route('/my_text')
def show_my_text():
    """
    Get Text from database for the current session id
    Display the session id and text in a webpage
    :return: Flask template
    """
    if "uid" not in session:
        session["uid"] = str(uuid.uuid4())

    session_id = str(session["uid"])

    my_items = [get_my_text(session_id)]  # making the text a list because the template expects a list.

    return render_template('show_my_text.html', title="Show Your text", session_id=session_id, session_text=my_items)
