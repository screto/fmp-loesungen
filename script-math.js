// MathJax configuration — must be set on window before loading the MathJax script
window.MathJax = {
    tex: {
        // allow $...$ and \(...\) for inline math
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        // allow $$...$$ and \[...\] for display math
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
    },
    svg: { fontCache: 'global' }
};

