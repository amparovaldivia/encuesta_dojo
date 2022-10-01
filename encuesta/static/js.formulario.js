function ayuda() {
    alert("en el espacio ingresa un comentario e ingresalo haciendo click, junto con tus datos")
}
function validar_formulario() {
    //aqui se escriben las validaciones, si encuentra una que no pasa return false
    var nombre = document.getElementById("name").value;
    if (nombre == "/") {
        return false;
    }  //este sirve solo para uno, hay expresiones regulares que son como para encasillar el texto y validar y se puede comparar texto con expresiones regulares en java y ahi uno pone si es false o true

    //fin de validaciones
    return true;//el true es java es con minuscula
}