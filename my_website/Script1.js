// Функция для обработки регистрации
document.getElementById('registrationForm')?.addEventListener('submit', function (e) {
    e.preventDefault(); // Отменяем стандартное поведение формы

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    // Сохраняем данные пользователя в localStorage (для простоты)
    localStorage.setItem('username', username);
    localStorage.setItem('email', email);

    // Перенаправление на страницу личного кабинета
    window.location.href = 'dashboard.html';
});

// Отображение приветственного сообщения в личном кабинете
window.onload = function () {
    const username = localStorage.getItem('username');
    if (username) {
        document.getElementById('w…// JavaScript source code
