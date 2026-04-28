document.addEventListener("DOMContentLoaded", () => {
    cargarModulos();
});

let modulosCargados = [];
let moduloActualEdicion = null;
let contenidosActuales = [];

async function cargarModulos() {
    try {
        const response = await fetch(`${API_URL}/modulos/`);
        if (response.ok) {
            const data = await response.json();
            modulosCargados = data.modulos;
            renderTable(modulosCargados);
        }
    } catch (error) {
        console.error("No se pudo conectar al backend:", error);
    }
}

function renderTable(modulos) {
    const tbody = document.getElementById("tabla-modulos");
    tbody.innerHTML = "";

    if (modulos.length === 0) {
        tbody.innerHTML = `<tr><td colspan="4" style="padding:10px; text-align:center;">Base de datos vacía. Sube los cambios y ejecuta "python seed_modulos.py" en Render.</td></tr>`;
        return;
    }

    modulos.forEach(mod => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td style="padding: 10px; border: 1px solid #ddd;">${mod.id}</td>
            <td style="padding: 10px; border: 1px solid #ddd;"><strong>${mod.nombre}</strong></td>
            <td style="padding: 10px; border: 1px solid #ddd;">${mod.nivel} <br><small>${mod.subnivel || ''}</small></td>
            <td style="padding: 10px; border: 1px solid #ddd;">
                <button onclick="abrirEditorContenido(${mod.id}, '${mod.nombre}')" style="background:#2980b9;color:white;border:none;padding:5px 10px;border-radius:5px;cursor:pointer;">Agregar Material</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

async function mostrarModalModulo() {
    alert("Como ya se cargarán los 20 módulos directamente, no necesitas esta función por el momento.");
}

// Ventana Emergente
async function abrirEditorContenido(mod_id, mod_nombre) {
    moduloActualEdicion = mod_id;
    document.getElementById("modal-titulo").innerText = "Añadiendo Material: " + mod_nombre;
    const body = document.getElementById("modal-body");
    body.innerHTML = "<em>Cargando recursos...</em>";
    document.getElementById("modal-contenido").style.display = "flex";

    try {
        const res = await fetch(`${API_URL}/modulos/${mod_id}/contenidos`);
        const data = await res.json();
        contenidosActuales = data.contenidos;

        body.innerHTML = "";
        if (contenidosActuales.length === 0) {
            body.innerHTML = "<p>No hay ranuras de contenido para este módulo (Deberías ejecutar seed_modulos.py)</p>";
            return;
        }

        contenidosActuales.forEach(cont => {
            const div = document.createElement("div");
            div.style.marginBottom = "10px";
            div.innerHTML = `
                <label style="display:block; font-weight:bold; margin-bottom:5px;">${cont.titulo} (${cont.tipo.toUpperCase()})</label>
                <input type="text" id="cont-${cont.id}" value="${cont.url || ''}" placeholder="Pega el enlace web aquí..." style="width:100%; padding:8px; border:1px solid #ccc; border-radius:4px;">
            `;
            body.appendChild(div);
        });

    } catch (e) {
        body.innerHTML = "<p>Error al cargar el contenido.</p>";
    }
}

function cerrarModal() {
    document.getElementById("modal-contenido").style.display = "none";
}

async function guardarContenidos() {
    const token = localStorage.getItem("token");
    let errores = 0;

    for (let cont of contenidosActuales) {
        const nuevaUrl = document.getElementById(`cont-${cont.id}`).value;
        // Solo actualizamos si cambió algo y no está vacío
        if (nuevaUrl !== undefined) {
            const formData = new URLSearchParams();
            formData.append("url", nuevaUrl);
            try {
                const res = await fetch(`${API_URL}/modulos/contenidos/${cont.id}?url=${encodeURIComponent(nuevaUrl)}`, {
                    method: "PUT",
                    headers: {
                        "Authorization": `Bearer ${token}`
                    }
                });
                if (!res.ok) errores++;
            } catch (e) {
                errores++;
            }
        }
    }

    if (errores > 0) {
        alert("Ocurrió un pequeño error al guardar algunos datos, verifica tu sesión.");
    } else {
        alert("¡Enlaces y materiales guardados correctamente en la Nube!");
        cerrarModal();
    }
}
