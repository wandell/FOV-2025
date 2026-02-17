import os
import shutil
import re

CHAPTERS_DIR = "chapters"
IMAGES_DIR = os.path.join(CHAPTERS_DIR, "images")
TARGET_CHAPTER_NUM = "02"
CHAPTER_FILENAME = f"chapter-{TARGET_CHAPTER_NUM}-image-formation-v2.qmd"
CHAPTER_PATH = os.path.join(CHAPTERS_DIR, CHAPTER_FILENAME)
TARGET_IMG_DIR = os.path.join(IMAGES_DIR, TARGET_CHAPTER_NUM)

def main():
    print(f"Processing Chapter {TARGET_CHAPTER_NUM}...")
    
    # 1. Read the chapter content
    if not os.path.exists(CHAPTER_PATH):
        print(f"Error: Chapter file not found: {CHAPTER_PATH}")
        return

    with open(CHAPTER_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. Find all images used in this chapter
    # Regex for ![alt](path)
    img_pattern = re.compile(r'!\[.*?\]\((images/(.*?))\)')
    
    matches = img_pattern.findall(content)
    # matches is list of (full_path, filename) tuples
    # e.g., [('images/eyeball.png', 'eyeball.png'), ...]
    
    moved_count = 0
    new_content = content

    for full_path, filename in matches:
        # Ignore if already processed or complex path
        if '/' in filename: 
            # e.g. images/subdir/foo.png - skip for now or handle?
            # Our regex captures 'images/(.*?)', so filename is the suffix.
            pass

        # Clean filename (remove query params/anchors)
        clean_filename = filename.split()[0].split('#')[0].split('?')[0]
        
        src_path = os.path.join(IMAGES_DIR, clean_filename)
        dst_path = os.path.join(TARGET_IMG_DIR, clean_filename)
        
        # Check if file exists
        if os.path.exists(src_path):
            # Move file
            print(f"Moving: {clean_filename} -> {TARGET_CHAPTER_NUM}/{clean_filename}")
            try:
                shutil.move(src_path, dst_path)
                moved_count += 1
            except Exception as e:
                print(f"  Error moving {clean_filename}: {e}")
                continue
        elif os.path.exists(dst_path):
            print(f"Skipping move (already exists): {clean_filename}")
        else:
            print(f"Warning: Image file not found: {src_path}")
            # We still update the link if the file is missing? 
            # Ideally yes, assuming the user will fix the file location later.
            # But let's only update link if we successfully moved OR it's already there.

        # Update content: replace 'images/filename' with 'images/02/filename'
        # Be careful to replace only the specific instance or globally?
        # Since this image is exclusive (verified by dry run), global replace is safe-ish,
        # but regex sub is safer.
        
        # Construct the new relative path for the QMD file
        new_rel_path = f"images/{TARGET_CHAPTER_NUM}/{filename}"
        
        # Replace explicitly in the text
        # We search for the exact string captured in the group: "images/eyeball.png"
        pass

    # 3. Rewrite content with new paths
    # We do a second pass with regex sub to ensure we catch all instances correctly
    def replace_link(match):
        full_match = match.group(0) # ![...](images/foo.png)
        rel_path = match.group(1)   # images/foo.png
        filename = match.group(2)   # foo.png
        
        return full_match.replace(rel_path, f"images/{TARGET_CHAPTER_NUM}/{filename}")

    new_content = img_pattern.sub(replace_link, content)
    
    # 4. Save updated chapter
    with open(CHAPTER_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"\nSuccess! Moved {moved_count} images.")
    print(f"Updated references in {CHAPTER_FILENAME}.")

if __name__ == "__main__":
    main()
