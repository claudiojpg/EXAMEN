const passwordInput = document.querySelector("#password")
const eye = document.querySelector("#eye")
eye.addEventListener("click", function(){
    this.classList.toggle("fa-eye-slash")
    const type = passwordInput.getAttribute("type") === "password" ? "text" : "password"
    passwordInput.setAttribute("type", type)
  })

  function login(){
    var user, password;
    
    user = document.getElementById("usuario").value;
    password = document.getElementById("password").value;
  
    
    if(user.trim() === "" && password.trim() === ""){
      alert("Debes completar los campos");
    } 
    else if(user == "admin" && password == "admin"){
      location.href="datos_fundap"; 
    } 
    else if(user != "admin") { 
      
      alert("El usuario no está registrado");
    } 
    else {
      
      alert("Contraseña incorrecta");
    }
  }

  document.addEventListener('DOMContentLoaded', function() {
   
    var submitButton = document.getElementById('submit-btn');
  
  
    submitButton.addEventListener('click', function(event) {
      
      event.preventDefault();

      
      alert('Aporte realizado');
    });
  });