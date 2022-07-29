from database.models import User, session
from exceptions import *

class FindUser:
    def find_user_by_email(self, form_email):
        x = session.query(User).filter_by(email = form_email).first()
        if not x:
            raise EmailNotFound
        return x
      

