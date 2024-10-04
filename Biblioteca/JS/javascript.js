function csvToArray(csv) {
    const rows = csv.trim().split("\n").slice(1);
    return rows.map(row => row.split(","));
}

fetch('../CSV/books.csv')
    .then(response => response.text())
    .then(data => {
        const libros = csvToArray(data);
        const tbody = document.querySelector('#tabla-libros tbody');
        
        libros.forEach(libro => {
            const fila = `
                <tr>
                    <td>${libro[0] || 'Sin ISBN'}</td> <!-- ISBN-13 -->
                    <td>${libro[1] || 'Sin título'}</td> <!-- Título -->
                    <td>${libro[2] || 'Sin autor'}</td> <!-- Autor -->
                    <td>${libro[3] || 'Sin género'}</td> <!-- Género -->
                    <td>${libro[4] || 'Sin stock'}</td> <!-- Stock -->
                </tr>`;
            tbody.innerHTML += fila;
        });
    })
    .catch(error => console.error('Error al cargar el archivo CSV:', error));
