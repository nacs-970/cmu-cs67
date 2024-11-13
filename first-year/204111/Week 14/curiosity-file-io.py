# windows 'b' always at the end
#'r' reading
#'w' writing, truncating the file first / overwrite
#'x' exclusive creation, failing if the already exists
#'a' writing, appending at the end of the file if exists
#'b' binary
#'t' text
#'+' reading & writing
#'U' universal newlines
print("- write file -")
def write_file(filename, contents, mode="wt"):
    with open(filename,mode) as output:
        output.write(contents)
    print("created", filename)
write_file("./help.txt","please help me!")
print()
print("- del file -")
def delete_file(path):
    import os
    if os.path.exists(path):
        try:
            #os.remove(path)
            return True
        except FileNotFoundError:
            return False
    else:
        return False
print(delete_file("./help.txt"))
print()
print("- read file -")
def read_file(filename,mode="rt"):
    try:
        with open(filename,mode,encoding="utf-8") as input_:
            return input_.read()
    except FileNotFoundError:
        return None
print(read_file("./help.txt"))
print()
print("- I/O Redirection -")
def find_mean(contents):
    lines = contents.splitlines()
    total = int(lines[0]);sum = 0
    for i in range(total):
        current = float(lines[i+1])
        sum += current
    return sum/(len(lines) - 1)
print(find_mean(read_file("./scores.txt")))
print()
print("- Examples -")
print("smiley_print")
def smiley_print(filename):
    with open (filename,"rt") as f:
        for line in f:
            print(":)",line,end="")
smiley_print("./scores.txt")
print("---")
print("copy_smiley_print")
def copy_with_smiies(source,destination):
    with open (source,"rt") as infile:
        with open (destination,"wt") as outfile:
            for line in infile:
                outfile.write(":) " + line)
copy_with_smiies("scores.txt","smilies.txt")
print(read_file("smilies.txt"))
print("---")
print("dir_SMILEY")
import os
for file in os.listdir("."):
    if len(file) > 4 and file[-4:] == ".txt":
        print("Text :", file)
        print("SMILEY")
        smiley_print(file)
print("---")
print("smiley_buffer")
def smiley_buffer(filename):
    buff = []
    with open(filename, "rt") as f:
        for line in f:
            buff += [":) " + line]
    destination = filename
    with open(destination, "wt") as outfile:
        for line in buff:
            outfile.write(line)
smiley_buffer("scores-2.txt")
smiley_print("./scores-2.txt")
