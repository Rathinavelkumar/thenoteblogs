import os
from flask import render_template, abort, current_app, redirect, url_for
from . import stories
from app.utils_markdown import render_aligned_markdown

"""
Story routes for TheNoteBlogs
"""

@stories.route('/')
def stories_index():
    """
    Redirects to the first story detail page or renders the story index.
    """
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'stories')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    # Default to first story
    if files:
        first_slug = files[0][:-3]
        return redirect(url_for('stories.story_detail', story_slug=first_slug))
    return render_template('shared_index.html', files=files, title='Stories', section='stories', carousel=False)

@stories.route('/<story_slug>')
def story_detail(story_slug):
    """
    Renders the detail page for a specific story.
    """
    content_dir = os.path.join(current_app.root_path, '..', 'content', 'stories')
    files = [f for f in os.listdir(content_dir) if f.endswith('.md')]
    files = sorted(files)
    md_path = os.path.join(content_dir, f'{story_slug}.md')
    try:
        with open(md_path, encoding='utf-8') as f:
            content = render_aligned_markdown(f.read())
    except FileNotFoundError:
        abort(404)
    return render_template(
        'shared_detail.html',
        content=content,
        title=story_slug.replace('-', ' ').title(),
        files=files,
        active_slug=story_slug,
        section='stories',
        section_title='Stories',
        carousel=False
    )
