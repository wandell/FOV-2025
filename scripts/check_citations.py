import re
import glob
import os

def get_citation_keys_from_qmd(qmd_files):
    # Matches @key where preceding char is not alphanumeric or dot.
    # We allow dots in the key, but strip trailing punctuation later.
    citation_pattern = re.compile(r'(?<![\w\.])@([a-zA-Z0-9_\-:\.]+)')
    
    ignored_prefixes = ('sec-', 'fig-', 'eq-', 'tbl-', 'ch-') 
    
    citations = set()
    
    for file_path in qmd_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Find all matches
                for match in citation_pattern.finditer(content):
                    key = match.group(1)
                    # Strip trailing punctuation often captured (.,;:)
                    key = key.rstrip('.,;:')
                    
                    # Filter out cross-references
                    if not any(key.startswith(p) for p in ignored_prefixes):
                        citations.add(key)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    return citations

def get_bib_keys(bib_file):
    bib_keys = set()
    # Regex to find @type{key,
    bib_pattern = re.compile(r'@\w+\s*\{\s*([^,]+),')
    
    try:
        with open(bib_file, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = bib_pattern.findall(content)
            for match in matches:
                bib_keys.add(match.strip())
    except Exception as e:
        print(f"Error reading {bib_file}: {e}")
        
    return bib_keys

def main():
    chapters_dir = 'chapters'
    bib_file = 'paperpile.bib'
    
    # Get all .qmd files in chapters/ and root
    qmd_files = glob.glob(os.path.join(chapters_dir, '*.qmd')) + glob.glob('*.qmd')
    
    print(f"Scanning {len(qmd_files)} .qmd files in workspace...")
    found_citations = get_citation_keys_from_qmd(qmd_files)
    print(f"Found {len(found_citations)} unique citation keys (excluding cross-refs).")
    
    print(f"Scanning '{bib_file}'...")
    bib_keys = get_bib_keys(bib_file)
    print(f"Found {len(bib_keys)} keys in bib file.")
    
    missing_keys = []
    case_mismatches = []
    
    # Create a lowercase map for case-insensitive check
    bib_keys_lower = {k.lower(): k for k in bib_keys}
    
    for cite in found_citations:
        if cite not in bib_keys:
            # Check for case mismatch
            if cite.lower() in bib_keys_lower:
                correct_key = bib_keys_lower[cite.lower()]
                case_mismatches.append((cite, correct_key))
            else:
                missing_keys.append(cite)
    
    missing_keys.sort()
    case_mismatches.sort()
    
    print("\n" + "="*40)
    print("MISSING KEYS (Not found in bib file):")
    print("="*40)
    if missing_keys:
        for key in missing_keys:
            print(f"- {key}")
    else:
        print("None.")
        
    print("\n" + "="*40)
    print("CASE MISMATCHES (Found in qmd, but casing differs in bib):")
    print("="*40)
    if case_mismatches:
        for bad, good in case_mismatches:
            print(f"- Used: {bad}  ->  Defined in Bib: {good}")
    else:
        print("None.")

if __name__ == "__main__":
    main()
