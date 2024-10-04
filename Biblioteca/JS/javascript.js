function csvToArray(csv) {
    const rows = csv.trim().split("\n").slice(1); // Omitir la primera fila (encabezados)
    return rows.map(row => row.split(",")); // Convertir cada fila en un array
}

fetch('../CSV/books.csv')
    .then(response => response.text())
    .then(data => {
        const libros = csvToArray(data); // Convertir el CSV en array
        const tbody = document.querySelector('#tabla-libros tbody');
        
        // Agregar filas a la tabla
        libros.forEach(libro => {
            const fila = `
                <tr>
                    <td>${libro[0] || 'Sin ISBN'}</td> <!-- ISBN-13 -->
                    <td>${libro[1] || 'Sin título'}</td> <!-- Título -->
                    <td>${libro[2] || 'Sin autor'}</td> <!-- Autor -->
                    <td>${libro[3] || 'Sin género'}</td> <!-- Género -->
                    <td>${libro[4] || 'Sin stock'}</td> <!-- Stock -->
                </tr>`;
            tbody.innerHTML += fila; // Agregar cada fila a la tabla
        });
    })
    .catch(error => console.error('Error al cargar el archivo CSV:', error));
