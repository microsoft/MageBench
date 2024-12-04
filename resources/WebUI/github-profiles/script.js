const APIURL = 'https://api.github.com/users/'

const main = document.getElementById('main')
const form = document.getElementById('form')
const search = document.getElementById('search')

async function getUser(username) {
    try {
        const { data } = await axios(APIURL + username)

        createUserCard(data)
        getRepos(username)
    } catch(err) {
        if(err.response.status == 404) {
            createErrorCard('No profile with this username')
        }
    }
}

async function getRepos(username) {
    try {
        const { data } = await axios(APIURL + username + '/repos?sort=created')

        addReposToCard(data)
    } catch(err) {
        createErrorCard('Problem fetching repos')
    }
}

function createUserCard(user) {
    const userID = user.name || user.login
    const userBio = user.bio ? `<p data-filter-by="has_text" data-evalby="color|margin">${user.bio}</p>` : ''
    const cardHTML = `
    <div class="card" data-filter-by="background-color" data-evalby="background-color|border-radius|box-shadow|padding|margin">
    <div>
      <img src="${user.avatar_url}" alt="${user.name}" class="avatar" data-filter-by="src" data-evalby="border-radius|border|height|width">
    </div>
    <div class="user-info" data-filter-by="color" data-evalby="color|margin-left">
      <h2 data-filter-by="has_text" data-evalby="margin-top">${userID}</h2>
      ${userBio}
      <ul data-filter-by="display" data-evalby="list-style-type|display|justify-content|padding|max-width">
        <li data-filter-by="has_text" data-evalby="display|align-items">${user.followers} <strong data-filter-by="has_text" data-evalby="font-size|margin-left">Followers</strong></li>
        <li data-filter-by="has_text" data-evalby="display|align-items">${user.following} <strong data-filter-by="has_text" data-evalby="font-size|margin-left">Following</strong></li>
        <li data-filter-by="has_text" data-evalby="display|align-items">${user.public_repos} <strong data-filter-by="has_text" data-evalby="font-size|margin-left">Repos</strong></li>
      </ul>

      <div id="repos" data-filter-by="has_text" data-evalby="display|align-items"></div>
    </div>
  </div>
    `
    main.innerHTML = cardHTML
    
}

function createErrorCard(msg) {
    const cardHTML = `
        <div class="card" data-filter-by="background-color" data-evalby="background-color|border-radius|box-shadow|padding|margin">
            <h1 data-filter-by="has_text" data-evalby="font-size|color">${msg}</h1>
        </div>
    `

    main.innerHTML = cardHTML
}

function addReposToCard(repos) {
    const reposEl = document.getElementById('repos')

    repos
        .slice(0, 5)
        .forEach(repo => {
            const repoEl = document.createElement('a')
            repoEl.classList.add('repo')
            repoEl.href = repo.html_url
            repoEl.target = '_blank'
            repoEl.innerText = repo.name
            repoEl.setAttribute('data-filter-by', 'has_text')
            repoEl.setAttribute('data-evalby', 'text-decoration|color|background-color|font-size|padding|margin-right|margin-bottom|display')

            reposEl.appendChild(repoEl)
        })
}

form.addEventListener('submit', (e) => {
    e.preventDefault()

    const user = search.value

    if(user) {
        getUser(user)

        search.value = ''
    }
})