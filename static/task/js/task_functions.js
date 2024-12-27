// Funcion para desplegar descripcion de tarea oculta
function toggleDescription(taskId){
    console.log('hiciste click')
    const description = document.getElementById('description-' + taskId);
    if (description.style.display === 'none' || description.style.display === '') {
        description.style.display = 'block';
    } else {
        description.style.display = 'none';
    }   
}
    