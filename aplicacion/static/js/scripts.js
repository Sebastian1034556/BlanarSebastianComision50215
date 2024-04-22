//BOTONES DE FORMULARIOS

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#mostrarFormularioClientes").addEventListener("click", function() {
        if (window.location.href.indexOf(clientesUrl) == -1) {
            // Si no está en la página normal (si está en la modificada al buscar), se hace la redirección para evitar errores
            window.location.href = clientesUrl;
        }});

        document.querySelector("#mostrarFormularioClientes").addEventListener("click", function() {
            document.querySelector("#formulario_clientes").style.display = "block";
            });
        });

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#mostrarFormularioEmpleados").addEventListener("click", function() {
        if (window.location.href.indexOf(empleadosUrl) == -1) {
            window.location.href = empleadosUrl;
        }});
        
        document.querySelector("#mostrarFormularioEmpleados").addEventListener("click", function() {
            document.querySelector("#formulario_empleados").style.display = "block";
            });
        });

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#mostrarFormularioProductos").addEventListener("click", function() {
        if (window.location.href.indexOf(productosUrl) == -1) {
            window.location.href = productosUrl;
        }});
        
        document.querySelector("#mostrarFormularioProductos").addEventListener("click", function() {
            document.querySelector("#formulario_productos").style.display = "block";
            });
        });

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#mostrarFormularioPedidos").addEventListener("click", function() {
        if (window.location.href.indexOf(pedidosUrl) == -1) {
            window.location.href = pedidosUrl;
        }});
        document.querySelector("#mostrarFormularioPedidos").addEventListener("click", function() {
            document.querySelector("#formulario_pedidos").style.display = "block";
            });
        });

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#adidas_section").addEventListener("click", function(){
        
    })
});