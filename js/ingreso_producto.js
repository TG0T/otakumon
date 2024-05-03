$(document).ready(function() { //funcion anonima
    $('#btn-ingreso').click(function(){ //$('#ID <= id del div/objeto').click <= es lo mismo que el onclick de html =>(function(){}) <= se le asigna la funcion
        let codigo = $('#codigo-producto').val()
        let nombre = $('#nombre-producto').val()
        let descripcion = $('#descripcion-producto').val()
        let precio = $('#precio-producto').val()
        let mail = $('#correo-ing').val(localStorage.getItemetItem("x"))

        let url = "https://programadormaldito.cl/route/usuario_duoc_almacenar"
        let datos = {
            codigo: codigo,
            nombre: nombre,
            descripcion: descripcion,
            precio: precio,
            mail: mail
        }

        $.ajax({
            url: url,
            type: "POST", //da la orden de "ingresar" datos
            contentType: "application/json",
            data: JSON.stringify(datos), //transforma en strings los datos conseguidos

            success: function(response){ //accion si la operacion funciona
                console.log(response)
            },
            error: function(status, error){ //accion si la operacion falla
                console.log(error + " " + status)
            }
        })
    })
})