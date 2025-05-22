// Archivo JavaScript para la tienda de camisetas de fútbol

document.addEventListener('DOMContentLoaded', function() {
    // Inicialización de tooltips de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Animación para las tarjetas de productos
    const productCards = document.querySelectorAll('.product-card');
    if (productCards.length > 0) {
        productCards.forEach(card => {
            card.classList.add('fade-in');
        });
    }

    // Validación de formularios
    const forms = document.querySelectorAll('.needs-validation');
    if (forms.length > 0) {
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }

    // Contador para cantidad de productos
    const quantityInputs = document.querySelectorAll('input[type="number"]');
    if (quantityInputs.length > 0) {
        quantityInputs.forEach(input => {
            input.addEventListener('change', function() {
                if (this.value < 1) {
                    this.value = 1;
                }
            });
        });
    }

    // Cambio de método de pago en checkout
    const metodoPago = document.querySelectorAll('input[name="metodo_pago"]');
    const datosTarjeta = document.getElementById('datos_tarjeta');
    
    if (metodoPago.length > 0 && datosTarjeta) {
        metodoPago.forEach(function(radio) {
            radio.addEventListener('change', function() {
                if (this.value === 'tarjeta') {
                    datosTarjeta.style.display = 'block';
                } else {
                    datosTarjeta.style.display = 'none';
                }
            });
        });
    }
});
