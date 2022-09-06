import click

from poc_cli_translations.commands.say.hello import hello

@click.group()
def say():
    """Command to say a text."""
    pass

say.add_command(hello)