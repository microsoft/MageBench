const monthEl = document.querySelector(".date h1");
const fullDateEl = document.querySelector(".date p");
const daysEl = document.querySelector(".days");

const monthInx = new Date().getMonth();
const lastDay = new Date(new Date().getFullYear(), monthInx + 1, 0).getDate();
const firstDay = new Date(new Date().getFullYear(), monthInx, 1).getDay() - 1;

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

monthEl.innerText = months[monthInx];
fullDateEl.innerText = new Date().toDateString();

let days = "";

for (let i = firstDay; i > 0; i--) {
  days += `<div class="empty" data-filter-by="background-color" data-evalby="background-color|width|height|display|justify-content|align-items"></div>`;
}
for (let i = 1; i <= lastDay; i++) {
  if (i === new Date().getDate()) {
    days += `<div class="today" data-filter-by="background-color" data-evalby="background-color|width|height|display|justify-content|align-items">${i}</div>`;
  } else {
    days += `<div data-filter-by="background-color" data-evalby="background-color|width|height|display|justify-content|align-items">${i}</div>`;
  }
}

daysEl.innerHTML = days;