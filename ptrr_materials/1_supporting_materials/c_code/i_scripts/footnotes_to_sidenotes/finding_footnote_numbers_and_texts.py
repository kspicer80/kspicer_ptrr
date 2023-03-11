import re

markdown_file_path = '/Users/spicy.kev/Library/CloudStorage/GoogleDrive-kspicer@stfrancis.edu/My Drive/post_tenure/ptrr.md'

with open(markdown_file_path, 'r') as f:
    markdown_text = f.read()

#footnote_number_pattern = r"\[\^(\d+)\]"
#footnote_number_matches = re.findall(footnote_number_pattern, test_string)
#print(footnote_number_matches)

footnote_pattern = r"\[\^(\d+)\]"
footnote_matches = re.findall(footnote_pattern, markdown_text)
footnote_string = ", ".join(["[^" + match + "]" for match in footnote_matches])
#print(footnote_string)

#footnote_text_pattern = r"\[\^(\d+)\]:\s*(.*?)(?:\n|\s*;?\s*&nbsp;)(.*)"
#footnote_text_pattern = r"\[\^(\d+)\]:\s*(.*?)\s*;?\s*&nbsp;(.*)"
#footnote_text_pattern = r"\[\^(\d+)\]:\s*(.*?)(?:\s*;?\s*&nbsp;\s*|\n)(.*)"
#footnote_text_pattern = r"\[\^(\d+)\]:\s*(.*?)(?:(?:\s*;|\n)\s*&nbsp;\s*)?(.*?)(?:\n|\Z)"
footnote_text_pattern = r"\[\^(\d+)\]:\s*(.*?);[\n\s]*&nbsp;\s*(.*?)\n"
#footnote_text_matches = re.findall(footnote_text_pattern, test_string, re.DOTALL)
footnotes = re.findall(r'\[\^(\d+)\]:&nbsp;(.*?)(?=\n\[|$)', markdown_text, re.DOTALL)
fn_dictionary = {}
for footnote in footnotes:
    number = footnote[0]
    number_string = f'[^{number}]'
    text = footnote[1].strip()
    fn_dictionary[number_string] = text

print(fn_dictionary)

# Create a new dictionary with the HTML code added to each value
new_fn_dictionary = {}
for key, value in fn_dictionary.items():
    new_value = f'<label for="sn-{key}" class="margin-toggle sidenote-number"></label>\n<input type="checkbox" id="sn-{key}" class="margin-toggle">\n<span class="sidenote">{value}</span>'
    new_fn_dictionary[key] = new_value

#print(new_fn_dictionary)

html_template = '<label for="sn-{num}" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-{num}" class="margin-toggle"/><span class="sidenote" id="{num}">{text}</span>'

'''
for key, value in fn_dictionary.items():
    html = html_template.format(num=key[2:-1], text=value)
    markdown_text = re.sub(re.escape(key), html, markdown_text)
'''

with open('test_0.html', 'w') as outfile:
    outfile.write(markdown_text)

for fn_key in fn_dictionary:
    fn_regex = re.compile(re.escape(fn_key))
    markdown_text = fn_regex.sub(fn_dictionary[fn_key].format(text=fn_dictionary[fn_key]), markdown_text)
'''
# Replace footnote markers in markdown with sidenote HTML
#footnote_pattern = r"\[\^(\d+)\]"
footnote_number_pattern = r"\[\^(\d+)\](?=[^\]]*$)"
for match in re.finditer(footnote_number_pattern, markdown_text):
    fn_number = match.group(0)
    try:
        fn_text = new_fn_dictionary[fn_number]
    except KeyError:
        print(f"Footnote {fn_number} not found in dictionary. Skipping...")
        continue
    html = html_template.format(num=fn_number, text=fn_text)
    markdown_text = markdown_text.replace(fn_number, html)

# Print the result
with open('test_1.md', 'w') as outfile:
    outfile.write(markdown_text)

# perform regex to find footnote references and replace them with HTML template
footnote_number_pattern = r"\[\^(\d+)\]"
for match in re.findall(footnote_number_pattern, markdown_text):
    footnote_number = match
    footnote_text = fn_dictionary.get(footnote_number, "")
    html_template = '<label for="sn-{0}" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-{0}" class="margin-toggle"/><span class="sidenote" id="{0}">{1}</span>'.format(footnote_number, footnote_text)
    markdown_text = markdown_text.replace("[^{}]".format(footnote_number), html_template)

with open("test_2.md", "w") as f:
    f.write(markdown_text)

footnote_marker_pattern = r"\[\^(\d+)\]"

html_template = (
    '<label for="sn-{num}" class="margin-toggle sidenote-number"></label>'
    '<input type="checkbox" id="sn-{num}" class="margin-toggle"/>'
    '<span class="sidenote" id="{num}">{text}</span>'
)

def replace_fn(match_obj):
    footnote_number = match_obj.group(1)
    if footnote_number in new_fn_dictionary:
        footnote_text = new_fn_dictionary[footnote_number]
    else:
        footnote_text = ""
    return html_template.format(num=footnote_number, text=footnote_text)

markdown_text = re.sub(footnote_marker_pattern, replace_fn, markdown_text)

# Print the HTML text
with open('test_3.md', 'w') as outfile:
    outfile.write(markdown_text)
'''
