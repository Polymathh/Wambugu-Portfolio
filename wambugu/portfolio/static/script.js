document.addEventListener("DOMContentLoaded", () => {
  const words = [
      "A Web Developer",
      "A Mobile App Developer",
      "A Digital Marketer"
  ];
  
  let index = 0;
  let charIndex = 0;
  let currentWord = "";
  const typeSpeed = 100;
  const eraseSpeed = 50;
  const delayBetweenWords = 1500;

  const typewriterElement = document.querySelector(".typewriter");

  function type() {
      if (charIndex < words[index].length) {
          currentWord += words[index].charAt(charIndex);
          typewriterElement.textContent = currentWord;
          charIndex++;
          setTimeout(type, typeSpeed);
      } else {
          setTimeout(erase, delayBetweenWords);
      }
  }

  function erase() {
      if (charIndex > 0) {
          currentWord = currentWord.slice(0, -1);
          typewriterElement.textContent = currentWord;
          charIndex--;
          setTimeout(erase, eraseSpeed);
      } else {
          index = (index + 1) % words.length;
          setTimeout(type, typeSpeed);
      }
  }

  if (typewriterElement) {
      setTimeout(type, 500);
  }


  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");

  // Toggle the menu when the hamburger is clicked
  navToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
  });

  // Close the menu when any link is clicked
  navLinks.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
          navLinks.classList.remove("active");
      });
  });

});

