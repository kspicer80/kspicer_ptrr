var toc = document.getElementById('table-of-contents');
var headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');

headings.forEach(function(heading) {
    var tocLink = document.createElement('a');
    tocLink.textContent = heading.textContent;
    tocLink.setAttribute('href', '#' + heading.id);
    toc.appendChild(tocLink);

    toc.appendChild(document.createElement('br')); // Add line break
});
