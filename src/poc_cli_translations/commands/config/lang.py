import click
import json
import os
from poc_cli_translations import LANGUAGE_FILE, CLI_DIR


@click.command()
@click.argument("lang", type=click.Choice(["en", "fr", "pt"], case_sensitive=False))
@click.pass_context
def lang(ctx, lang: str):
    """Command to say hello"""
    try:
        __create_language_file(lang)
        print("OK")
    except Exception:
        print("NOK")

    
def __create_language_file(content: dict):
    try:
        if not CLI_DIR.exists():
            os.mkdir(CLI_DIR)
        with open(LANGUAGE_FILE, "w", encoding="utf-8") as language_file:
            language_file.write(json.dumps(content))

    except Exception as err:
        print(f"Couldn't create activation file at {LANGUAGE_FILE}")
        raise err
