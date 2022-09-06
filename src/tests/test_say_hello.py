from click.testing import CliRunner
from poc_cli_translations.cli import cli

def test_say_hello():
    runner = CliRunner()
    result = runner.invoke(cli, ["say", "hello", "stacker"])
    
    assert result.exit_code == 0
    assert result.output == "Hello stacker!\n"