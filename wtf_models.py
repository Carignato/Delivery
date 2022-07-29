from logging.config import valid_ident
from pydoc import render_doc
from tokenize import String
from attr import attrs, validate
import attr
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class Register_wtf(FlaskForm): 
        name = StringField('Name', validators=[InputRequired(), Length(min = 5, max = 100 )], render_kw={"placeholder": "Nome"})
        date = StringField('Data', validators=[InputRequired(), Length(min = 10, max = 10), Regexp('[0-9]{2}\/[0-9]{2}\/[0-9]{4}', message="Data Invalida") ], render_kw={"placeholder": "dd/mm/aaaa"})
        email = StringField('Email', validators=[InputRequired(), Length(min = 5, max = 100 ), Regexp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", message="Email inválido")], render_kw={"placeholder": "E-mail"})
        cpf = StringField('CPF',  validators=[InputRequired(),Length(min = 5, max = 15 ), Regexp("^([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}|[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})$", message="CPF inválido")], render_kw={"placeholder": "___.___.___-__"})
        phone = StringField('Phone', validators=[InputRequired(), Length(min = 5, max = 15 )], render_kw={"placeholder": "(  )_____-____"}) 
        password = PasswordField('Password', validators=[InputRequired(), Length(min = 8, max = 100 ), EqualTo('confirm_password', message='As senhas precisam ser iguais')], render_kw={"placeholder": "Senha"})          
        gender = RadioField('Label', choices=[('M','Masculino'),('F','Feminino'), ('N','Não informar')], validators=[Regexp("[A-Z]{1}", message="Invalid")] )
        confirm_password = PasswordField('Confirme a senha', validators=[InputRequired(), Length(min = 8, max = 100)], render_kw={"placeholder": "Confirme a senha"})
        button = SubmitField("Enviar")

class Address_wtf(FlaskForm):
        name = StringField('Name', validators=[InputRequired(), Length(min = 3, max = 100)], render_kw={"placeholder": "Nome do destinatario"})
        cep = StringField('CEP', validators=[InputRequired(), Length(max = 9)], render_kw={"placeholder": "CEP"})
        street = StringField('Street', validators=[InputRequired(), Length(max= 100)], render_kw={"placeholder": "Rua", 'readonly': True} )
        number = IntegerField('Number', validators=[InputRequired(), Length(min = 1, max= 20)], render_kw ={"placeholder": "Numero"}  )
        complement = StringField('Complement', validators=[InputRequired(), Length(min = 1, max = 100)], render_kw={"placeholder": "Complemento"})
        zone = StringField('Zone', validators=[InputRequired(), Length(min = 1, max = 100)], render_kw={"placeholder": "Bairro" , 'readonly': True})
        city = StringField('City', validators=[InputRequired(), Length(min = 1 , max = 50)], render_kw={"placeholder": "Cidade" , 'readonly': True})
        state = StringField('State', validators=[InputRequired(), Length(min = 1 , max = 2)], render_kw={"placeholder": "UF" , 'readonly': True})        
        set_default = BooleanField('Default_Address', render_kw={"placeholder": "Endereço Padrão"})
        button = SubmitField("+ Adicionar endereço") 
        
class Cards_wtf(FlaskForm):
        card_number = StringField('Card_number', validators=[InputRequired(), Length(min = 19, max = 19 )], render_kw={"placeholder": "Numero do cartão"})
        name_card = StringField('Name_card', validators=[InputRequired(), Length(min = 3, max = 100 )], render_kw={"placeholder": "Nome impresso no cartão"})
        valid_date = StringField('Valid_date', validators=[InputRequired(), Length(min = 5 , max = 5)] , render_kw = {"placeholder": "Validade"})
        code = StringField('code', validators=[InputRequired(), Length(min = 3 , max = 3)], render_kw = {"placeholder": "CVV"})        
        button = SubmitField(" + Adicionar cartão")        