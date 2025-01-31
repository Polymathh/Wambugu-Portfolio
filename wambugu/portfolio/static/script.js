const words = [
    "A Web Developer",
    "A Mobile App Developer",
    "A Digital Marketer"
  ];
  
  let index = 0;
  let charIndex = 0;
  let currentWord = "";
  const typeSpeed = 100; // Speed of typing
  const eraseSpeed = 50; // Speed of erasing
  const delayBetweenWords = 1500; // Delay before switching words
  
  const typewriterElement = document.querySelector(".typewriter");
  
  function type() {
    if (charIndex < words[index].length) {
      currentWord += words[index].charAt(charIndex);
      typewriterElement.innerHTML = currentWord;
      charIndex++;
      setTimeout(type, typeSpeed);
    } else {
      setTimeout(erase, delayBetweenWords);
    }
  }
  
  function erase() {
    if (charIndex > 0) {
      currentWord = currentWord.slice(0, -1);
      typewriterElement.innerHTML = currentWord;
      charIndex--;
      setTimeout(erase, eraseSpeed);
    } else {
      index = (index + 1) % words.length; // Move to the next word
      setTimeout(type, typeSpeed);
    }
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    setTimeout(type, 500);
  });
  