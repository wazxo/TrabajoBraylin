const icon = document.getElementById("toggler");
const nav = document.getElementById("navbar");

// Funciones
nav.style.display = "none"; // Oculta la navegación inicialmente

const showNav = (e) => {
  e.target.parentElement.classList.toggle("change-backGround"); // Cambia el fondo del contenedor
  e.target.classList.toggle("clicked"); // Cambia el estado del icono

  // setTimeout para animaciones suaves
  e.target.classList.contains("clicked")
    ? ((nav.style.cssText = "display: flex;"), // Corrige el error tipográfico aquí
      setTimeout(() => (nav.style.transform = "translateY(0)"), 300))
    : ((nav.style.transform = "translateY(-100%)"),
      setTimeout(() => (nav.style.display = "none"), 700));
};

// Eventos
icon.addEventListener("click", showNav);
