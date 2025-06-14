import os

def list_files_to_file(startpath, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(startpath):
            # Exclude `.git` and `node_modules`
            dirs[:] = [d for d in dirs if d not in [".git", "node_modules"]]

            level = root.replace(startpath, "").count(os.sep)
            indent = " " * 4 * level
            f.write(f"{indent}[{os.path.basename(root)}]\n")

            subindent = " " * 4 * (level + 1)
            for file in files:
                f.write(f"{subindent}- {file}\n")

folder_path = "Path on what folder you want made into a tree"
output_file = "Path on where you want that file to go"
list_files_to_file(folder_path, output_file)
print(f"File tree saved to {output_file}")
