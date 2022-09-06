import click

from poc_cli_translations.commands.say import say
from poc_cli_translations.commands.config import config

CLI_COMMAND_NAME = "poc"
CLI_VERSION = "1.0.0"

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

class CliGroup(click.Group):
    def format_help(self, ctx, formatter):
        super().format_help(ctx, formatter)
    
@click.group(cls=CliGroup, context_settings=CONTEXT_SETTINGS)
@click.help_option("-h", "--help", help="Show command helper.")
@click.version_option(
    CLI_VERSION,
    "-v",
    "--version",
    message=f"{CLI_COMMAND_NAME} version: %(version)s",
    help=f"Show {CLI_COMMAND_NAME} CLI version.",
)    
@click.pass_context
def cli(ctx):
    pass

cli.add_command(say)
cli.add_command(config)

@cli.result_callback()
@click.pass_context
def process_result(*args, **kwargs):
  pass

def main():
    cli(prog_name=CLI_COMMAND_NAME, obj={})

if __name__ == "__main__":
    main()
