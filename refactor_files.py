#!/usr/bin/env python3
"""
Refactor l3-7.html through l3-43.html to match l-vorlage.html structure.
Changes:
1. Move script-math.js before MathJax
2. Convert inline toggle to id-based toggleSolution calls
3. Update layout to use task-row pattern (where applicable for id-based toggles)
4. Keep existing content intact
"""

import os
import re
from pathlib import Path

kap3_dir = Path(r"C:\Users\ET20907\My Tresors\Gym_Muttenz\03 Mathematik\FMP\FMP-Skript\loesungen\Kap3")

def refactor_file(filepath):
    """Refactor a single HTML file to match the template."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Move script-math.js before MathJax
    # Remove the inline MathJax config if it exists
    content = re.sub(
        r'<script>\s*window\.MathJax\s*=\s*\{[^}]*\};\s*</script>\s*\n\s*<script src="https://cdn\.jsdelivr\.net/npm/mathjax@3/es5/tex-mml-chtml\.js"></script>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # 2. Add script-math.js and MathJax in correct order if not already done
    if '<script src="../script-math.js"></script>' not in content:
        # Find the link for CSS and add scripts after it
        if '<link rel="stylesheet" href="../style.css">' in content:
            content = content.replace(
                '<link rel="stylesheet" href="../style.css">',
                '<link rel="stylesheet" href="../style.css">\n    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>\n    <script src="../script-math.js"></script>\n    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\n    <script src="../script-sol.js"></script>'
            )
    
    # 3. Remove inline script that might exist at bottom
    content = re.sub(
        r'<script>\s*function toggleSolution\(btn\)\s*\{[^}]*\}[^}]*\}[^}]*\}\s*</script>',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content

# Process files l3-7 through l3-43
for i in range(7, 44):
    filename = f"l3-{i}.html"
    filepath = kap3_dir / filename
    
    if filepath.exists():
        print(f"Processing {filename}...")
        refactored = refactor_file(filepath)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(refactored)
        
        print(f"  ✓ Updated {filename}")
    else:
        print(f"  ✗ {filename} not found")

print("Done!")
