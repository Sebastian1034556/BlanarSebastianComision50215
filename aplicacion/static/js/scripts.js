export const comprobarUrl = (url,strict=null) => {
    if (strict === true){
        const currentUrl = new URL(window.location.href);
        const targetUrl = new URL(url, window.location.origin);
        return currentUrl.pathname === targetUrl.pathname;
    } else {
        return window.location.href.includes(url.split("/")[1]) 
    }
}
function mostrarFormulario(btnMostrar, formulario, url) {
    btnMostrar.addEventListener("click", () => {
        if (window.location.href.indexOf(url) == -1) {
            window.location.href = url;
        }
        formulario.style.display = "block";
    });
}

document.addEventListener("DOMContentLoaded", () => {
    // #region BOTONES DE FORMULARIOS

    // Obtención de elementos del DOM
    const btnMostrarClienteForm = document.querySelector("#mostrarFormularioClientes");
    const clienteForm = document.querySelector("#formulario_clientes");

    const btnMostrarEmpleadoForm = document.querySelector("#mostrarFormularioEmpleados");
    const empleadoForm = document.querySelector("#formulario_empleados");

    const btnMostrarProductoForm = document.querySelector("#mostrarFormularioProductos");
    const productoForm = document.querySelector("#formulario_productos");

    const btnMostrarPedidoForm = document.querySelector("#mostrarFormularioPedidos");
    const pedidoForm = document.querySelector("#formulario_pedidos");

    // Ejemplos de uso
    if (comprobarUrl(clientesUrl) && btnMostrarClienteForm && clienteForm) {
        mostrarFormulario(btnMostrarClienteForm, clienteForm, clientesUrl);
    } 
    else if (comprobarUrl(empleadosUrl) && btnMostrarEmpleadoForm && empleadoForm) {
        mostrarFormulario(btnMostrarEmpleadoForm, empleadoForm, empleadosUrl);
    } 
    else if (comprobarUrl(productosUrl) && btnMostrarProductoForm && productoForm) {
        mostrarFormulario(btnMostrarProductoForm, productoForm, productosUrl);
    } 
    else if (comprobarUrl(pedidosUrl) && btnMostrarPedidoForm && pedidoForm) {
        mostrarFormulario(btnMostrarPedidoForm, pedidoForm, pedidosUrl);
    }

    // #endregion

// #region HEADER
const header = document.querySelector(".header");
if (comprobarUrl(homeUrl,true) && header || comprobarUrl(homeUrl + "login/",true) && header) {
    header.style.position = "fixed";
}
// #endregion

});
