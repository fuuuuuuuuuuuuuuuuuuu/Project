import os
import sys
import pytest

# Ensure src/ is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from file_reader import CustomFileReader
from file_merger import CustomFileMerger
from utils import deco

@pytest.fixture
def sample_file(tmp_path):
    f = tmp_path / 'sample.txt'
    f.write_text('Line one\nLine two\nLine three with Python\n')
    return str(f)

@pytest.fixture
def another_file(tmp_path):
    f = tmp_path / 'another.txt'
    f.write_text('Another line\nWith content\n')
    return str(f)

def test_generator_reads_lines(sample_file):
    r = CustomFileReader(sample_file)
    assert list(r.line_generator()) == [
        'Line one\n',
        'Line two\n',
        'Line three with Python\n'
    ]

def test_keyword_filtering(sample_file):
    r = CustomFileReader(sample_file)
    assert r.get_lines_containing('Python') == ['Line three with Python\n']

def test_add_creates_combined_file(tmp_path, sample_file, another_file):
    r1 = CustomFileReader(sample_file)
    r2 = CustomFileReader(another_file)
    merged = r1 + r2
    text = open(merged.filepath, 'r').read()
    assert 'Line one' in text and 'Another line' in text

def test_concat_multiple(tmp_path, sample_file, another_file):
    m = CustomFileMerger(sample_file)
    r2 = CustomFileReader(another_file)
    f3 = tmp_path / 'third.txt'
    f3.write_text('Third file line\n')
    r3 = CustomFileReader(str(f3))
    merged = m.concat_multiple(r2, r3)
    lines = open(merged.filepath, 'r').readlines()
    assert any('Third file line' in l for l in lines)
    assert len(lines) >= 4

def test_display_lines_cli_color(sample_file):
    r = CustomFileReader(sample_file)
    colored = r.display_lines_with_keyword('Python')
    assert colored.startswith('\x1b[94m')
    assert 'Line three with Python' in colored
    assert colored.endswith('\x1b[0m')

def test_decorator_on_string():
    @deco('green')
    def greet():
        return 'hello'
    result = greet()
    assert result == '\x1b[92mhello\x1b[0m'

def test_decorator_on_list():
    @deco('red')
    def get_lines():
        return ['a\n', 'b\n']
    result = get_lines()
    assert isinstance(result, list)
    assert all(line.startswith('\x1b[91m') and line.endswith('\x1b[0m') for line in result)
