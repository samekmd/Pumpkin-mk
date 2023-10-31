const botoes = document.querySelectorAll(".referencias-btn");
const cards = document.querySelectorAll(".comece_referencias_renato, .comece_referencias_julio");

botoes.forEach(botao => {
    botao.addEventListener("click", function() {
        const alvo = this.getAttribute("href").substring(1); // Remove o "#" do href
        cards.forEach(card => {
            card.style.display = card.id === alvo ? "block" : "none";
        });
    });
});
