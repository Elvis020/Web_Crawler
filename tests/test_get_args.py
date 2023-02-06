import os
import pytest

from subprocess import getstatusoutput


class TestGetArgs:

    @pytest.fixture
    def prg(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, '..', 'app.py'))
        return f'python {file_path}'

    def test_get_args_with_h_params(self, prg):
        for flag in ['-h', '--help']:
            rv, out = getstatusoutput(f'{prg} {flag}')
            assert rv == 0
            assert out.lower().startswith('usage')

    def test_get_args_with_url_params(self, prg):
        my_url = 'https://www.turntabl.io'
        for flag in [f'-u {my_url}', f'--url {my_url}']:
            rv, out = getstatusoutput(f'{prg} {flag}')
            assert rv == 0
            assert out.startswith('Gathering all links')

    @pytest.mark.skip
    def test_get_args_with_deepcrawl_params(self, prg):
        for flag in [f'-d', f'--deepcrawl']:
            rv, out = getstatusoutput(f'{prg} {flag}')
            assert rv == 0
            assert out.startswith('Gathering all links')
