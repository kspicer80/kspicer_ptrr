// Select all the headings that should be included in the table of contents
const headings = document.querySelectorAll('h1');

// Create a new ordered list element to hold the table of contents
const ol = document.createElement('ol');

// Loop through the headings and create a list item with a link for each one
headings.forEach((heading) => {
  // Get the heading number and text content
  const number = heading.textContent.match(/^\d+/);
  const text = heading.textContent;

  // Create a new list item with a link to the heading
  const li = document.createElement('li');
  const a = document.createElement('a');
  a.textContent = `${number} ${text}`;
  a.href = `#${heading.id}`;

  // Add the link to the list item and the list item to the ordered list
  li.appendChild(a);
  ol.appendChild(li);
});

// Get the ol element with class "toc" inside the nav element
const toc = document.querySelector('nav .hover-content ol.toc');

// Replace the contents of the existing ol element with the new one
toc.innerHTML = ol.innerHTML;
