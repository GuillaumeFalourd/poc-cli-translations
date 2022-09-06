# POC CLI Translations

POC using [Click](https://click.palletsprojects.com/en/8.1.x) and [python-i18n](https://pypi.org/project/python-i18n/#description) to test how to implement translations on a CLI tool.

## Usage

To setup the virtual environment, please run at the repository `root` directory:

```bash
python3 -m venv env
```

Then:

```bash
source env/bin/activate
```

And finally:

```bash
make install
```

Afterwards, the `poc` command should be available:

```bash
(env) ➜  poc-cli-translations git:(main) ✗ poc
Usage: poc [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help     Show command helper.
  -v, --version  Show poc CLI version.

Commands:
  config  Command to config something.
  say     Command to say a text.
```

## Commands

### Configure CLI output language

To configure the CLI output language, use the command below:

```bash
poc config lang en
```

3 languages are currently available:
- en (english)
- pt (portuguese)
- fr (french)

_Observation: It will print an `OK` message if the command is run successfully._

### Say Hello

To test the Hello World command line, use the command below:

```bash
poc say hello Bob
```

This should print an **Hello World** message, then a **Hi** message with the informed name, according to the language set in the previous command:

```text
Hello world!
Hi Bob!
```
