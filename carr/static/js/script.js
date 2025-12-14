// Script para adicionar interatividade ao site

document.addEventListener('DOMContentLoaded', function() {
    // Suavizar scroll
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const target = document.querySelector(targetId);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Adicionar classe ativa ao navbar
    const currentLocation = location.pathname;
    const menuItems = document.querySelectorAll('.nav-menu a');
    menuItems.forEach(item => {
        if (item.getAttribute('href') === currentLocation) {
            item.classList.add('active');
        }
    });

    // Animação de entrada dos cards
    const cards = document.querySelectorAll('.carro-card');
    cards.forEach((card, index) => {
        card.style.animation = `slideDown 0.6s ease ${index * 0.1}s both`;
    });

    // Favoritar carros
    const botoesF = document.querySelectorAll('.btn-secundario');
    botoesF.forEach(btn => {
        btn.addEventListener('click', function() {
            this.classList.toggle('favoritado');
            if (this.classList.contains('favoritado')) {
                this.style.background = '#ffe6e6';
                this.style.color = '#e74c3c';
                this.textContent = '❤️ Adicionado aos Favoritos';
            } else {
                this.style.background = 'white';
                this.style.color = 'var(--dark)';
                this.textContent = '❤️ Adicionar aos Favoritos';
            }
        });
    });
});

// Função para simular scroll suave
function scrollToSection(sectionId) {
    const section = document.querySelector(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}
