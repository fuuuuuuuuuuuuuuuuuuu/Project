from src.file_reader import CustomFileReader

class CustomFileMerger(CustomFileReader):
    def __init__(self, filepath):
        super().__init__(filepath)

    def __str__(self):
        return f"<CustomFileMerger: {self._filepath}>"

    def concat_multiple(self, *readers):
        """
        Concatenates this file + all other given reader objects into a new file.
        Returns a new CustomFileMerger instance.
        """
        import os
        basename = os.path.basename(self.filepath)
        new_file = f"merged_multi_{basename}"
        with open(new_file, "w") as out:
            out.writelines(self.line_generator())
            for reader in readers:
                out.writelines(reader.line_generator())
        return CustomFileMerger(new_file)
