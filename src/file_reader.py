class CustomFileReader:
    def __init__(self, filepath):
        self._filepath = filepath

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        if not value.endswith(".txt"):
            raise ValueError("Only .txt files are allowed")
        self._filepath = value

    def line_generator(self):
        """Yields one line at a time from the file."""
        with open(self._filepath, "r") as file:
            for line in file:
                yield line

    def get_lines_containing(self, keyword):
        """Returns lines that contain a given keyword."""
        return [line for line in self.line_generator() if keyword in line]

    def __str__(self):
        return f"<CustomFileReader: {self._filepath}>"
    
    @staticmethod
    def is_txt_file(path):
        """Static method to check if a file is .txt."""
        return path.endswith(".txt")

    @classmethod
    def from_filename(cls, filename):
        """Class method to create reader from just a filename."""
        if not filename.endswith(".txt"):
            filename += ".txt"
        return cls(filename)

    def __add__(self, other):
        """Add (concatenate) two files into a new one."""
        import os
        basename1 = os.path.basename(self.filepath).replace(".txt", "")
        basename2 = os.path.basename(other.filepath)
        new_file = f"merged_{basename1}_{basename2}"
        with open(new_file, "w") as out:
            out.writelines(self.line_generator())
            out.writelines(other.line_generator())
        return CustomFileReader(new_file)
