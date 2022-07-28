from models import User, session


class FindUser:
    def find_user_by_email(self, form_email):
        self.form_email = form_email
        check_user = session.query(User).filter_by(email = self.form_email).first()
        if check_user:
            return check_user
        else:
            raise Exception(f'Email {self.form_email} not found in our database')   
        
        
    def find_user_by_cpf(self, form_cpf):
        self.form_cpf = form_cpf
        check_user = session.query(User).filter_by(cpf = self.form_cpf).first()
        if check_user:
            return check_user
        else:
            raise Exception(f'Email {self.form_cpf} not found in our database')                 
    