let result = document.querySelector(".result-btn");

result.addEventListener("click", decimal);

function decimal() {
  let decimal = document.getElementById("number").value;
  let tempDecimal;
  let rem = 0;
  let binary = 0;
  let place = 1;

  tempDecimal = decimal;

  while (tempDecimal > 0) {
    rem = tempDecimal % 2;
    binary = binary + rem * place;
    tempDecimal = parseInt(tempDecimal / 2);
    place = place * 10;
  }

  const h1 = document.createElement("h1");
  h1.innerHTML = `${binary}`;
  h1.setAttribute("data-filter-by", "text");
  h1.setAttribute("data-evalby", "font-size|font-weight|color");

  const container = document.querySelector(".results-container");
  container.append(h1);
}