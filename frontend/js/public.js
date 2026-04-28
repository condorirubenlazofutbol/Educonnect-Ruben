document.addEventListener("DOMContentLoaded", () => {
    loadPublicLevels();
});

function loadPublicLevels() {
    const container = document.getElementById("levels-container");
    container.innerHTML = "";

    dummyLevels.forEach(level => {
        // Level header
        const levelDiv = document.createElement("div");
        levelDiv.className = "level-container";

        levelDiv.innerHTML = `
            <div class="level-header">
                <img src="${level.image}" alt="${level.name}" onerror="this.src='https://placehold.co/100x100/2980b9/FFF?text=Nivel'">
                <h2>${level.name}</h2>
            </div>
            <div class="modules-grid">
                ${level.modules.map(mod => `
                    <div class="module-card">
                        <img src="${mod.img}" alt="${mod.name}" onerror="this.src='https://placehold.co/300x160/34495e/FFF?text=Módulo+${mod.id}'">
                        <div class="module-info">
                            <h3>Módulo ${mod.id}</h3>
                            <p>${mod.name}</p>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;

        container.appendChild(levelDiv);
    });
}
