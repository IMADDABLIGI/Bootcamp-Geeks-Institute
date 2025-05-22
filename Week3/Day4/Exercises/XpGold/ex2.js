const button = document.querySelector('input[type="button"]');
const select = document.getElementById('colorSelect');

button.addEventListener('click', removecolor);

function removecolor() {
  const selectedIndex = select.selectedIndex;
  if (selectedIndex !== -1) {
    select.remove(selectedIndex);
  }
}
