import pytest
from src.file_reader import CustomFileReader

@pytest.fixture
def sample_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Line one\nLine two\nLine three with Python\n")
    return str(file)

def test_generator_reads_lines(sample_file):
    reader = CustomFileReader(sample_file)
    lines = list(reader.line_generator())
    assert len(lines) == 3
    assert lines[2] == "Line three with Python\n"

def test_keyword_filtering(sample_file):
    reader = CustomFileReader(sample_file)
    python_lines = reader.get_lines_containing("Python")
    assert python_lines == ["Line three with Python\n"]

from src.file_merger import CustomFileMerger

@pytest.fixture
def another_file(tmp_path):
    file = tmp_path / "another.txt"
    file.write_text("Another line\nWith content\n")
    return str(file)

def test_add_creates_combined_file(tmp_path, sample_file, another_file):
    r1 = CustomFileReader(sample_file)
    r2 = CustomFileReader(another_file)

    merged = r1 + r2
    with open(merged.filepath) as f:
        contents = f.read()

    assert "Line one" in contents
    assert "Another line" in contents

def test_concat_multiple(tmp_path, sample_file, another_file):
    merger = CustomFileMerger(sample_file)
    r2 = CustomFileReader(another_file)

    # Create a 3rd file
    file3 = tmp_path / "third.txt"
    file3.write_text("Third file line\n")
    r3 = CustomFileReader(str(file3))

    merged = merger.concat_multiple(r2, r3)

    with open(merged.filepath) as f:
        all_lines = f.readlines()

    assert any("Third file" in line for line in all_lines)
    assert len(all_lines) >= 5
