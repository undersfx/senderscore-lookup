from argparse import ArgumentParser
from senderscore import senderscore
import pytest

IP = '179.188.249.171'
INVALID_IP = '179.188.249.1717'
NO_SCORE_IP = '179.188.249.0'


@pytest.fixture(scope='session')
def parser():
    parser = senderscore.config_parser()
    return parser


def test_is_valid_ip_true():
    assert senderscore.is_valid_ip(IP)


def test_is_valid_ip_false():
    assert not senderscore.is_valid_ip(INVALID_IP)


def test_get_score_success_type():
    score = senderscore.get_score(IP)
    assert isinstance(score, str)


def test_get_score_failed_type():
    score = senderscore.get_score(INVALID_IP)
    assert isinstance(score, str)


def test_cli_success(capsys):
    senderscore.cli(IP)
    captured = capsys.readouterr()
    assert f'{IP} has senderscore' in captured.out


def test_cli_not_valid_ip_exit():
    with pytest.raises(SystemExit):
        senderscore.cli(INVALID_IP)


def test_cli_not_found_exit():
    with pytest.raises(SystemExit):
        senderscore.cli(NO_SCORE_IP)


def test_config_parser_prog_attribute(parser):
    assert parser.prog == 'Sender Score Lookup'


def test_config_parser_type(parser):
    assert isinstance(parser, ArgumentParser)
