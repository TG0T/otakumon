$(document).ready(function() {

    let login = localStorage.getItem('x1')

    if(login == 'NO'){
        $('#logged').hide()
        $('#not_logged').show()
    }
    else{

        $('#logged').show()
        $('#not_logged').hide()

    let link = "https://programadormaldito.cl/route/producto_duoc_obtener"

    $.ajax({
        url: link,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            let listado = $('#listado');

            data.forEach(function(item) {
                item.forEach(function(producto) {

                    let itemlista = $('<div class="col-md-4 mb-3"></div>');
                    itemlista.append('<div class="card">');
                    itemlista.find('.card').append('<div class="card-body">');
                    itemlista.find('.card-body').append('<h5 class="card-title">Código: ' + producto.p_codigo + '</h5>');
                    itemlista.find('.card-body').append('<p class="card-text">Nombre: ' + producto.p_nombre + '</p>');
                    itemlista.find('.card-body').append('<p class="card-text">Descripción: ' + producto.p_descripcion + '</p>');
                    itemlista.find('.card-body').append('<p class="card-text">Precio: ' + producto.p_precio + '</p>');
                    itemlista.find('.card-body').append('<p class="card-text">Correo electrónico: ' + producto.p_mail_creado + '</p>');
                    itemlista.append('</div></div>');

                    listado.append(itemlista);
                });
            });
        },
        error: function(xhr, status, error) {
            console.error('Error al obtener el JSON:', error);
        }
    });
}


})