import os
from file_reader import CustomFileReader

class CustomFileMerger(CustomFileReader):
    """
    Extends CustomFileReader with ability to merge multiple readers.
    """

    def __str__(self):
        return f"<CustomFileMerger: {self._filepath}>"

    def concat_multiple(self, *readers):
        """
        Concatenate this file and any number of other CustomFileReader instances.
        """
        base = os.path.basename(self.filepath).replace(".txt", "")
        new_file = f"merged_multi_{base}.txt"
        with open(new_file, "w", encoding="utf-8") as out:
            out.writelines(self.line_generator())
            for reader in readers:
                out.writelines(reader.line_generator())
        return CustomFileMerger(new_file)
