function toggleSolution(target) {
    // target can be a button element (this) or an id string for the solution element
    if (typeof target === 'string') {
        const el = document.getElementById(target);
        if (!el) return;
        el.classList.toggle('is-hidden');
        return;
    }

    // assume DOM element (button)
    const btn = target;
    const solution = btn.nextElementSibling;
    if (!solution) return;
    const wasHidden = solution.classList.contains('is-hidden');
    solution.classList.toggle('is-hidden');
    // set button text according to new state
    btn.textContent = wasHidden ? 'Lösung verbergen' : 'Lösung anzeigen';
}

// Provide a toggleInline alias for pages that call toggleInline(this)
function toggleInline(btn) { return toggleSolution(btn); }

// backward-compatible alias (old misspelling)
function toogleSolution(arg) { return toggleSolution(arg); }