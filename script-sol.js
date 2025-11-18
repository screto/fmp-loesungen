function toggleSolution(target) {
    // target can be a button element (this) or an id string for the solution element
    if (typeof target === 'string') {
        const el = document.getElementById(target);
        if (!el) return;
        const wasHidden = el.classList.contains('is-hidden');
        el.classList.toggle('is-hidden');

        // Try to find any clickable elements (buttons/inputs) that reference this id
        // in their onclick attribute and update their displayed text accordingly.
        const clickable = Array.from(document.querySelectorAll('[onclick]')).filter(b => {
            const attr = b.getAttribute('onclick') || '';
            // match both 'id' and "id" and plain occurrences
            return attr.indexOf('\"' + target + '\"') !== -1 || attr.indexOf("'" + target + "'") !== -1 || attr.indexOf(target) !== -1;
        });

        const newText = wasHidden ? 'Lösung verbergen' : 'Lösung anzeigen';
        clickable.forEach(btn => {
            if (btn.tagName === 'INPUT' && 'value' in btn) {
                btn.value = newText;
            } else {
                btn.textContent = newText;
            }
        });

        return;
    }

    // assume DOM element (button)
    const btn = target;
    const solution = btn.nextElementSibling;
    if (!solution) return;
    const wasHidden = solution.classList.contains('is-hidden');
    solution.classList.toggle('is-hidden');
    // set button text according to new state
    const newText = wasHidden ? 'Lösung verbergen' : 'Lösung anzeigen';
    if (btn.tagName === 'INPUT' && 'value' in btn) {
        btn.value = newText;
    } else {
        btn.textContent = newText;
    }
}

// Provide a toggleInline alias for pages that call toggleInline(this)
function toggleInline(btn) { return toggleSolution(btn); }

// backward-compatible alias (old misspelling)
function toogleSolution(arg) { return toggleSolution(arg); }