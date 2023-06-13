from bs4 import BeautifulSoup

with open('ptrr.html', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

paragraphs = soup.find_all('p')
for index, paragraph in enumerate(paragraphs, start=1):
    paragraph['id'] = f'para_{index}'

with open('testing_p_tags.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())