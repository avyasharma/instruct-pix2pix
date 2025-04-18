import os
import json

# Set this to the directory containing all the folders
parent_directory = '/ocean/projects/cis250054p/shared/instruct-pix2pix/data/clip-filtered-small'

edit_prompts = []

folder_names = sorted(os.listdir(parent_directory))

# Iterate through every item in that directory
for folder_name in folder_names:
    folder_path = os.path.join(parent_directory, folder_name)

    # print(folder_path)

    # Check that it's a directory
    if os.path.isdir(folder_path):
        # Construct the path to the specific file you want (e.g. data.json)
        json_path = os.path.join(folder_path, 'prompt.json')

        # If the file exists, open and parse its JSON
        if os.path.isfile(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                if 'edit' in data:
                    edit_prompts.append(data['edit'])

with open('edit_prompts.txt', 'w', encoding='utf-8') as f:
    for prompt in edit_prompts:
        f.write(prompt + '\n')

print(f'Collected {len(edit_prompts)} edit_prompt values.')
