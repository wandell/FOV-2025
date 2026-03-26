import os
import re

qmd_files = []
for root, dirs, files in os.walk('.'):
    if '_book' in root or '.git' in root or 'site_libs' in root:
        continue
    for f in files:
        if f.endswith('.qmd'):
            qmd_files.append(os.path.join(root, f))

# Pattern to find citations in qmd files: @ followed by an Uppercase letter, lowercase letters, and numbers
# like @Author2020-something or @Author2020
citation_pattern_qmd = re.compile(r'@([A-Z])([a-zA-Z]*[0-9]{4}[A-Za-z0-9\-]*)')

# Pattern to find citation keys in .bib files: @Article{Author2020...
citation_pattern_bib = re.compile(r'^@([A-Za-z]+)\{([A-Z])([a-zA-Z]*[0-9]{4}[A-Za-z0-9\-]*)', re.MULTILINE)

# Process qmd files
for qmd_file in qmd_files:
    try:
        with open(qmd_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We replace the first letter with its lowercase version
        new_content = citation_pattern_qmd.sub(lambda m: '@' + m.group(1).lower() + m.group(2), content)
        
        if new_content != content:
            with open(qmd_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated citations in {qmd_file}")
    except Exception as e:
        print(f"Error processing {qmd_file}: {e}")

# Process bib file
bib_file = 'paperpile.bib'
if os.path.exists(bib_file):
    try:
        with open(bib_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = citation_pattern_bib.sub(lambda m: '@' + m.group(1) + '{' + m.group(2).lower() + m.group(3), content)
        
        if new_content != content:
            with open(bib_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated citations in {bib_file}")
    except Exception as e:
        print(f"Error processing {bib_file}: {e}")
