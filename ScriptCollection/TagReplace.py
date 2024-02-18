import os

def replace_tag_in_files(folder_path, old_tag, new_tag):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        if file.endswith('.txt'):
            with open(file_path, 'r') as f:
                lines = f.readlines()

            with open(file_path, 'w') as f:
                for line in lines:
                    updated_line = line.replace(old_tag, new_tag)
                    f.write(updated_line)

    print("Tag-Austausch abgeschlossen.")

folder_path = "L:\\Datasets\\lora\\xyz" # Set path to Dataset
old_tag = "Airi"                        # Set the old Tag to Replace
new_tag = "Fuyu"                        # Set the new Tag to Insert
replace_tag_in_files(folder_path, old_tag, new_tag)
