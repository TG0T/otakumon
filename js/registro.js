$(document).ready(function() { //funcion anonima
    $('#btn-registrar').click(function(){ //$('#ID <= id del div/objeto').click <= es lo mismo que el onclick de html =>(function(){}) <= se le asigna la funcion
        let mail = $('#mail').val()
        let pass = $('#pass').val()
        let nombre = $('#nombre').val()
        let apellido = $('#apellido').val()

        let url = "https://programadormaldito.cl/route/usuario_duoc_almacenar"
        let datos = {
            mail: mail,
            pass: pass,
            nombre: nombre,
            apellido: apellido
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

    $('#btn_login').click(function(){ //$('#ID <= id del div/objeto').click <= es lo mismo que el onclick de html =>(function(){}) <= se le asigna la funcion
        let mail = $('#l-mail').val() //consigue valores del login
        let pass = $('#l-pass').val() //consigue valores del login  

        let url = "https://programadormaldito.cl/route/usuario_login" //direccion de la api
        let datos = {
            mail: mail, //consuige datos de mail y pass desde la api ()
            pass: pass
        }

        let correo = {}

        $.ajax({
            url: url,
            type: "POST", //da la orden de "ingresar" datos
            contentType: "application/json",
            data: JSON.stringify(datos), //transforma en strings los datos conseguidos

            success: function(response){ //accion si la operacion funciona
                console.log(response)
                correo.mail = mail

                localStorage.setItem("x", mail);
            },
            error: function(status, error){ //accion si la operacion falla

            }
        })
    })
})