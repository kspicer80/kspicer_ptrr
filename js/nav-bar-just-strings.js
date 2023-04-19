// Select all the headings that should be included in the table of contents
const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');

// Initialize the table of contents string
let tocString = '';

// Loop through the headings and add each one to the table of contents string
headings.forEach((heading) => {
  // Get the heading's text content and ID
  const text = heading.textContent;
  const id = heading.getAttribute('id');

  // Get the level of the heading
  const level = parseInt(heading.tagName.substring(1));

  // Add the heading to the table of contents string
  tocString += `${'  '.repeat(level-1)}${text}\n`;
});

// Get the div element with class "toc" inside the nav element
const toc = document.querySelector('nav .hover-content div.toc');

// Set the inner HTML of the div to the table of contents string
toc.innerHTML = tocString;
