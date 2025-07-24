import os
import mimetypes
from utils import deco

class CustomFileReader:
    """
    File reader that uses a generator to read lines, supports filtering,
    merging with __add__, and factory methods.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    @property
    def filepath(self) -> str:
        return self._filepath

    @filepath.setter
    def filepath(self, value: str):
        """
        Validates that the file path is a .txt file.

        Raises:
            ValueError: If the file is not a .txt.
        """
        if not self.is_txt_file(value):
            raise ValueError("Only .txt files are allowed")
        self._filepath = value

    def line_generator(self):
        """
        Generator that yields one line at a time from the file.
        """
        with open(self._filepath, "r", encoding="utf-8") as file:
            for line in file:
                yield line

    def get_lines_containing(self, keyword: str):
        """
        Returns a list of lines containing the keyword.

        Args:
            keyword (str): Substring to search for.

        Returns:
            List[str]: Matching lines including newline.
        """
        return [line for line in self.line_generator() if keyword in line]

    @deco("blue")
    def display_lines_with_keyword(self, keyword: str):
        """
        For demo: returns all lines containing keyword, colored blue.
        """
        return "".join(self.get_lines_containing(keyword))

    def __str__(self):
        return f"<CustomFileReader: {self._filepath}>"

    @staticmethod
    def is_txt_file(path: str) -> bool:
        """
        Checks MIME type to confirm text/plain.
        """
        mime_type, _ = mimetypes.guess_type(path)
        return mime_type == "text/plain"

    @classmethod
    def from_filename(cls, filename: str):
        """
        Factory method that adds .txt extension if missing.
        """
        if not filename.endswith(".txt"):
            filename += ".txt"
        return cls(filename)

    def __add__(self, other):
        """
        Concatenate two text files into a new file.
        Returns a new CustomFileReader for the merged file.
        """
        basename1 = os.path.basename(self.filepath).replace(".txt", "")
        basename2 = os.path.basename(other.filepath).replace(".txt", "")
        new_file = f"merged_{basename1}_{basename2}.txt"
        with open(new_file, "w", encoding="utf-8") as out:
            out.writelines(self.line_generator())
            out.writelines(other.line_generator())
        return CustomFileReader(new_file)


if __name__ == "__main__":
    """
    Entry point for running a simple demo using CustomFileReader.
    - Creates a demo text file if it doesn't exist
    - Reads lines containing a keyword
    - Displays them with ANSI color using a decorator
    """
    demo_path = "demo.txt"

    if not os.path.exists(demo_path):
        with open(demo_path, "w", encoding="utf-8") as f:
            f.write("Line one\n")
            f.write("Blue line with word Python inside\n")
            f.write("Line three\n")

    reader = CustomFileReader(demo_path)
    colored_output = reader.display_lines_with_keyword("Python")
    print(colored_output)