let ano;
let data = new Date();

//Exibir as opções de ano de conclusão de curso
function data_conclusao_curso () {
    document.getElementById("ano-0").innerHTML = data.getFullYear();
    document.getElementById("ano-1").innerHTML = data.getFullYear() + 1;
    document.getElementById("ano-2").innerHTML = data.getFullYear() + 2;
    document.getElementById("ano-3").innerHTML = data.getFullYear() + 3;
    document.getElementById("ano-4").innerHTML = data.getFullYear() + 4;
    document.getElementById("ano-5").innerHTML = data.getFullYear() + 5;
}

$(document).ready(function(){
    $(".toggle").click(function(){
        $(".toggle-item").toggle(500);
    });
});