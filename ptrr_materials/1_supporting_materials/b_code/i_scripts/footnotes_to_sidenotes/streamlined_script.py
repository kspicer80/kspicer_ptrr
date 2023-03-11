import re

markdown_file_path = '/Users/spicy.kev/Library/CloudStorage/GoogleDrive-kspicer@stfrancis.edu/My Drive/post_tenure/ptrr.md'

with open(markdown_file_path, 'r') as f:
    markdown_text = f.read()

footnote_pattern = r"\[\^(\d+)\]"
footnote_matches = re.findall(footnote_pattern, markdown_text)
footnote_string = ", ".join(["[^" + match + "]" for match in footnote_matches])

footnote_text_pattern = r"\[\^(\d+)\]:\s*(.*?);[\n\s]*&nbsp;\s*(.*?)\n"
footnotes = re.findall(r'\[\^(\d+)\]:&nbsp;(.*?)(?=\n\[|$)', markdown_text, re.DOTALL)
fn_dictionary = {}
for footnote in footnotes:
    number = footnote[0]
    number_string = f'[^{number}]'
    text = footnote[1].strip()
    fn_dictionary[number_string] = text

#print(fn_dictionary)

html_template = '<label for="sn-{num}" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-{num}" class="margin-toggle"/><span class="sidenote" id="{num}">{text}</span>'

for key, value in fn_dictionary.items():
    html = html_template.format(num=key[2:-1], text=value)
    try:
        markdown_text = re.sub(re.escape(key), html, markdown_text)
    except re.error as e:
        print(f"Error: {e}, Key: {key}, Value: {value}")

with open('streamlined_version.md', 'w') as outfile:
    outfile.write(markdown_text)
