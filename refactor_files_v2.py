#!/usr/bin/env python3
"""
Refactor l3-7.html through l3-43.html to match l-vorlage.html structure (REFINED).
Changes:
1. Remove old inline MathJax config and old MathJax script
2. Add script-math.js before new MathJax in correct order
3. Remove duplicate or old inline toggleSolution functions
"""

import os
import re
from pathlib import Path

kap3_dir = Path(r"C:\Users\ET20907\My Tresors\Gym_Muttenz\03 Mathematik\FMP\FMP-Skript\loesungen\Kap3")

def refactor_file_v2(filepath):
    """Refactor a single HTML file to match the template - REFINED VERSION."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    skip_until_end_script = False
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip old inline MathJax config script block
        if '<script>' in line and i + 1 < len(lines):
            next_line = lines[i + 1]
            if 'window.MathJax' in next_line or 'MathJax' in next_line:
                # Skip this script block and all lines until </script>
                while i < len(lines) and '</script>' not in lines[i]:
                    i += 1
                i += 1  # skip the closing tag
                continue
        
        # Skip old MathJax CDN script (the first one if duplicated)
        if 'mathjax@3/es5/tex-mml-chtml.js' in line:
            # Check if we've already added the correct scripts after CSS
            # If this is appearing before the CSS, skip it
            if not any('script-math.js' in l for l in new_lines[-10:]):
                i += 1
                continue
        
        # Skip old inline toggleSolution function script
        if '<script>' in line and 'toggleSolution' in ''.join(lines[i:min(i+20, len(lines))]):
            while i < len(lines) and '</script>' not in lines[i]:
                i += 1
            i += 1
            continue
        
        # When we find the CSS link, inject the new script tags right after it
        if '<link rel="stylesheet" href="../style.css">' in line and 'script-math.js' not in ''.join(new_lines[-5:]):
            new_lines.append(line)
            new_lines.append('    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>\n')
            new_lines.append('    <script src="../script-math.js"></script>\n')
            new_lines.append('    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\n')
            new_lines.append('    <script src="../script-sol.js"></script>\n')
            i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    return ''.join(new_lines)

# Process files l3-7 through l3-43
for i in range(7, 44):
    filename = f"l3-{i}.html"
    filepath = kap3_dir / filename
    
    if filepath.exists():
        print(f"Processing {filename}...")
        refactored = refactor_file_v2(filepath)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(refactored)
        
        print(f"  ✓ Cleaned {filename}")
    else:
        print(f"  ✗ {filename} not found")

print("Done!")
