var tocContainer = document.getElementById('toc-container');
var headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');

headings.forEach(function(heading) {
    var tocLink = document.createElement('a');
    tocLink.textContent = heading.textContent;
    tocLink.setAttribute('href', '#' + heading.id);
    tocContainer.appendChild(tocLink);

    tocContainer.appendChild(document.createElement('br')); // Add line break
});

tocContainer.style.position = 'fixed';
tocContainer.style.top = '0';
tocContainer.style.left = '0';
