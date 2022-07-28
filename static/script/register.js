
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
  




  $("button").click(function () {
    $(".check-icon").hide();
    setTimeout(function () {
      $(".check-icon").show();
    }, 10);
  });


  function yourlink() {

    var locs = ['http://google.com', 'http://yahoo.com'] 

    for (let i = 0; i < locs.length; i++) {
      window.open(locs[i])}
    };