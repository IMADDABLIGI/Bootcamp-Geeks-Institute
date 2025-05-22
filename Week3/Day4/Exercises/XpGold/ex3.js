let shoppingList = [];

const root = document.getElementById('root');
const form = document.createElement('form');

const input = document.createElement('input');
input.type = 'text';
input.placeholder = 'Add item';

const addButton = document.createElement('button');
addButton.type = 'submit';
addButton.textContent = 'AddItem';

form.appendChild(input);
form.appendChild(addButton);
root.appendChild(form);

const clearButton = document.createElement('button');
clearButton.textContent = 'ClearAll';
root.appendChild(clearButton);

const list = document.createElement('ul');
root.appendChild(list);

function addItem(e) {
  e.preventDefault();
  const item = input.value.trim();
  if (item !== '') {
    shoppingList.push(item);
    renderList();
    input.value = '';
  }
}

function clearAll() {
  shoppingList = [];
  renderList();
}

function renderList() {
  list.innerHTML = '';
  shoppingList.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    list.appendChild(li);
  });
}

form.addEventListener('submit', addItem);
clearButton.addEventListener('click', clearAll);
