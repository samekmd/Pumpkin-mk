alert("The page is reloading")

//Inicop do Carousel 
var radio = document.querySelector('.manual-btn')
var cont = 1

document.getElementById("radio1").checked = true


//setInterval(() => {
   // proximaImg()
//}, 5000)

function  proximaImg(){
     cont++

     if(cont > 3){
        cont = 1
     }
     


     

     document.getElementById("radio"+cont).checked = true

   



}



//Fim do Carousel


//Inicio do Carousel Vertical

var radio = document.querySelector('btn btn-outline-danger')
var cont = 1
document.getElementById("vbtn-radio1").checked = true

function  proximaImg_Vertical(){
   cont++

   if(cont > 3){
      cont = 1
   }
   document.getElementById("radio"+cont).checked = true
}