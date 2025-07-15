 function cargarEmpleados() {
        console.log("Click en Empleados");

        fetch('listar-todos-empleados/')
        .then(response => {
            if (!response.ok) throw new Error("Error en la carga de empleados");
            return response.text();
        })
        .then(html => {
            document.querySelector('.main-content').innerHTML = html;
        })
        .catch(error => {
            console.error(error);
            document.querySelector('.main-content').innerHTML = "<p>Error al cargar empleados.</p>";
        });
    }

// Funcion para dar clic en buscar empleado en la consola central. 
function empleadoPorBusqueda(){
    const kword = document.getElementById("kword").value
    console.log("Buscando:", kword); 
    console.log("Buscando:", kword); 
    fetch(`listar-todos-empleados/?kword=${encodeURIComponent(kword)}`)
    .then(response => {
        if(!response.ok) throw new Error("Error en la carga de empleado.")
        return response.text();
    })

    .then(html => {
        document.querySelector('.main-content').innerHTML = html;
    })

    .catch(error => {
        console.error(error);
        document.querySelector('.main-content').innerHTML = "<p>Error en la carga de empleado.</p>";
    });
}