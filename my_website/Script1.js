// ������� ��� ��������� �����������
document.getElementById('registrationForm')?.addEventListener('submit', function (e) {
    e.preventDefault(); // �������� ����������� ��������� �����

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    // ��������� ������ ������������ � localStorage (��� ��������)
    localStorage.setItem('username', username);
    localStorage.setItem('email', email);

    // ��������������� �� �������� ������� ��������
    window.location.href = 'dashboard.html';
});

// ����������� ��������������� ��������� � ������ ��������
window.onload = function () {
    const username = localStorage.getItem('username');
    if (username) {
        document.getElementById('w�// JavaScript source code
