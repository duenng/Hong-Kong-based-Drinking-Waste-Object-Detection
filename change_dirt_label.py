import os

def change_class_in_annotations(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        parts = line.strip().split(' ')
        if parts[0] == '0':
            parts[0] = '3'
        elif parts[0] == '1':
            parts[0] = '4'
        elif parts[0] == '2':
            parts[0] = '5'
        new_line = ' '.join(parts)
        new_lines.append(new_line)

    return new_lines

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.txt'):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}_dirty.txt")
            
            modified_lines = change_class_in_annotations(input_path)
            with open(output_path, 'w') as file:
                for line in modified_lines:
                    file.write(line + '\n')
            print(f"Processed {filename}")

process_directory('./valid/labels')