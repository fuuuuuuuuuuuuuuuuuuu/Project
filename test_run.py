from src.file_reader import CustomFileReader

# Create sample files
with open("sample.txt", "w") as f:
    f.write("Hello world\nThis is a test\nPython is cool\n")

with open("sample2.txt", "w") as f:
    f.write("Another file\nWith different lines\nPython is fun\n")

# Create reader instances
r1 = CustomFileReader("sample.txt")
r2 = CustomFileReader("sample2.txt")

# Test @property
print("Filepath:", r1.filepath)

# Test generator
print("\nLines from r1:")
for line in r1.line_generator():
    print(line.strip())

# Test list comprehension
print("\nLines containing 'Python':", r1.get_lines_containing("Python"))

# Test static method
print("\nIs '.txt' file?", CustomFileReader.is_txt_file("sample.csv"))

# Test class method
r3 = CustomFileReader.from_filename("new_file")
print("Created from filename:", r3)

# Test __add__
print("\nMerging r1 and r2...")
merged = r1 + r2
print("Merged file created:", merged.filepath)

from src.file_merger import CustomFileMerger

merger = CustomFileMerger("sample.txt")
merged_all = merger.concat_multiple(r2, r3)
print("Multi-file merged:", merged_all.filepath)

from src.utils import deco

@deco("red")
def danger_msg():
    return "🔥 Something went wrong!"

@deco("green")
def success_msg():
    return "✅ All tests passed!"

print(danger_msg())
print(success_msg())
