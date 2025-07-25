document.addEventListener("DOMContentLoaded", function(){ //espera la carga del DOM
    document.body.addEventListener("click", function (evento){ //Escucha todos los clics en el documento
        const link = evento.target.closest("a.empleado_detail"); //identifica el clic de la clase empleado_detail
        if (link){
            evento.preventDefault(); // evita la navegacion a la url
    
            fetch(link.href)
                .then(response => {
                    if (!response.ok) throw new Error('Error al cargar detalles'); // verifica respuesta 200
                    return response.text(); // convierte la repuesta html a texto
            })
            .then(html => {
                document.querySelector('.main-content').innerHTML = html;
            })
            .catch(error => {
                console.error(error)
            });
        }



    });
});

