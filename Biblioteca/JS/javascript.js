fetch('../CSV/books.csv')
    .then(response => response.text())
    .then(data => {
        const filas = data.split("\n").slice(1);
        const tbody = document.querySelector('#tabla-libros tbody');
        
        filas.forEach(fila => {
            const [isbn, title, author, genre, stock] = fila.split(",");
            tbody.innerHTML += `
                <tr>
                    <td>${isbn || 'No code'}</td>
                    <td>${title || 'No title'}</td>
                    <td>${author || 'No author'}</td>
                    <td>${genre || 'No genre'}</td>
                    <td>${stock || 'Out of stock'}</td>
                </tr>`;
        });
    })
    .catch(() => console.error('Error: No se encontró el archivo csv.'));