import os
import re

# Set this to the root of your Obsidian vault or docs folder
BASE_DIR = "../docs"

# Regex to match Obsidian-style embeds like ![[image.png|300x200]]
obsidian_img_pattern = re.compile(r'!\[\[([^\|\]]+)\|(\d+)[xX](\d+)\]\]')

# Regex to match markdown images with size in alt text, e.g. ![alt|300x200](image.png)
markdown_img_pattern = re.compile(r'!\[(.*?)\|(\d+)[xX](\d+)\]\((.*?)\)')

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace Obsidian-style images with markdown + attr_list
            def replace_obsidian_img(match):
                filename = match.group(1).strip()
                width = match.group(2)
                height = match.group(3)
                return f"![]({filename}){{ width={width} height={height} }}"

            content = obsidian_img_pattern.sub(replace_obsidian_img, content)

            # Replace markdown images with size in alt text to attr_list syntax
            def replace_markdown_img(match):
                alt_text = match.group(1).strip()
                width = match.group(2)
                height = match.group(3)
                filename = match.group(4).strip()
                return f"![{alt_text}]({filename}){{ width={width} height={height} }}"

            content = markdown_img_pattern.sub(replace_markdown_img, content)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

print("All markdown files updated in-place.")
