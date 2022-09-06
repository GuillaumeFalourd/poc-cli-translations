import click

from poc_cli_translations.commands.config.lang import lang

@click.group()
def config():
    """Command to config something."""
    pass

config.add_command(lang)