import os
import click
from App import App


@App.cli.group()
def translate():
    """Translation and localization commands."""

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extra command failed')
    if os.system(
            'pybabel init -i messages.pot -d App/translations -l' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')

@translate.command()
def update():
    """Update all languages"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d App/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile all languages"""
    if os.system('pybabel compile -d App/translation'):
        raise RuntimeError('compile command failed')
