let data = new Date();

//Exibir as opções de ano de conclusão de curso
document.getElementById("ano-0").innerHTML = data.getFullYear();
document.getElementById("ano-1").innerHTML = data.getFullYear() + 1;
document.getElementById("ano-2").innerHTML = data.getFullYear() + 2;
document.getElementById("ano-3").innerHTML = data.getFullYear() + 3;
document.getElementById("ano-4").innerHTML = data.getFullYear() + 4;
document.getElementById("ano-5").innerHTML = data.getFullYear() + 5;
document.getElementById("ano-0").setAttribute("value", "" + data.getFullYear());
document.getElementById("ano-1").setAttribute("value", "" + (data.getFullYear() + 1));
document.getElementById("ano-2").setAttribute("value", "" + (data.getFullYear() + 2));
document.getElementById("ano-3").setAttribute("value", "" + (data.getFullYear() + 3));
document.getElementById("ano-4").setAttribute("value", "" + (data.getFullYear() + 4));
document.getElementById("ano-5").setAttribute("value", "" + (data.getFullYear() + 5));

//Validar a senha
function validar(){
    let senha = document.getElementById("password").value;
    let senhaRepetida = document.getElementById("password-repeated").value;

    if(senha != "" && senhaRepetida != "" && senha === senhaRepetida) location.href="createdaccount.html";
    else alert('Senhas diferentes!');
}
