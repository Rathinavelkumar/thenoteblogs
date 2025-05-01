import markdown
import re

def render_aligned_markdown(md_text):
    """
    Convert Markdown to HTML and wrap H1 and H2 sections with alignment classes.
    H1: .center-align
    H2: .left-align
    """
    html = markdown.markdown(md_text, extensions=['extra'])

    # Function to wrap H1 and its following content until next H1/H2
    def wrap_h1_sections(html):
        pattern = r'(<h1>.*?</h1>(?:.|\n)*?)(?=<h[12]>|$)'
        def repl(m):
            return f'<div class="center-align">{m.group(1)}</div>'
        return re.sub(pattern, repl, html, flags=re.DOTALL)

    # Function to wrap H2 and its following content until next H1/H2
    def wrap_h2_sections(html):
        pattern = r'(<h2>.*?</h2>(?:.|\n)*?)(?=<h[12]>|$)'
        def repl(m):
            return f'<div class="left-align">{m.group(1)}</div>'
        return re.sub(pattern, repl, html, flags=re.DOTALL)

    html = wrap_h1_sections(html)
    html = wrap_h2_sections(html)
    return html
