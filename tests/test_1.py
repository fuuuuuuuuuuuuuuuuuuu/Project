import os
import sys
import pytest

# Ensure the project src/ folder is discoverable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from file_reader import CustomFileReader
from file_merger import CustomFileMerger

@pytest.fixture
def professor_file(tmp_path):
    f = tmp_path / 'professor.txt'
    lines = [
        'Alpha line\n',
        'Beta with Python keyword\n',
        'Gamma line\n',
        'Python appears again\n'
    ]
    f.write_text(''.join(lines))
    return str(f)

@pytest.fixture
def extra_file(tmp_path):
    f = tmp_path / 'extra.txt'
    lines = [
        'Extra content\n',
        'Another Python occurrence\n'
    ]
    f.write_text(''.join(lines))
    return str(f)

def test_professor_generator_and_filter(professor_file):
    reader = CustomFileReader(professor_file)
    all_lines = list(reader.line_generator())
    assert len(all_lines) == 4

    python_lines = reader.get_lines_containing('Python')
    # ✅ Strip trailing newlines to match expected values
    python_lines = [line.strip() for line in python_lines]

    assert python_lines == [
        'Beta with Python keyword',
        'Python appears again'
    ]

def test_professor_add_and_merger(professor_file, extra_file, tmp_path):
    r1 = CustomFileReader(professor_file)
    r2 = CustomFileReader(extra_file)

    # Test __add__
    merged_one = r1 + r2
    content_one = open(merged_one.filepath, 'r').read()
    assert 'Alpha line' in content_one
    assert 'Extra content' in content_one

    # Test multiple concat
    merger = CustomFileMerger(professor_file)
    merged_multi = merger.concat_multiple(r2, r1)
    content_multi = open(merged_multi.filepath, 'r').read().splitlines()

    assert content_multi[0] == 'Alpha line'
    assert any('Extra content' in line for line in content_multi)
    assert any('Python keyword' in line for line in content_multi)
