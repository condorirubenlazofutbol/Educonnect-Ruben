const API_URL = "https://sistemas-informaticos-backend.onrender.com";

// Dummy data to populate public view before actual DB response
const dummyLevels = [
    {
        id: "basico",
        name: "Nivel Técnico Básico",
        image: "images/basico.png",
        modules: [
            { id: 1, name: "Taller de Sistemas Operativos I", img: "images/basico-M1.png" },
            { id: 2, name: "Matemática para la Informática", img: "images/basico-M2.png" },
            { id: 3, name: "Programación I-A", img: "images/basico-M3.png" },
            { id: 4, name: "Hardware de Computadoras I", img: "images/basico-M4.png" },
            { id: 5, name: "Emergente", img: "images/basico-M5.png" }
        ]
    },
    {
        id: "auxiliar",
        name: "Nivel Técnico Auxiliar",
        image: "images/auxiliar.png",
        modules: [
            { id: 6, name: "Taller de Sistemas Operativos II", img: "images/auxiliar-M6.png" },
            { id: 7, name: "Ofimática y Tecnología Multimedia I", img: "images/auxiliar-M7.png" },
            { id: 8, name: "Programación I-B", img: "images/auxiliar-M8.png" },
            { id: 9, name: "Hardware de Computadoras II", img: "images/auxiliar-M9.png" },
            { id: 10, name: "Emergente", img: "images/auxiliar-M10.png" }
        ]
    },
    {
        id: "medio1",
        name: "Nivel Técnico Medio I",
        image: "images/medio.png",
        modules: [
            { id: 11, name: "Inglés Técnico", img: "images/medio1-M11.png" },
            { id: 12, name: "Diseño y Programación Web I-A", img: "images/medio1-M12.png" },
            { id: 13, name: "Programación I-C", img: "images/medio1-M13.png" },
            { id: 14, name: "Ofimática y Tecnología Multimedia II", img: "images/medio1-M14.png" },
            { id: 15, name: "Emprendimiento Productivo", img: "images/medio1-M15.png" }
        ]
    },
    {
        id: "medio2",
        name: "Nivel Técnico Medio II",
        image: "images/medio.png",
        modules: [
            { id: 16, name: "Redes de Computadoras I", img: "images/medio2-M16.png" },
            { id: 17, name: "Diseño y Programación Web I-B", img: "images/medio2-M17.png" },
            { id: 18, name: "Base de Datos I", img: "images/medio2-M18.png" },
            { id: 19, name: "Programación Móvil I", img: "images/medio2-M19.png" },
            { id: 20, name: "Modalidades de Graduación", img: "images/medio2-M20.png" }
        ]
    }
];

function triggerNotification(msg, type = 'success') {
    alert(`${type.toUpperCase()}: ${msg}`);
}
