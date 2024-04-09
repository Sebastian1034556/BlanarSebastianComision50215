//BOTONES DE FORMULARIOS

document.getElementById("mostrarFormulario").addEventListener("click", function() {
    if (window.location.href.indexOf("{% url 'clientes' %}") == -1) {
        // Si no está en la página normal (si está en la modificada al buscar), se hace la redirección para evitar errores
        window.location.href = "{% url 'clientes' %}";
    }});
    document.getElementById("mostrarFormulario").addEventListener("click", function() {
        document.getElementById("formulario").style.display = "block";
    });


document.getElementById("mostrarFormulario_empleados").addEventListener("click", function() {
    if (window.location.href.indexOf("{% url 'empleados' %}") == -1) {
        window.location.href = "{% url 'empleados' %}";
    }});
    document.getElementById("mostrarFormulario_empleados").addEventListener("click", function() {
        document.getElementById("formulario_empleados").style.display = "block";
    });


document.getElementById("mostrarFormulario_pedidos").addEventListener("click", function() {
    if (window.location.href.indexOf("{% url 'pedidos' %}") == -1) {
        window.location.href = "{% url 'pedidos' %}";
    }});
    document.getElementById("mostrarFormulario_pedidos").addEventListener("click", function() {
        document.getElementById("formulario_pedidos").style.display = "block";
    });

document.getElementById("mostrarFormulario").addEventListener("click", function() {
    if (window.location.href.indexOf("{% url 'productos' %}") == -1) {
        window.location.href = "{% url 'productos' %}";
    }});
    document.getElementById("mostrarFormulario").addEventListener("click", function() {
        document.getElementById("formulario").style.display = "block";
    });