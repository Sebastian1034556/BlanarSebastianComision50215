import { comprobarUrl } from './scripts.js';

function validarFormulario(url,form,fields,regex,errorMessages,update = false) {
    document.addEventListener('DOMContentLoaded', ()=> {
        if (comprobarUrl(url)) {
            form.addEventListener('input', (event) => onInput(event,fields,regex,errorMessages));
            form.addEventListener('submit', (event) => onSubmit(event,fields,regex,update));
        }
    });
}

function onInput(event,fields,regex,errorMessages) {
    const target = event.target;
    
    for (let i = 0 ; i < fields.length ; i++ ){
        if (target.id === "id_" + fields[i])
            validateField(target, regex[i], errorMessages[i]);
    }
}

async function onSubmit(event,fields,regex,update) {
    const form = event.target;
    const elements = []
    let dni = undefined

    for (let i = 0; i < fields.length; i++){
        elements.push(document.getElementById('id_' + fields[i]))
        if (fields[i] === "dni"){
            dni = document.getElementById('id_' + fields[i]).value
        } 
    }
    const alertMessage = document.getElementById('error-message');
    let validFields = true

    for (let i = 0 ; i < fields.length ; i++){
        if (!regex[i].test(elements[i].value) || (fields[i] === "sueldo" && parseFloat(elements[i].value) >= 10000000) || (fields[i] === "precio" && parseFloat(elements[i].value) >= 10000000)){
            validFields = false
            event.preventDefault();
            alertMessage.innerText = "Por favor, corrija los campos en rojo antes de enviar el formulario."
        }
    }
    if (validFields && dni){
        if (update == false){
            event.preventDefault();
            try {
                const esDniUnico = await verificarDni(dni);
                alert(esDniUnico)
                if (!esDniUnico) {  
                    alertMessage.innerText = 'El DNI ya está registrado. Por favor, revíselo.';
                } else {
                    form.submit();
                }
            } catch (e) {
                alertMessage.innerText = 'Ocurrió un error al verificar el DNI.';
            }
        } else {
            form.submit();
        }
        
    }
}

function validateField(input, regex, errorMsg) {
    const alertMessage = document.getElementById('error-message');
    if (regex.test(input.value) && (input.id !== 'id_sueldo' || parseFloat(input.value) < 10000000) && (input.id !== 'id_precio' || parseFloat(input.value) < 10000000)) {
        input.classList.add('valid-input');
        input.classList.remove('invalid-input');
        alertMessage.innerText = '';
    } else {
        input.classList.remove('valid-input');
        input.classList.add('invalid-input');
        alertMessage.innerText = errorMsg;
    }
}

const URL_VIEWS = '/verificarDni/';

async function verificarDni(dni) {
    const urlConDni = `${URL_VIEWS}?dni=${encodeURIComponent(dni)}`;
    try {
        const res = await fetch(urlConDni);
        const data = await res.json();
        if (data.exists) {
            return false;
        } else {
            return true;
        }
    } catch (e) {
        console.error('Error:', e);
        return false;
    }
}

// #region regex
const nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑãõçÇ]{3,50}$/;
const apellidoRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑãõçÇ]{3,50}$/;
const edadRegex = /^(1[89]|[2-9]\d|1[01]\d|120)$/;
const dniRegex = /^\d{8}$/;
const sueldoRegex =  /^[0-9]+(\.[0-9]{1,2})?$/;
const nombreProductoRegex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑãõçÇ\s\-'.]{3,100}$/
const precioRegex = /^[0-9]+(\.[0-9]{1,2})?$/;
const marcaRegex = /^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑãõçÇ\s\-]{2,50}$/
const stockRegex =  /^[0-9][0-9]*$/
const colorRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑãõçÇ\s\-]{3,30}$/
const tallaRegex = /^\d{1,2}(?:-\d{1,2})?$/
const imagenRegex = /\.(jpg|jpeg|png|gif|bmp|webp)$/i

//#endregion

// #region errores
const nombreError = 'El nombre debe tener entre 3 y 50 caracteres y solo contener letras (sin espacios).'
const apellidoError = 'El apellido debe tener entre 3 y 50 caracteres y solo contener letras (sin espacios).'
const edadError = 'La edad debe ser de entre 18 y 120 años.'
const dniError = 'El DNI debe tener 8 dígitos.'
const sueldoError = "El sueldo debe ser un numero positivo menor a 10000000, con hasta dos decimales opcionales."

const nombreProductoError = 'El nombre del producto debe tener entre 3 y 100 caracteres y solo puede contener letras, números, espacios,puntos, guiones y apóstrofes.';
const precioError = 'El precio debe ser un número positivo menor a 10000000, con hasta dos decimales opcionales.';
const marcaError = 'La marca debe tener entre 2 y 50 caracteres y solo puede contener letras, números, espacios y guiones.';
const stockError = 'El stock debe ser un número entero positivo.';
const colorError = 'El color debe tener entre 3 y 30 caracteres y solo puede contener letras, espacios y guiones.';
const tallaError = 'La talla debe tener entre 1 y 10 caracteres y solo puede contener letras y números.';
const imagenError = 'El archivo debe ser una imagen con una de las siguientes extensiones: jpg, jpeg, png, gif, bmp, webp.';
//#endregion

// clientes
const formularioClientes = document.getElementById('cliente-form')

const fieldsClientes = ["nombre","apellido","edad","dni"]
const regexClientes = [nombreRegex,apellidoRegex,edadRegex,dniRegex]

const errorMessagesClientes = [nombreError,apellidoError,edadError,dniError]

// empleados

const formularioEmpleados = document.getElementById('empleado-form')
const fieldsEmpleados = ["nombre","dni","apellido","edad","sueldo"]
const regexEmpleados = [nombreRegex,dniRegex,apellidoRegex,edadRegex,sueldoRegex]
const errorMessagesEmpleados = [nombreError,dniError,apellidoError,edadError,sueldoError]

// productos
const formularioProductos = document.getElementById("producto-form")
const fieldsProductos = ["nombre","precio","marca","stock","color","talla","imagen"]
const regexProductos = [nombreProductoRegex,precioRegex,marcaRegex,stockRegex,colorRegex,tallaRegex,imagenRegex]
const errorMessagesProductos = [nombreProductoError,precioError,marcaError,stockError,colorError,tallaError,imagenError]

if (comprobarUrl(clientesUrl)) validarFormulario(clientesUrl,formularioClientes,fieldsClientes,regexClientes,errorMessagesClientes)
else if (comprobarUrl(empleadosUrl)) validarFormulario(empleadosUrl,formularioEmpleados,fieldsEmpleados,regexEmpleados,errorMessagesEmpleados)
else if (comprobarUrl(productosUrl)) validarFormulario(productosUrl,formularioProductos,fieldsProductos,regexProductos,errorMessagesProductos)

if (comprobarUrl("/clienteUpdate/")){
    const updateClientes = document.getElementById('clienteForm')
    validarFormulario('/clienteUpdate/', updateClientes ,fieldsClientes,regexClientes,errorMessagesClientes,true)
} 
else if (comprobarUrl("/empleadoUpdate/")){
    const updateEmpleados = document.getElementById('empleadoForm')
    validarFormulario('/empleadoUpdate/',updateEmpleados,fieldsEmpleados,regexEmpleados,errorMessagesEmpleados,true)
}
else if (comprobarUrl("/productoUpdate/")){
    const updateProductos = document.getElementById('productoForm')
    validarFormulario('/productoUpdate/',updateProductos,fieldsProductos,regexProductos,errorMessagesProductos,true)
}
