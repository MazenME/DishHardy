let confirmed;


function deleteRecipe(button) {
    confirmed = confirm("Are you sure you want to delete this Recipe?");
    if (!confirmed) {
        event.preventDefault();
    }
}