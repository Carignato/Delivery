from flask_sqlalchemy import SQLAlchemy, inspect
from flask_login import current_user
from database.models import Address, User, Cards
from werkzeug.security import generate_password_hash
def obj_to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

def flatten_join(tup_list):
    return [{**obj_to_dict(a), **obj_to_dict(b)} for a,b in tup_list]

def createAddress(form):
    if 'id' in form:
        address = Address(
            name = form['name'],
            cep = form['cep'].replace('-',''),
            street = form['street'],
            number = form['number'],
            complement = form['complement'],
            zone = form['zone'],
            city = form['city'],
            state = form['state'],
            id = form['id'],
            id_user = current_user.id
        )
    else:
        address = Address(
            name = form['name'],
            cep = form['cep'].replace('-',''),
            street = form['street'],
            number = form['number'],
            complement = form['complement'],
            zone = form['zone'],
            city = form['city'],
            state = form['state'],
            id_user = current_user.id
        )
    return address


def createRegister(form):
    register = User(
        name = form['name'].strip(),
        email = form['email'].replace(" ", ""),
        date = form['date'].replace(" ", "").replace('/','-'),
        cpf = form['cpf'], 
        phone = form['phone'], 
        gender = form['gender'].replace(" ", ""),
        password = generate_password_hash(form['password'])
        )   
    return register
  
  
def createCard(form):
    cards = Cards(
        card_number = form['card_number'].replace(" ", ""),
        name_card = form['name_card'],
        valid_date = form['valid_date'].replace(" ", ""),
        code =  generate_password_hash(form['code']),
        id_user = current_user.id
        )  
     
    return cards  
  