import os
from flask import render_template, abort, current_app, redirect, url_for
from . import movies
from markdown import markdown

@movies.route('/')
def movies_index():
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'movies')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    # Default to first movie
    if files:
        first_slug = files[0][:-3]
        return redirect(url_for('movies.movie_detail', movie_slug=first_slug))
    return render_template('movies/index.html', files=files, title='Movies', carousel=False)

@movies.route('/<movie_slug>')
def movie_detail(movie_slug):
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'movies')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    md_path = os.path.join(content_dir, f'{movie_slug}.md')
    try:
        with open(md_path, encoding='utf-8') as f:
            content = markdown(f.read())
    except FileNotFoundError:
        abort(404)
    return render_template(
        'movies/detail.html',
        content=content,
        title=movie_slug.replace('-', ' ').title(),
        files=files,
        active_slug=movie_slug,
        carousel=False
    )
