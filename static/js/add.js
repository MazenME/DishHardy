let ingredientCounter = 1;
let ingredientSection = document.getElementById('ingredient-section');
let newIngredientContainer;
let confirmed;
let ingredientContainer;


if (ingredientCounter < 2) {
    document.getElementById("ingredient-delete").style.display = "none";
}

function addIngredient() {
    ingredientCounter++;
    newIngredientContainer = document.createElement('div');
    newIngredientContainer.classList.add('ingredient-container');
    newIngredientContainer.innerHTML = `
        <input type="text" id="ingredient-name-${ingredientCounter}" name="ingredient-name[]" placeholder="Ingredient Name" required>
        <input type="number" id="ingredient-quantity-${ingredientCounter}" name="ingredient-quantity[]" placeholder="Quantity" required>
        <input type="text" id="ingredient-unit-${ingredientCounter}" name="ingredient-unit[]" placeholder="Unit" required>
        <button type="button" class="ingredient-delete" onclick="deleteIngredient(this)">Delete</button>
    `;
    ingredientSection.appendChild(newIngredientContainer);
    if (ingredientCounter > 1) {
        const deleteButtons = document.querySelectorAll('.ingredient-delete');
        deleteButtons.forEach(button => button.style.display = 'inline-block');
    }
}

function deleteIngredient(button) {
    confirmed = confirm("Are you sure you want to delete this ingredient?");
    if (!confirmed) {
        return;
    }
    ingredientContainer = button.parentElement;
    ingredientContainer.remove();
    ingredientCounter--;
    if (ingredientCounter < 2) {
        const deleteButtons = document.querySelectorAll('.ingredient-delete');
        deleteButtons.forEach(button => button.style.display = 'none');
    }
}
