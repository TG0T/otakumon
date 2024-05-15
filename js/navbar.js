let login = localStorage.getItem('x1')

function user_login(){
    if (login == 'SI'){
            $('#registrate').hide()
            $('#inciasesion').hide()
            $('#sesioniniciada').show()
            $('#IngresoP').show()
            
                let navv = $('#login')
                navv.append('<nav class="navbar navbar-expand-lg bg-body-tertiary fuentenav" data-bs-theme="dark" id="main"><div class="container-fluid"><a href="index.html"><img src="/logo/OMlogo.png" alt="https://imgur.com/12B2WVN" class="navbar-brand logo"></a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav me-auto mb-2 mb-lg-0"><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Categorias</a><ul class="dropdown-menu"><li><a class="dropdown-item" href="#">Shounen</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item" href="#">Mecha</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item" href="#">Mahou Shoujo</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item" href="#">Shojo</a></li></ul></li></ul><form class="d-flex buscar" role="search"><input class="form-control me-2" type="search" placeholder="Encuentra tu manga favorito!" aria-label="Search"><button class="btn btn-outline-success" type="submit">Buscar</button></form><ul class="navbar-nav me-2"><li class="nav-item"><div><a href="/ingreso_producto.html"><button type="submit" class="btn btn-info" id="registrate">Ingreso productos</button></a></div></li></ul><ul class="navbar-nav me-auto mb-2 mb-lg-0"><li class="nav-item dropdown"><div class="dropdown"><button type="button" class="btn btn-warning dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">Usuario</button><div class="dropdown-menu p-3 anchar"><div class="mb-3"><label for="exampleDropdownFormEmail2" class="form-label">Bienvenido:</label><label id="correo_l"></label></div><button type="submit" class="btn btn-danger" id="btn_logoff">Cerrar sesion</button></div></ul></ul></div></ul></div></div></nav>')
        } else{
            $('#registrate').show()
            $('#inciasesion').show()
            $('#sesioniniciada').hide()
            $('#IngresoP').hide()
            let navv = $('#login')
            navv.append('<nav class="navbar navbar-expand-lg bg-body-tertiary fuentenav" data-bs-theme="dark" id="main"><div class="container-fluid"><a href="../index.html"><img src="/logo/OMlogo.png"class="navbar-brand logo"></a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav me-auto mb-2 mb-lg-0"><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Categorias</a><ul class="dropdown-menu"><li><a class="dropdown-item" href="#">Shounen</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item" href="#">Mecha</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item" href="#">Mahou Shoujo</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item" href="#">Shojo</a></li></ul></li></ul><form class="d-flex buscar" role="search"><input class="form-control me-2" type="search" placeholder="Encuentra tu manga favorito!" aria-label="Search"><button class="btn btn-outline-success" type="submit">Buscar</button></form><ul class="navbar-nav me-2"><li class="nav-item"><div><a href="registro.html"><button type="submit" class="btn btn-info" id="registrate">Registrate</button></a></div></li></ul><ul class="navbar-nav me-auto mb-2 mb-lg-0"><li class="nav-item dropdown"><div class="dropdown"><button type="button" class="btn btn-warning dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" data-bs-auto-close="outside">Cliente</button><div class="dropdown-menu p-3 anchar"><div class="mb-3"><label for="exampleDropdownFormEmail2" class="form-label">Correo</label><input type="email" class="form-control" id="l-mail" placeholder="email@dominio.com"></div><div class="mb-3"><label for="exampleDropdownFormPassword2" class="form-label">Contraseña</label><input type="password" class="form-control" id="l-pass" placeholder="Contraseña"></div><div class="mb-3"><div class="form-check"><input type="checkbox" class="form-check-input" id="dropdownCheck2"><label class="form-check-label" for="dropdownCheck2">Recuerdame</label></div></div><div class="mb-3 ms-auto"><a href="">¿Olvidaste tu contraseña?</a></div><button type="submit" class="btn btn-success" id="btn_login">Iniciar sesion</button></div></ul></ul></div></ul></div></div></nav>')
        }
}

$(document).ready(function(){
    user_login();
    console.log(login)
    $('#correo_l').text(localStorage.getItem('x'))

    $("#logo").click(function(){
        location.href = "../index.html"
    })
})