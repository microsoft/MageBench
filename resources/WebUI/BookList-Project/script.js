const title = document.getElementById("title");
const author = document.getElementById("author");
const year = document.getElementById("year");
const bookList = document.getElementById("book-list");
const btn = document.querySelector(".btn");

btn.addEventListener("click", function (e) {
  e.preventDefault();

  if (title.value == "" && author.value == "" && year.value == "") {
    alert("Fill The Form");
  } else {
    const newRow = document.createElement("section");

    // Creating new Title
    const newTitle = document.createElement("div");
    newTitle.innerHTML = title.value;
    newTitle.setAttribute("data-filter-by", "has_text");
    newTitle.setAttribute("data-evalby", "font-size|font-weight|color|background");
    newRow.appendChild(newTitle);

    // Creating new Author
    const newAuthor = document.createElement("div");
    newAuthor.innerHTML = author.value;
    newAuthor.setAttribute("data-filter-by", "has_text");
    newAuthor.setAttribute("data-evalby", "font-size|font-weight|color|background");
    newRow.append(newAuthor);

    // Creating new Year
    const newYear = document.createElement("div");
    newYear.innerHTML = year.value;
    newYear.setAttribute("data-filter-by", "has_text");
    newYear.setAttribute("data-evalby", "font-size|font-weight|color|background");
    newRow.appendChild(newYear);

    bookList.appendChild(newRow);
  }
});