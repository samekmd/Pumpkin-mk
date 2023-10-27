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

const radioButtons = document.querySelectorAll('.btn-check');
radioButtons.forEach((radioButton, index) => {
    radioButton.addEventListener('change', () => {
        // Oculte todos os cartões
        document.querySelectorAll('.card-box_bio').forEach(card => {
            card.style.display = 'none';
        });

        // Exiba o cartão correspondente ao botão clicado
        const card = document.getElementById(`card${index + 1}`);
        card.style.display = 'block';
    });
});

