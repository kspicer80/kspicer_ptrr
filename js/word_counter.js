window.addEventListener('DOMContentLoaded', function () {
    var bodyText = document.body.innerText;
    var wordCount = bodyText.trim().split(/\s+/).length;
    var wordCountElement = document.getElementById('wordCount');
    wordCountElement.textContent = 'The word count for this document is: ' + wordCount + '.';
  });