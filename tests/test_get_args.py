import os
import pytest

from subprocess import getstatusoutput


class TestGetArgs:

    @pytest.fixture
    def prg(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, '..', 'app.py'))
        return f'python {file_path}'

    def test_get_args_with_h_param(self, prg):
        for flag in ['-h', '--help']:
            exitcode, out = getstatusoutput(f'{prg} {flag}')
            assert exitcode == 0
            assert out.lower().startswith('usage')

    def test_get_args_with_url_param(self, prg):
        my_url = 'https://www.turntabl.io'
        for flag in [f'-u {my_url}', f'--url {my_url}']:
            exitcode, out = getstatusoutput(f'{prg} {flag}')
            assert exitcode == 0
            assert out.startswith('Gathering all links')

    def test_get_args_with_threads_param(self, prg):
        for flag in [f'-t 3', f'--threads 3']:
            exitcode, out = getstatusoutput(f'{prg} {flag}')
            assert exitcode == 0