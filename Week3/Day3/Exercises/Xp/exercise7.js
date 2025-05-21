const allBooks = [
  {
    title: "The Subtlle are of not give a Fack",
    author: "Manson",
    image: "https://www.shutterstock.com/shutterstock/photos/1214866222/display_1500/stock-photo-paris-france-oct-woman-unboxing-new-book-against-green-background-the-subtle-art-of-not-1214866222.jpg",
    alreadyRead: true
  },
  {
    title: "Dead Note",
    author: "Space Toon",
    image: "https://m.media-amazon.com/images/I/51HlcY7eauL._SY445_SX342_.jpg",
    alreadyRead: false
  }
];

const listSection = document.querySelector('.listBooks');

allBooks.forEach(book => {
  const bookDiv = document.createElement('div');

  const bookInfo = document.createElement('p');
  bookInfo.textContent = `${book.title} written by ${book.author}`;
  
  const img = document.createElement('img');
  img.src = book.image;
  img.style.width = '100px';

  bookDiv.appendChild(bookInfo);
  bookDiv.appendChild(img);

  listSection.appendChild(bookDiv);
});
