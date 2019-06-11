//Validar a senha
function validar(){
    let senha = document.getElementById("password").value;
    let senhaRepetida = document.getElementById("password-repeated").value;

    if(senha != senhaRepetida){
        senhaRepetida = document.getElementById("password-repeated");
        senhaRepetida.setCustomValidity('Senhas diferentes.');
    }

    else{
        post('{% url 'webapp:empresa:register_page' %}try/', {username: document.getElementById("username").value, email: document.getElementById("email").value,
        nome_fantasia: document.getElementById("fantasy-name").value, nome_juridico: document.getElementById("name").value, city, password: senha});
    }
}

/**
 * sends a request to the specified url from a form. this will change the window location.
 * @param {string} path the path to send the post request to
 * @param {object} params the paramiters to add to the url
 * @param {string} [method=post] the method to use on the form
 */

function post(path, params, method='post') {

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;
  
    for (const key in params) {
      if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];
  
        form.appendChild(hiddenField);
      }
    }
  
    document.body.appendChild(form);
    form.submit();
  }
  