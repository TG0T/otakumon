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

        let url = "https://programadormaldito.cl/route/usuario_duoc_login" //direccion de la api
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
                if(mail == '' || pass == ''){
                    Swal.fire({
                        title: "Todos los campos son obligatorios",
                        icon: "warning"
                    }
                    );
                }else if(response[0].RESPUESTA == 'LOGIN NOK'){
                    Swal.fire({
                        title: "Usuario o contraseña invalido",
                        icon: "warning"
                    }
                    );
                }else{
                    Swal.fire({
                        title: "Credenciales validas",
                        text: "Seras redirijido en unos segundos",
                        icon: "success"
                    }
                    );
                    
                correo.mail = mail

                localStorage.setItem("x", mail);
                localStorage.setItem("x1", 'SI');

                setTimeout(() => {
                    window.location.href = "../index.html"
                }, 3000);

                
            }
            },
            error: function(status, error){ //accion si la operacion falla
                alert('No fue posible contactar con el serivor')
            }
        })
    })

    $('#btn_logoff').click(function(){
        localStorage.setItem('x1','NO')
        localStorage.setItem('x','')

        const Toast = Swal.mixin({
            toast: true,
            position: "top-end",
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.onmouseenter = Swal.stopTimer;
              toast.onmouseleave = Swal.resumeTimer;
            }
          });
          Toast.fire({
            icon: "success",
            title: "Has cerrado sesion de forma exitosa!"
          });

        setTimeout(() => {
            window.location.href = "../index.html"
        }, 3000);

    })
})