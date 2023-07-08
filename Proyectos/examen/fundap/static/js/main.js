const passwordInput = document.querySelector("#password")
const eye = document.querySelector("#eye")
eye.addEventListener("click", function(){
    this.classList.toggle("fa-eye-slash")
    const type = passwordInput.getAttribute("type") === "password" ? "text" : "password"
    passwordInput.setAttribute("type", type)
  })

  function login(){
    var user, password
    
    user = document.getElementById("usuario").value;
    password= document.getElementById("password").value;


    if(user == "admin" && password =="admin"){
       location.href="datos_fundap"

       
    }
    
    else{
     alert("error")    
    }
}
