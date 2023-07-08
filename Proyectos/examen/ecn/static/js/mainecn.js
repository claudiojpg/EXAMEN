function login(){
    var user, password
    
    user = document.getElementById("usuario").value;
    password= document.getElementById("password").value;


    if(user == "usuario" && password =="1234"){
       location.href="index.html"

       localStorage.usuario=user
    }
    
    else{
     alert("error")    
    }
}






const time=document.getElementById('time');
const date=document.getElementById('date');

const monthNames=["Enero","Febrero","Marzo",
                    "Abril","Mayo","Junio","Julio",
                "Agosto","Septiembre","Octubre","Noviembre"
            ,"Diciembre"];
const interval = setInterval(() =>{

    const local =new Date();
    let day=local.getDate();
        month=local.getMonth();
        year=local.getFullYear();

time.innerHTML= local.toLocaleTimeString();
date.innerHTML=`${day} ${monthNames[month]} ${year}`;

},1000);

const passwordInput = document.querySelector("#password")
const eye = document.querySelector("#eye")
eye.addEventListener("click", function(){
    this.classList.toggle("fa-eye-slash")
    const type = passwordInput.getAttribute("type") === "password" ? "text" : "password"
    passwordInput.setAttribute("type", type)
  })


        function enviarFormulario() {
            var nombre = document.getElementById("nombre").value;
            var correo = document.getElementById("correo").value;
            var telefono = document.getElementById("telefono").value;
            var mensaje = document.getElementById("mensaje").value;

          

            alert("¡Formulario enviado con éxito!"); 
        }
 