let date = new Date();
let dd = date.getDate();
let mm = date.getMonth() + 1;      
let yyyy = date.getFullYear();

if(dd < 10){
    dd = '0' + dd;
}

if(mm < 10){
    mm = '0' + mm;
}

date = yyyy + '-' + mm + '-' + dd;
document.getElementById("start-day").setAttribute("min",date);
document.getElementById("end-day").setAttribute("min",date);

yyyy++;
date = yyyy + '-' + mm + '-' + dd;
document.getElementById("start-day").setAttribute("max",date);
document.getElementById("end-day").setAttribute("max",date);

function validar_data(){
    if(document.getElementById("start-day").value >= document.getElementById("end-day").value)
        document.getElementById("start-day").setCustomValidity('O data inicial deve ser inferior à data de término.');
}