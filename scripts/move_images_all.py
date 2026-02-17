import os
import shutil
import re
import glob

CHAPTERS_DIR = "chapters"
IMAGES_DIR = os.path.join(CHAPTERS_DIR, "images")

# Regex to capture markdown image links: ![alt](images/filename)
# matches "images/filename" in group 1, "filename" in group 2
IMG_LINK_PATTERN = re.compile(r'!\[.*?\]\((images/([^/]*?))\)')

def get_chapter_number(filename):
    """
    Extracts the chapter number from filenames like 'chapter-02-image-formation.qmd'.
    Returns '03', '10' etc. or None.
    """
    match = re.search(r'chapter-(\d+)', filename)
    if match:
        return match.group(1)
    return None

def main():
    print(f"Scanning usage in: {CHAPTERS_DIR}")

    # 1. Map images to chapters
    qmd_files = glob.glob(os.path.join(CHAPTERS_DIR, "*.qmd"))
    image_usage = {}  # { 'filename': set(['chapter-03.qmd']) }

    for qmd_path in qmd_files:
        filename = os.path.basename(qmd_path)
        with open(qmd_path, 'r', encoding='utf-8') as f:
            content = f.read()

        matches = IMG_LINK_PATTERN.findall(content)
        for _, img_name in matches:
            # Clean filename
            img_name = img_name.split()[0].split('#')[0].split('?')[0]
            if img_name not in image_usage:
                image_usage[img_name] = set()
            image_usage[img_name].add(filename)

    # 2. Identify moves
    moves = {} # { '03': ['img1.png'], '04': [...] }

    for img, chapters in image_usage.items():
        # Only move if used in exactly one file
        if len(chapters) == 1:
            chapter_file = list(chapters)[0]
            num = get_chapter_number(chapter_file)
            
            # Skip if no chapter number (e.g. part-1.qmd)
            # Skip if Chapter 02 (already done, though images likely not found in root anyway)
            if num and num != '02': 
                if num not in moves:
                    moves[num] = []
                moves[num].append((img, chapter_file))

    # 3. Execute Moves
    print(f"Found {len(moves)} chapters to organize.\n")

    for num, items in sorted(moves.items()):
        print(f"Processing Chapter {num} ({len(items)} images)...")
        
        target_dir = os.path.join(IMAGES_DIR, num)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # We need to update the QMD file content
        # Since all images in 'items' belong to the same chapter_file, get it from the first item
        if not items: continue
        chapter_filename = items[0][1]
        chapter_path = os.path.join(CHAPTERS_DIR, chapter_filename)
        
        with open(chapter_path, 'r', encoding='utf-8') as f:
            content = f.read()

        moved_count = 0
        
        for img_name, _ in items:
            src = os.path.join(IMAGES_DIR, img_name)
            dst = os.path.join(target_dir, img_name)

            # Move File
            if os.path.exists(src):
                try:
                    shutil.move(src, dst)
                    moved_count += 1
                except Exception as e:
                    print(f"  Error moving {img_name}: {e}")
            elif os.path.exists(dst):
                # Already moved?
                pass
            else:
                print(f"  Warning: {img_name} not found at {src}")

        # Update Links in QMD
        # Logic: Replace "images/img_name" with "images/03/img_name"
        # We assume exclusive usage, so global replace of specific string is safe
        
        def replace_fn(match):
            full_str = match.group(0) # ![...](images/foo.png)
            path = match.group(1)     # images/foo.png
            fname = match.group(2)    # foo.png
            
            # Check if this filename is one we decided to move
            # (matches regex group 2)
            clean_fname = fname.split()[0].split('#')[0].split('?')[0]
            
            # Check if this specific image was in our move list for this chapter
            # (It should be, based on our logic, but good to be precise)
            if any(item[0] == clean_fname for item in items):
                return full_str.replace(path, f"images/{num}/{fname}")
            return full_str

        new_content = IMG_LINK_PATTERN.sub(replace_fn, content)

        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"  Moves complete. Updated {chapter_filename}.\n")

if __name__ == "__main__":
    main()
