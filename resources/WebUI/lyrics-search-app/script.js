const form = document.getElementById("form");
const search = document.getElementById("search");
const result = document.getElementById("result");
const more = document.getElementById("more");

const apiURL = "https://api.lyrics.ovh";

async function searchSongs(term) {
  const res = await fetch(`${apiURL}/suggest/${term}`);
  const data = await res.json();
  showData(data);
}

async function getLyrics(artist, songTitle) {
  const res = await fetch(`${apiURL}/v1/${artist}/${songTitle}`);
  const data = await res.json();
  console.log(artist, songTitle);
  if (data.error) {
    showAlert(data.error);
  } else {
    const lyrics = data.lyrics.replace(/(\r\n|\r|\n)/g, "<br>");

    result.innerHTML = `
        <h2 data-filter-by="text" data-evalby="font-size|font-weight|color"><strong>${artist}</strong> - ${songTitle}</h2>
        <span data-filter-by="text" data-evalby="font-size|font-weight|color">${lyrics}</span>
    `;
  }
  more.innerHTML = "";
}

async function getMoreSongs(url) {
  const res = await fetch(`https://cors-anywhere.herokuapp.com/${url}`); // proxy is required to avoid CORS issue
  const data = await res.json();
  showData(data);
}

function showData(data) {
  result.innerHTML = `
    <ul class="songs">
      ${data.data
        .map(
          (song) => `<li>
      <span data-filter-by="text" data-evalby="font-size|font-weight|color"><strong>${song.artist.name}</strong> - ${song.title}</span>
      <button class="btn" data-artist="${song.artist.name}" data-songtitle="${song.title}" data-filter-by="text" data-evalby="font-size|padding|background-color|border-radius">Get Lyrics</button>
    </li>`
        )
        .join("")}
    </ul>
    `;
  // Pagination
  if (data.prev || data.next) {
    more.innerHTML = `
                    ${
                      data.prev
                        ? `<button class="btn" onclick="getMoreSongs('${data.prev}')" data-filter-by="text" data-evalby="font-size|padding|background-color|border-radius">Prev</button>`
                        : ""
                    }
                    ${
                      data.next
                        ? `<button class="btn" onclick="getMoreSongs('${data.next}')" data-filter-by="text" data-evalby="font-size|padding|background-color|border-radius">Next</button>`
                        : ""
                    }
                    `;
  } else more.innerHTML = "";
}

function showAlert(message) {
  const notif = document.createElement("div");
  notif.classList.add("toast");
  notif.innerText = message;
  notif.setAttribute("data-filter-by", "text");
  notif.setAttribute("data-evalby", "font-size|padding|background-color|border-radius|color");
  document.body.appendChild(notif);
  setTimeout(() => notif.remove(), 3000);
}

// Event Listeners
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const searchTerm = search.value.trim();
  if (!searchTerm) showAlert("Please type in a search term");
  else searchSongs(searchTerm);
});
result.addEventListener("click", (e) => {
  const clickedElement = e.target;
  if (clickedElement.tagName === "BUTTON") {
    const artist = clickedElement.getAttribute("data-artist");
    const songTitle = clickedElement.getAttribute("data-songtitle");
    getLyrics(artist, songTitle);
  }
});

// Init
searchSongs("one");