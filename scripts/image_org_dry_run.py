import os
import re
import glob

CHAPTERS_DIR = "chapters"
IMAGES_DIR = os.path.join(CHAPTERS_DIR, "images")

def get_chapter_number(filename):
    """
    Extracts the chapter number from filenames like 'chapter-02-image-formation.qmd'.
    Returns 'NN' string or None if not found.
    """
    match = re.search(r'chapter-(\d+)', filename)
    if match:
        return match.group(1)
    # Handle 'part-1-...' or 'appendix-...' if needed,
    # but the user specifically asked for "chapter-02* -> images/02"
    return None

def main():
    print(f"Scanning images in: {IMAGES_DIR}")
    
    # 1. List all existing images
    all_images = set()
    if os.path.exists(IMAGES_DIR):
        for f in os.listdir(IMAGES_DIR):
            if os.path.isfile(os.path.join(IMAGES_DIR, f)) and not f.startswith('.'):
                all_images.add(f)
    print(f"Found {len(all_images)} total images in {IMAGES_DIR}.\n")

    # 2. Scan QMD files for image references
    qmd_files = glob.glob(os.path.join(CHAPTERS_DIR, "*.qmd"))
    image_usage = {}  # { 'image_filename': set(['chapter-01.qmd', 'chapter-02.qmd']) }
    
    # Regex to capture markdown image links: ![alt](path)
    # We mainly care about paths starting with "images/" or "./images/"
    img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    
    for qmd_path in qmd_files:
        filename = os.path.basename(qmd_path)
        with open(qmd_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        matches = img_pattern.findall(content)
        for match in matches:
            # Clean up path: standard markdown link might have title tooltips etc "path 'title'"
            path = match.split()[0] 
            
            # We assume images are in chapters/images, so links should look like "images/foo.png"
            if 'images/' in path:
                # Extract the actual filename from the path
                # e.g. "images/eyeball.png" -> "eyeball.png"
                parts = path.split('/')
                try:
                    idx = parts.index('images')
                    if idx + 1 < len(parts):
                        img_name = parts[idx+1]
                        
                        # Remove any fragments or queries (rare in local files but good practice)
                        img_name = img_name.split('#')[0].split('?')[0]
                        
                        if img_name not in image_usage:
                            image_usage[img_name] = set()
                        image_usage[img_name].add(filename)
                except ValueError:
                    continue

    # 3. Analyze and Report
    moves = {}    # { '02': ['img1.png', 'img2.png'] }
    shared = []   # ['shared1.png', ...]
    unused = []   # ['unused1.png', ...]
    missing = []  # ['missing_ref.png'] -> referenced in QMD but not found in folder

    # Check referenced images
    for img, chapters in image_usage.items():
        if img not in all_images:
            missing.append(f"{img} (used in {', '.join(chapters)})")
            continue
            
        if len(chapters) == 1:
            # exclusive to one chapter
            chapter_file = list(chapters)[0]
            num = get_chapter_number(chapter_file)
            if num:
                if num not in moves:
                    moves[num] = []
                moves[num].append(img)
            else:
                # Referenced in a non-chapter file (e.g. part-1.qmd), keep in shared/root or specific folder?
                # User asked for "chapter-02...", so maybe 'part-1' images stay in root or go to 'misc'
                shared.append(f"{img} (used in {chapter_file})")
        else:
            # Shared across multiple files
            shared.append(f"{img} (used in {len(chapters)} files: {', '.join(chapters)})")

    # Check unreferenced images
    for img in all_images:
        if img not in image_usage:
            unused.append(img)

    # 4. Print Report
    print("=== DRY RUN REPORT: IMAGE REORGANIZATION ===\n")
    
    # Sort keys nicely
    sorted_chapters = sorted(moves.keys())
    
    total_moves = 0
    for num in sorted_chapters:
        file_list = moves[num]
        total_moves += len(file_list)
        print(f"## Chapter {num} (Target: chapters/images/{num}/)")
        print(f"   Moving {len(file_list)} images.")
        # Print first few as example
        example = ', '.join(file_list[:3])
        if len(file_list) > 3:
            example += ", ..."
        print(f"   Examples: {example}\n")

    print(f"## Shared Images (Target: chapters/images/ or chapters/images/shared/)")
    print(f"   {len(shared)} images are used in multiple chapters or non-numbered files.")
    for s in shared[:5]:
        print(f"   - {s}")
    if len(shared) > 5:
        print(f"   ... and {len(shared)-5} more.\n")

    print(f"## Unused Images (Action: Delete or Archive?)")
    print(f"   {len(unused)} files found in chapters/images/ but NOT referenced in any QMD.")
    
    print(f"\n## Missing Images (Warning!)")
    print(f"   {len(missing)} images reference in text but NOT found in folder.")
    for m in missing[:5]:
        print(f"   - {m}")

    print("\n" + "="*40)
    print(f"SUMMARY:")
    print(f"Total images found: {len(all_images)}")
    print(f"Distinct images referenced: {len(image_usage)}")
    print(f"Planned moves: {total_moves}")
    print(f"Shared/Skipped: {len(shared)}")
    print(f"Unused: {len(unused)}")
    print("="*40)

if __name__ == "__main__":
    main()
