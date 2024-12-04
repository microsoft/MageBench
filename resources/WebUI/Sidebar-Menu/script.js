document.querySelector(".hamburger-menu").addEventListener("click", () => {
  document.querySelector(".container").classList.toggle("change");
});

document.querySelector(".nav-list").addEventListener("click", e => {
  const el = e.target.parentNode;

  console.log(el);

  if (el.classList[0] === "nav-link") {
    el.nextElementSibling.classList.toggle("change");
    el.classList.toggle("change");
  }
});
