import click
from poc_cli_translations.core.message import translate

@click.command()
@click.argument("name")
@click.pass_context
def hello(ctx, name: str):
    """Command to say hello"""
    translate("hello")
    translate("hi", f"{name}")  
