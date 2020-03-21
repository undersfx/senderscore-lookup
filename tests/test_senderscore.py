from senderscore import senderscore
import pytest


def test_is_valid_ip_true():
    assert senderscore.is_valid_ip('179.188.249.171')


def test_is_valid_ip_false():
    assert not senderscore.is_valid_ip('179.188.249.1711')


def test_get_score_success_type():
    score = senderscore.get_score('179.188.249.171')
    assert isinstance(score, str)


def test_get_score_failed_type():
    score = senderscore.get_score('179.188.249.1711')
    assert isinstance(score, str)


def test_cli_success(capsys):
    senderscore.cli('179.188.249.171')
    captured = capsys.readouterr()
    assert '179.188.249.171 has senderscore' in captured.out


def test_cli_not_valid_ip_exit():
    with pytest.raises(SystemExit):
        senderscore.cli('179.188.249.1710')


def test_cli_not_found_exit():
    with pytest.raises(SystemExit):
        senderscore.cli('179.188.249.0')
