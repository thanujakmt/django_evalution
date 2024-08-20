
document.addEventListener('DOMContentLoaded', function () {
    const dropArea = document.getElementById('drop-area');
    if (dropArea) {
        dropArea.addEventListener('dragover', function (e) {
            e.preventDefault();
            e.stopPropagation();
            e.target.classList.add('bg-gray-100');
        });

        dropArea.addEventListener('dragleave', function (e) {
            e.preventDefault();
            e.stopPropagation();
            e.target.classList.remove('bg-gray-100');
        });

        dropArea.addEventListener('drop', function (e) {
            e.preventDefault();
            e.stopPropagation();
            e.target.classList.remove('bg-gray-100');
            let files = e.dataTransfer.files;
            // handleFiles(files);
        });
    } else {
        console.error("Element with id 'drop-area' not found.");
    }
});
