const menuIcon = document.getElementById("mobileOpen");
const mobileMenu = document.getElementById("mobileMenu");

document.addEventListener("click", function (event) {
  if (mobileMenu) {
    if (event.target !== mobileMenu && event.target !== menuIcon) {
      mobileMenu.classList.remove("close");
    }
  }
});

function menuHandler(event) {
  event.stopPropagation();
  if (mobileMenu.classList.contains("close")) {
    console.log("hey");
    mobileMenu.classList.remove("close");
  } else {
    console.log("hai");
    mobileMenu.classList.add("close");
  }
}

function showContent(event,contentType) {
  event.preventDefault();
  const contentSections = document.querySelectorAll(".items_displayed");
  contentSections.forEach((section) => {
    if (section.id === `${contentType}Content`) {
      section.classList.remove("hidden_1");
    } else {
      section.classList.add("hidden_1");
    }
  });
  const headings = document.querySelectorAll(".items_h");
  headings.forEach((heading) => {
    if (heading.id === `${contentType}Heading`) {
      heading.classList.add("heading_o");
    } else {
      heading.classList.remove("heading_o");
    }
  });
  headingChanger(contentType);
}

function headingChanger(name) {
  const h = document.getElementById("porductName");
  const capitalizedName =
    name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  h.textContent = capitalizedName;
}

$(".owl-carousel").owlCarousel({
loop: true,
center: true,
items: 1,
autoplay: true,
autoplayTimeout: 2000,
autoplayHoverPause: true,
dots: true,
});
