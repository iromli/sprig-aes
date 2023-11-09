from click.testing import CliRunner


def test_cli_encrypt():
    from sprig_aes.cli import encrypt

    runner = CliRunner()
    result = runner.invoke(
        encrypt,
        ["a secret message", "--key", "6Jsv61H7fbkeIkRvUpnZ98fu"],
    )
    assert result.exit_code == 0
    assert result.output.strip() == "zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C"


def test_cli_encrypt_key_file():
    from sprig_aes.cli import encrypt

    runner = CliRunner()

    with runner.isolated_filesystem():
        with open("key.txt", "w") as f:
            f.write("6Jsv61H7fbkeIkRvUpnZ98fu")

        result = runner.invoke(
            encrypt,
            ["a secret message", "--key-file", "key.txt"],
        )
        assert result.exit_code == 0
        assert result.output.strip() == "zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C"


def test_cli_encrypt_no_key():
    from sprig_aes.cli import encrypt

    runner = CliRunner()
    result = runner.invoke(
        encrypt,
        ["a secret message"],
    )
    assert result.exit_code == 1
    assert "Aborted" in result.output.strip()


def test_cli_decrypt():
    from sprig_aes.cli import decrypt

    runner = CliRunner()
    result = runner.invoke(
        decrypt,
        ["zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C", "--key", "6Jsv61H7fbkeIkRvUpnZ98fu"],
    )
    assert result.exit_code == 0
    assert result.output.strip() == "a secret message"


def test_cli_decrypt_key_file():
    from sprig_aes.cli import decrypt

    runner = CliRunner()

    with runner.isolated_filesystem():
        with open("key.txt", "w") as f:
            f.write("6Jsv61H7fbkeIkRvUpnZ98fu")

        result = runner.invoke(
            decrypt,
            ["zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C", "--key-file", "key.txt"],
        )
        assert result.exit_code == 0
        assert result.output.strip() == "a secret message"


def test_cli_decrypt_no_key():
    from sprig_aes.cli import decrypt

    runner = CliRunner()
    result = runner.invoke(
        decrypt,
        ["zLBGM41dAfA2JuIkVHRKaxO7SO8JXrhsDdD3W6XwPrQVsORCA0a4WpPG2rm8GG9C"],
    )
    assert result.exit_code == 1
    assert "Aborted" in result.output.strip()
