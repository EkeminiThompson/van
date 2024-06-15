document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.button');
    buttons.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.backgroundColor = '#333';
        });
        button.addEventListener('mouseout', () => {
            button.style.backgroundColor = '#e8491d';
        });
    });
});
