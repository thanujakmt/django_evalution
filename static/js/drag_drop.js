
document.addEventListener('DOMContentLoaded', function () {
    const dropArea = document.getElementById('drop-area');
    if (dropArea) {
        dropArea.addEventListener('dragover', function (e) {
            e.preventDefault();
            e.stopPropagation();
            e.target.classList.add('bg_color');
        });

        dropArea.addEventListener('dragleave', function (e) {
            e.preventDefault();
            e.stopPropagation();
            e.target.classList.remove('bg_color');
        });

        dropArea.addEventListener('drop', function (e) {
            e.preventDefault();
            e.stopPropagation();
            let id = dropArea.getAttribute('aria-label')
            e.target.classList.remove('bg_color');
            let files = e.dataTransfer.files;
            handleFiles(files,id);
            console.log(files)
        });
    } else {
        console.error("Element with id 'drop-area' not found.");
    }
});

const update_image = (imageUrl) =>{
    let dropArea = document.getElementById('drop-area')
    let imageTag = `<img style = "max-width:400px;" src='${imageUrl}' >`
    dropArea.innerHTML = imageTag

}

function handleFiles(files,id) {
    let formData = new FormData();
    formData.append('image', files[0]);
    console.log(formData)

    fetch(`/upload/${id}`, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    }).then(response => {
        if (response.ok) {
            
            return response.json()
            alert('Image uploaded successfully!');
           
        } else {
            alert('Image upload failed!');
        }
    })
    .then(data =>(
        update_image(data.image)
    ));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

