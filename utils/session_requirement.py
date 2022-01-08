from flask import session, redirect
from functools import wraps

def login_requiered(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        print(session)
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect("/index")

    return wrap


def logout_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect('/index')
        else:
            return f(*args, **kwargs)
            
    return wrap