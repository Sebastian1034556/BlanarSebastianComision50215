import { comprobarUrl } from './scripts.js';

function validarFormularioClientes() {
    document.addEventListener('DOMContentLoaded', onDocumentLoaded);
}

function onDocumentLoaded() {
    if (comprobarUrl(clientesUrl)) {
        const form = document.getElementById('cliente-form');
        form.addEventListener('input', onInput);
        form.addEventListener('submit', onSubmit);
    }
}

function validateField(input, regex, errorMsg) {
    const alertMessage = document.getElementById('error-message');
    if (regex.test(input.value)) {
        input.classList.add('valid-input');
        input.classList.remove('invalid-input');
        alertMessage.innerText = '';
    } else {
        input.classList.remove('valid-input');
        input.classList.add('invalid-input');
        alertMessage.innerText = errorMsg;
    }
}

function onInput(event) {
    const target = event.target;
    const nombreRegex = /^[a-zA-Z]{3,50}$/; 
    const apellidoRegex = /^[a-zA-Z]{3,50}$/;
    const edadRegex = /^(1[89]|[2-9]\d|1[01]\d|120)$/;
    const dniRegex = /^\d{8}$/;

    if (target.id === 'id_nombre') {
        validateField(target, nombreRegex, 'El nombre debe tener entre 3 y 50 caracteres y solo contener letras (sin espacios).');
    } else if (target.id === 'id_apellido') {
        validateField(target, apellidoRegex, 'El apellido debe tener entre 3 y 50 caracteres y solo contener letras (sin espacios).');
    } else if (target.id === 'id_edad') {
        validateField(target, edadRegex, 'La edad debe ser de entre 18 y 120 años.');
    } else if (target.id === 'id_dni') {
        validateField(target, dniRegex, 'El DNI debe tener 8 dígitos.');
    }
}

async function onSubmit(event) {
    const form = event.target;
    const nombre = document.getElementById('id_nombre');
    const apellido = document.getElementById('id_apellido');
    const edad = document.getElementById('id_edad');
    const dni = document.getElementById('id_dni');
    const nombreRegex = /^[a-zA-Z]{3,50}$/;
    const apellidoRegex = /^[a-zA-Z]{3,50}$/;
    const edadRegex = /^(1[89]|[2-9]\d|1[01]\d|120)$/;
    const dniRegex = /^\d{8}$/;
    const alertMessage = document.getElementById('error-message');

    if (!nombreRegex.test(nombre.value) || !apellidoRegex.test(apellido.value) ||
        !edadRegex.test(edad.value) || !dniRegex.test(dni.value)) {
        event.preventDefault();
        alertMessage.innerText = 'Por favor, corrija los campos en rojo antes de enviar el formulario.';
    } else {
        event.preventDefault();
        try {
            const esDniUnico = await verificarDni(dni.value);
            if (!esDniUnico) {  
                alertMessage.innerText = 'El DNI ya está registrado. Por favor, revíselo.';
            } else {
                form.submit();
            }
        } catch (e) {
            alertMessage.innerText = 'Ocurrió un error al verificar el DNI.';
        }
    }
}

const URL_VIEWS = '/verificarDni/';

async function verificarDni(dni) {
    const urlConDni = `${URL_VIEWS}?dni=${encodeURIComponent(dni)}`;
    try {
        const res = await fetch(urlConDni);
        const data = await res.json();
        if (data.exists) {
            return false; // Retorna false si el DNI es duplicado
        } else {
            return true; // Retorna true si el DNI no es duplicado
        }
    } catch (e) {
        console.error('Error:', e);
        return false; // Retorna false en caso de error
    }
}

validarFormularioClientes()