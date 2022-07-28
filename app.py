from pydoc import render_doc
from wtf import *
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy, inspect
from models import *
import re
from datetime import date
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db?check_same_thread=False"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager = LoginManager(app)
app_static_folder="static"



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
  
  

@login_manager.user_loader
def load_user(id):
    return session.query(User).get(id)
   

@app.route('/homepage')
@login_required
def homepage(): 
    return render_template('homepage.html')

@app.route('/base_profile')
def base_profile():
    return render_template('base_profile.html')

@app.route("/login", methods =["GET", "POST"])
def login():
    if request.method == "POST":    
        from database.classes import FindUser
        
        form_email = request.form['email']
        form_password = request.form['password']
        
        check_user = FindUser().find_user_by_email(form_email)
        
        if check_user == None:
           flash('E-mail ou senha incorretos', 'login_error') 
           return render_template('login.html')
       
        if not check_password_hash(check_user.password,form_password):
             return render_template('login.html')
        
        else:
            login_user(check_user) 
          
            return redirect(url_for('homepage'))
   
    
    
    return render_template('login.html')   
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))








@app.route('/cards',  methods = ['GET','POST'])
@login_required
def cards():
    
     form_cards_wtf = Cards_wtf()
     
    
     if form_cards_wtf.validate_on_submit():
        form = createCard(request.form)
        
        list_of_indexes = [4, 5, 6, 7, 8 ,9 ,10, 11]
        new_character = '*'

        # Replace characters at index positions in list
        for i in list_of_indexes:
            form.card_number = form.card_number[:i] + new_character + form.card_number[i+1:]
         
        session.add(form)
        session.commit()
        
       
        return redirect(url_for('cards'))
               
     cards_info = session.query(Cards).filter(Cards.id_user == current_user.id).all()     

     return render_template('cards.html', form_cards_wtf = form_cards_wtf, cards_info = cards_info)


@app.route('/exclude_card')
@login_required
def exclude_card():
    
    id = request.args.get('id')
    print(id)
    db.session.query(Cards).filter(Cards.id == id).delete()
    db.session.commit()
    
    
    return redirect(url_for('cards'))





@app.route('/register_success')
def register_success():
    form_wtf = Register_wtf()
    return render_template('/register_success.html',  form_wtf = form_wtf)


@app.route('/register', methods = ["GET","POST"])
def register():
    
    # Formulario criado com a biblioteca what the forms
    form_wtf = Register_wtf()
    
    # Caso o formulario não encontre nenhum erro na solicitação via POST
    if form_wtf.validate_on_submit():

        form = createRegister(request.form)
    
        check_user = session.query(User).filter((User.email == form.email) | (User.phone == form.phone) | (User.cpf == form.cpf)).first()
        
        if check_user != None:

            flash('Esse usuário já está cadastrado')
        
        else:
            
         session.add(form)
         session.commit()
         
          
        return render_template('register_success.html', form_wtf = form_wtf)
    
    return render_template('register.html', form_wtf = form_wtf)






@app.route('/address', methods = ['GET','POST'])
@login_required
def address():

    if request.method == "POST" and "edit_address" in request.form:
     
        form = createAddress(request.form)
        print(request.form)
    
        session.query(Address).filter(Address.id == form.id).update({
            Address.name: form.name,
            Address.cep: form.cep,
            Address.number: form.number,
            Address.street: form.street,
            Address.complement: form.complement,
            Address.zone: form.zone,
            Address.city: form.city,
            Address.state: form.state
        })
        db.session.commit()
       
        return redirect(url_for('address'))    

    if request.method == 'POST':
        
        form = createAddress(request.form)
        print(request.form)
        zone = re.sub("([\(\[]).*?([\)\]])", "", form.zone)
        form.zone = zone
        address_info = session.query(Address).filter(Address.id_user == current_user.id).all()  
        session.add(form)
        session.commit()

        # Check if there is already a default address for the user. If there is, update it, otherwise, add a new one.
        checkbox = request.form.get('set_default')
        if checkbox:
            default_address_info = session.query(DefaultAddress).filter(DefaultAddress.id_user == current_user.id).first()
            if default_address_info is not None:
                db.session.query(DefaultAddress).filter(DefaultAddress.id_user == current_user.id).update({DefaultAddress.id_address: form.id})
            else:
                new_default_address = DefaultAddress(id_user = form.id_user, id_address = form.id)
                session.add(new_default_address)
            db.session.commit()

        return redirect(url_for('address'))
    
   
    form_address_wtf = Address_wtf()
   
    address_info = session.query(Address).filter_by(id_user = current_user.id).all()
    
    # Get default address ID for the user. If it doesn't exist, set as -1.
    default_address = session.query(DefaultAddress).filter(DefaultAddress.id_user == 44444).first()
    if default_address is not None:
        default_address_id = default_address.id_address
    else:
        default_address_id = -1
    
    return render_template('address.html', default_address_id = default_address_id, address_info = address_info, form_address_wtf = form_address_wtf)
                                                                   



@app.route('/exclude_address', methods = ['GET'])
@login_required
def exclude_address(): 
    
    id = request.args.get('id')

    db.session.query(Address).filter(Address.id == id).delete()
    db.session.commit()
    return redirect(url_for('address'))


@app.route('/profile')
@login_required
def profile():
     users = session.query(User).all()
     return render_template('profile.html', users = users)
   

if __name__ =="__main__":   
 app.run(debug=True)
 