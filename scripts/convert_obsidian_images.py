import os
import re

# Set this to the root of your Obsidian vault or docs folder
BASE_DIR = "../docs"

# Regex to match Obsidian-style embeds like ![[image.png|300x200]]
obsidian_img_pattern = re.compile(r'!\[\[([^\|\]]+)\|(\d+)[xX](\d+)\]\]')

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace with Markdown + attr_list
            def replace_img(match):
                filename = match.group(1).strip()
                width = match.group(2)
                height = match.group(3)
                return f"![]({filename}){{ width={width} height={height} }}"

            modified_content = obsidian_img_pattern.sub(replace_img, content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)

print("All markdown files updated in-place.")
