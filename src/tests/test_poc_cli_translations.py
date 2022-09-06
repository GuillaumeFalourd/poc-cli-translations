from poc_cli_translations import main

def test_poc_cli_translations():
    result = main()
    assert result == 0 