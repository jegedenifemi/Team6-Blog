// Initialize Swiper (carousel)
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  cssMode: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  mousewheel: true,
  keyboard: true,
});

// Change favicon with theme
lightSchemeIcon = document.querySelector("link#fav-green");
darkSchemeIcon = document.querySelector("link#fav-white");

function onUpdate() {
  if (matcher.matches) {
    lightSchemeIcon.remove();
    document.head.append(darkSchemeIcon);
  } else {
    document.head.append(lightSchemeIcon);
    darkSchemeIcon.remove();
  }
}

matcher = window.matchMedia("(prefers-color-scheme: dark)");
matcher.addListener(onUpdate);
onUpdate();

// SIGNUP MODAL
// let modalClose = document.querySelector(".close");
// let signupModal = document.querySelector(".signup-modal");

// function removeModal() {
//   console.log("wyd bro");
//   // signupModal[0].style.cursor = "pointer";
//   signupModal[0].style.display = "none";
// }
// modalClose.onclick = () => {
//   signupModal[0].style.display = "none";
// };

// modalClose.onclick = removeModal();

// MOBILE MENU
let burgerBtn = document.querySelectorAll(".hamburger");
let burgerMenu = document.querySelectorAll(".mobile_menu");

// function showMenu(event) {
//   console.log(22);
//   burgerMenu[0].style.display = "block";
// }

burgerBtn[0].onclick = function showMenu() {
  document.querySelectorAll(".fa-magnifying-glass")[1].style.display = "none";
  document.querySelectorAll(".fa-magnifying-glass")[1].style.transition =
    "30s ease-in-out";
  burgerMenu[0].style.display = "block";
  burgerMenu[0].style.animation = "mobilemenushow .3s";
  burgerMenu[0].style.transition = ".5s ease";
};

// function showMenu(event) {
//   console.log(22);
//   burgerMenu[0].style.display = "block";
// }
