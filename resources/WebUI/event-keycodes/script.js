const insert = document.getElementById('insert')

window.addEventListener('keydown', (event) => {
  insert.innerHTML = `
  <div class="key" data-filter-by="text" data-evalby="text|font-size|font-weight|color">
  ${event.key === ' ' ? 'Space' : event.key} 
  <small data-filter-by="has_text" data-evalby="text|font-size|font-weight|color">event.key</small>
</div>

<div class="key" data-filter-by="text" data-evalby="text|font-size|font-weight|color">
  ${event.keyCode}
  <small data-filter-by="has_text" data-evalby="text|font-size|font-weight|color">event.keyCode</small>
</div>

<div class="key" data-filter-by="has_text" data-evalby="text|font-size|font-weight|color">
  ${event.code}
  <small data-filter-by="text" data-evalby="text|font-size|font-weight|color">event.code</small>
</div>
  `
})