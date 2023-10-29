document.addEventListener('DOMContentLoaded', function () {
    var dropdownButton = document.getElementById('dropdownButton');
    var dropdownMenu = document.getElementById('dropdownMenu');

    dropdownButton.addEventListener('click', function () {
        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'block';
        }
    });
});

// Esconder todas as seções, exceto a primeira
document.addEventListener('DOMContentLoaded', function () {
    var sections = document.querySelectorAll('.conteudo-dropdown');
    for (var i = 1; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }
});

function toggleMenu() {
    var dropdownMenu = document.querySelector('.custom-dropdown-menu');
    dropdownMenu.classList.toggle('show');
}

function showSection(sectionId) {
    // Esconder todas as seções de conteúdo
    var sections = document.querySelectorAll('.conteudo-dropdown');
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }

    // Mostrar a seção desejada
    var selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.style.display = 'block';
    }
}