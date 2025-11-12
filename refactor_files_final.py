#!/usr/bin/env python3
"""
Final cleanup - remove ALL duplicate scripts and old configs from l3-7 through l3-43.
"""

import os
import re
from pathlib import Path

kap3_dir = Path(r"C:\Users\ET20907\My Tresors\Gym_Muttenz\03 Mathematik\FMP\FMP-Skript\loesungen\Kap3")

def final_cleanup(filepath):
    """Remove duplicate scripts completely."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove ALL old inline MathJax config scripts
    content = re.sub(
        r'\s*<script>\s*window\.MathJax\s*=\s*\{[^}]*\};\s*</script>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove ALL old MathJax CDN includes (will be replaced with ordered set)
    content = re.sub(
        r'\s*<script[^>]*src="[^"]*mathjax[^"]*"[^>]*></script>\s*',
        '',
        content,
        flags=re.IGNORECASE
    )
    
    # Remove ALL old polyfill includes
    content = re.sub(
        r'\s*<script[^>]*src="https://polyfill\.io[^"]*"[^>]*></script>\s*',
        '',
        content,
        flags=re.IGNORECASE
    )
    
    # Remove ALL old script-math.js includes
    content = re.sub(
        r'\s*<script[^>]*src="\.\./script-math\.js"[^>]*></script>\s*',
        '',
        content
    )
    
    # Remove ALL old script-sol.js includes
    content = re.sub(
        r'\s*<script[^>]*src="\.\./script-sol\.js"[^>]*></script>\s*',
        '',
        content
    )
    
    # Remove inline toggleSolution function definitions (old style)
    content = re.sub(
        r'\s*<script>\s*function\s+(?:toggleInline|toggleSolution)\s*\([^)]*\)\s*\{[^}]*\}\s*</script>\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Now add the correct script chain once, right after the CSS link
    # Find the CSS link and insert scripts after it
    css_pattern = r'(\s*<link\s+rel="stylesheet"\s+href="\.\./style\.css"\s*>\s*)'
    
    replacement = r'''\1
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script src="../script-math.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="../script-sol.js"></script>
'''
    
    content = re.sub(css_pattern, replacement, content)
    
    return content

# Process files
for i in range(7, 44):
    filename = f"l3-{i}.html"
    filepath = kap3_dir / filename
    
    if filepath.exists():
        print(f"Cleaning {filename}...")
        cleaned = final_cleanup(filepath)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        
        print(f"  ✓ Final cleanup done")
    else:
        print(f"  ✗ {filename} not found")

print("Final cleanup complete!")
