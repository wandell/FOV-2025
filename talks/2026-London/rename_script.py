import os
import re

base_dir = "/Users/wandell/Documents/FOV-2025-Quarto/talks/2026-London"
qmd_path = os.path.join(base_dir, "index.qmd")

with open(qmd_path, "r") as f:
    text = f.read()

def replacer(match):
    caption = match.group(1)
    old_rel_path = match.group(2)
    tag = match.group(3)
    attrs = match.group(4)
    
    # Strip fig- prefix for the filename
    fname_base = tag
    if fname_base.startswith("fig-"):
        fname_base = fname_base[4:]
        
    ext = os.path.splitext(old_rel_path)[1]
    new_rel_path = f"images/{fname_base}{ext}"
    
    # Move file if it exists
    old_full_path = os.path.join(base_dir, old_rel_path)
    new_full_path = os.path.join(base_dir, new_rel_path)
    
    if os.path.exists(old_full_path) and old_full_path != new_full_path:
        # Create directory if it somehow doesn't exist
        os.makedirs(os.path.dirname(new_full_path), exist_ok=True)
        os.rename(old_full_path, new_full_path)
        print(f"Renamed: {old_full_path} -> {new_full_path}")
    elif os.path.exists(new_full_path) and old_full_path != new_full_path:
        print(f"Already exists: {new_full_path}")
        
    return f"![{caption}]({new_rel_path}){{#{tag}{attrs}}}"

new_text = re.sub(r"!\[(.*?)\]\((images/[^)]+)\)\{\#([^} ]+)(.*?)\}", replacer, text)

with open(qmd_path, "w") as f:
    f.write(new_text)

print("Done")
