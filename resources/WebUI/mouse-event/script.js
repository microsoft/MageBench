const containerEl = document.querySelector(".container");

window.addEventListener("mousemove", (event) => {
  containerEl.innerHTML = `
        <div class="mouse-event" data-filter-by="border" data-evalby="border|margin|min-width|min-height|position|justify-content|align-items|display|font-size">
        <span data-filter-by="text" data-evalby="font-size|font-weight|color">${event.clientX}</span>
        <h4 data-filter-by="text" data-evalby="font-size|font-weight|color">Mouse X Prosition(px)</h4>
      </div>
      <div class="mouse-event" data-filter-by="border" data-evalby="border|margin|min-width|min-height|position|justify-content|align-items|display|font-size">
        <span data-filter-by="text" data-evalby="font-size|font-weight|color">${event.clientY}</span>
        <h4 data-filter-by="text" data-evalby="font-size|font-weight|color">Mouse Y Prosition(px)</h4>
      </div>
  `;
});