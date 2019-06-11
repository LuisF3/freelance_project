let ano;
let data = new Date();

//Exibir as opções de ano de conclusão de curso
ano = document.getElementById("ano-0").innerHTML = data.getFullYear();
ano = document.getElementById("ano-1").innerHTML = data.getFullYear() + 1;
ano = document.getElementById("ano-2").innerHTML = data.getFullYear() + 2;
ano = document.getElementById("ano-3").innerHTML = data.getFullYear() + 3;
ano = document.getElementById("ano-4").innerHTML = data.getFullYear() + 4;
ano = document.getElementById("ano-5").innerHTML = data.getFullYear() + 5;

//Validar a senha
function validar(){
    let senha = document.getElementById("password").value;
    let senhaRepetida = document.getElementById("password-repeated").value;

    if(senha != "" && senhaRepetida != "" && senha === senhaRepetida) location.href="createdaccount.html";
    else alert('Senhas diferentes!');
}
