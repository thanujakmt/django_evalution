function handleAppIcon(){
    let icon_wrapper = document.getElementById('icon_wrapper')
    let imageTag = document.getElementById('app_icon_image')
    let app_icon_input = document.getElementById('app_icon')
    console.log(icon_wrapper)
    icon_wrapper.addEventListener('click',() =>{
        // let app_icon_input = document.getElementById('app_icon')
        app_icon_input.click()
        console.log('click')
    })

    app_icon_input.addEventListener('change',(e) =>{
        const file  = e.target.files[0]
        

       
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imageTag.src = e.target.result;
                console.log(imageTag)
                // imageTag.style.display = 'block';
                // imagePreview.style.backgroundImage = url(${e.target.result});
            };
            reader.readAsDataURL(file);
        }
    })

    icon_wrapper.addEventListener('dragover', function (e) {
        e.preventDefault();
        e.stopPropagation();
        e.target.classList.add('bg_color');
    });

    icon_wrapper.addEventListener('dragleave', function (e) {
        e.preventDefault();
        e.stopPropagation();
        e.target.classList.remove('bg_color');
    });

    icon_wrapper.addEventListener('drop',(e) =>{
        e.preventDefault();
        e.stopPropagation();
        e.target.classList.remove('bg_color');
        const file = e.dataTransfer.files[0]

        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imageTag.src = e.target.result;

            };
            reader.readAsDataURL(file);

            app_icon_input.files = e.dataTransfer.files;
        }
    })



}

handleAppIcon()