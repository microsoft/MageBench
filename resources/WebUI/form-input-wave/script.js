const labels = document.querySelectorAll('.form-control label')

labels.forEach(label => {
    label.innerHTML = label.innerText
        .split('')
        .map((letter, idx) => `<span style="transition-delay:${idx * 50}ms" data-filter-by="has_text" data-evalby="transition-delay">${letter}</span>`)
        .join('')
})