# Create and Write to a File
with open("example.txt", "w") as f:
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")
    f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read Entire Content
with open("example.txt", "r") as f:
    print("📄 Full Content:\n", f.read())

# Read Line by Line
with open("example.txt", "r") as f:
    print("\n📌 Reading Line by Line:")
    for line in f:
        print(line.strip())

# Read First Line using readline()
with open("example.txt", "r") as f:
    print("\n🔹 First Line:", f.readline().strip())

# Read All Lines into a List
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("\n📋 Readlines (List of Lines):")
    for line in lines:
        print(line.strip())

# Append Data to the File
with open("example.txt", "a") as f:
    f.write("This is appended line 1.\n")
    f.write("This is appended line 2.\n")

# Demonstrate seek() and tell()
with open("example.txt", "r") as f:
    print("\n🧭 File Pointer Demo:")
    print("Position:", f.tell())
    print("Reading:", f.readline().strip())
    print("Position after reading:", f.tell())
    f.seek(0)
    print("Reset position to:", f.tell())
    print("Reading again:", f.readline().strip())

# Exclusive Creation using 'x' mode
try:
    with open("unique_file.txt", "x") as f:
        f.write("This file was created using 'x' mode.")
        print("\n✅ 'unique_file.txt' created successfully.")
except FileExistsError:
    print("\n⚠️ 'unique_file.txt' already exists!")

# Copy File Function
def copy_file(source, destination):
    try:
        with open(source, "r") as src, open(destination, "w") as dest:
            for line in src:
                dest.write(line)
        print(f"\n📁 File copied from '{source}' to '{destination}'.")
    except FileNotFoundError:
        print(f"\n❌ Error: Source file '{source}' not found.")
    except Exception as e:
        print(f"\n🚨 Unexpected Error: {e}")

# Call the copy function
copy_file("example.txt", "example_copy.txt")
