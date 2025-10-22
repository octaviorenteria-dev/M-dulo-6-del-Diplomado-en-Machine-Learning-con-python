async function callInference() { // función asíncrona 
    try {
        
        const data = { "image": document.getElementById('image').src };

        const response = await fetch('/inference', { // Hacer la petición al servidor en el path '/inference', le enviamos el path de la imagen como POST
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }); 
        if (response.ok) {
            const data = await response.json(); // esperar por la respuesta de Flask, el resultado es JSON
            
            // actualizar el texto del DIV con el resultado de la inferencia de la imágen.
            let score = 100*data.score.toFixed(2);
            document.getElementById('text').innerHTML = `<b>label:</b> ${data.label}</br><b>score:</b> ${score}%`; // El servidor regresa los datos como { "label": "text", "score": float }

        } else { // en caso de error
            console.error('Error calling /inference:', response.status);
            document.getElementById('text').textContent = "Error";
        }
    } catch (error) { // el path no responde o el servidor genera error inesperado
        console.error('Error calling /inference:', error);
        document.getElementById('text').textContent = "Error";
    }
}

function updateImage() {
    // Get the selected options
    var selectedOption = document.getElementById("images").options[document.getElementById("images").selectedIndex];
    
    // Set the src of the image
    document.getElementById("image").src = `static/images/${selectedOption.value}`;
    document.getElementById('text').innerHTML="what class is it?";

  }
