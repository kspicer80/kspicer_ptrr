import os
import PyPDF2
import docx

input_dir = r"C:/Users/KSpicer/Desktop/final_projects"
output_file = r"C:/Users/KSpicer/Desktop/final_projects/txt_files.txt"

with open(output_file, 'w') as out_file:
    for dirpath, dirnames, filenames in os.walk(input_dir):
        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as in_file:
                        file_content = in_file.read()
                        if len(file_content) == 0:
                            continue
                        first_1000_chars = file_content[:1000]
                        out_file.write(f'--- {os.path.relpath(file_path, input_dir)} ---\n')
                        out_file.write(first_1000_chars)
                        out_file.write('\n\n')
                except UnicodeDecodeError:
                    print(f'Skipping file {file_path} due to UnicodeDecodeError')
            elif filename.endswith('.pdf'):
                file_path = os.path.join(dirpath, filename)
                # Handle PDF files as before...
            elif filename.endswith('.docx'):
                file_path = os.path.join(dirpath, filename)
                try:
                    doc = docx.Document(file_path)
                    file_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
                    if len(file_content) == 0:
                        continue
                    first_1000_chars = file_content[:1000]
                    out_file.write(f'--- {os.path.relpath(file_path, input_dir)} ---\n')
                    out_file.write(first_1000_chars)
                    out_file.write('\n\n')
                except Exception as e:
                    print(f'Skipping file {file_path} due to error: {e}')
