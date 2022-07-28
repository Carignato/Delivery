        
        # Verificar se o form.gender retorna com uma mensagem válida, caso contrário retorna uma mensagem 401
        
        
        

        if check_email != None:
            flash('Esse email já existe')
            return render_template('register.html')
        
        if not re.match(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", form.email):
            flash('email invalido')
            return render_template('register.html')
        
        check_cpf = session.query(User.cpf).filter_by(cpf=form.cpf).first()
        
        if check_cpf != None:
             print('Esse cpf já existe')
             return render_template('register.html')
         
        if not re.match(r'^([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}|[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})$', form.cpf):
            print(form.cpf)
            print('cpf invalido')
            return render_template('register.html')
        
        
        char_to_replace = {
                        '.': '',
                        '-':''}
      
        for key, value in char_to_replace.items():

            form.cpf = form.cpf.replace(key, value)
        
        check_phone = session.query(User.phone).filter_by(phone=form.phone).first()
       
        if  check_phone != None:
            print('Telefone já cadastrado')
            return render_template('register.html')
        
        if not re.match(r'\([0-9]{2}\) [0-9]{5}\-[0-9]{4}', form.phone):
            print(form.phone)
            print('numero de telefone inválido')
            return render_template('register.html')
            
        char_to_replace = {
                        ' ':'',
                        '(': '',
                        '-': '',
                        '.': '',
                        ')':''}
      
        for key, value in char_to_replace.items():
            form.phone = form.phone.replace(key, value)
            date_format = form.date

            date_format = re.findall(r'[0-9]{4}',form.date)[0]
            date_format = int(date_format) 
            current_year = date.today().year
        
        if date_format < 1900 or date_format > current_year:
             print('Data invalida')               
             return render_template('register.html')
         
         
        session.add(form)
        session.commit()
        return render_template('register.html', name = name, teste = teste)
    
    
    
    
    
    
    
    
    function ValidateEmail(inputText) {
  var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  if (inputText.value.match(mailformat)) {
   // alert("Valid email address!");
    return true;
  } else {
    //alert("You have entered an invalid email address!");
    return false;
  }
}


function ValidateCPF(inputText) {
  var cpfformat = /([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})/;
  if (inputText.value.match(cpfformat)) {
    //alert("Valid CPF!");
    return true;
  } else {
    //alert("You have entered an invalid CPF!");
    return false;
  }
}



function checkPassword(password, password_2) {
  password1 = password.value;
  password2 = password_2.value;


  if (password1 == '')
    //alert("Please enter Password");


  else if (password2 == '')
   // alert("Please enter confirm password");

 
  else if (password1 != password2) {
    //alert("\nPassword did not match: Please try again...")
    return false;
  } else {
    
    return true;
  }
}

function isValidDate(dateString)
{
    // First check for the pattern
    if(!/^\d{1,2}\/\d{1,2}\/\d{4}$/.test(dateString))
      // alert("\nPassword did not match: Please try again...")

    // Parse the date parts to integers
    var parts = dateString.split("/");
    var day = parseInt(parts[1], 10);
    var month = parseInt(parts[0], 10);
    var year = parseInt(parts[2], 10);

    // Check the ranges of month and year
    if(year < 1000 || year > 3000 || month == 0 || month > 12)
        return false;

    var monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];

    // Adjust for leap years
    if(year % 400 == 0 || (year % 100 != 0 && year % 4 == 0))
        monthLength[1] = 29;

    // Check the range of the day
    return day > 0 && day <= monthLength[month - 1];
};





