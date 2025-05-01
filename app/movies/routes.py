import os
from flask import render_template, abort, current_app, redirect, url_for
from . import movies
from app.utils_markdown import render_aligned_markdown

"""
Movie routes for TheNoteBlogs
"""

@movies.route('/')
def movies_index():
    """Redirects to the first movie detail page or renders the movie index."""
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'movies')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    # Default to first movie
    if files:
        first_slug = files[0][:-3]
        return redirect(url_for('movies.movie_detail', movie_slug=first_slug))
    return render_template('shared_index.html', files=files, title='Movies', section='movies', carousel=False)

@movies.route('/<movie_slug>')
def movie_detail(movie_slug):
    """Renders the detail page for a specific movie."""
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'movies')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    md_path = os.path.join(content_dir, f'{movie_slug}.md')
    try:
        with open(md_path, encoding='utf-8') as f:
            content = render_aligned_markdown(f.read())
    except FileNotFoundError:
        abort(404)
    return render_template(
        'shared_detail.html',
        content=content,
        title=movie_slug.replace('-', ' ').title(),
        files=files,
        active_slug=movie_slug,
        section='movies',
        section_title='Movies',
        carousel=False
    )
