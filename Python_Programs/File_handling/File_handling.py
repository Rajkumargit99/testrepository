
def read_file(file_path):
    file = open(file_path, "r")
    data = file.read()
    print(data)
    file.close()

read_file("Module1.txt")
print("------------------------------------------------------------------------")
def write_file(file_path, content):
    with open(file_path, "w") as wfile:
        wfile.write(content)
        print(content)

write_file("Module2.txt", "Learning data, and its replaceable")
print("------------------------------------------------------------------------")
write_file("Module3.txt", "Learning data, and its creating new file")
print("------------------------------------------------------------------------")
write_file(r"C:\Users\LENOVO\Desktop\Manual Testing\Module4.txt", "Learning data, and its append method")
print("------------------------------------------------------------------------")
def append_file(file_path, content):
    with open(file_path, "a") as pfile:
        pfile.write(content)
        print(content)

append_file("Module5.txt", '''Hi i am following the append method for now 
and this is the most usefull
and content for the py files
this is for example i am using this''')
print("------------------------------------------------------------------------")
def read_file_n_ltters(file_path, n_letters):
    with open(file_path, "r") as lr_file:
        data = lr_file.read(n_letters)
        print(data)

read_file_n_ltters("Module1.txt", 160)
print("------------------------------------------------------------------------")

def read_file_n_lines(file_path, n_lines):
    with open(file_path, "r") as lr_file:
        for _ in range(n_lines):
            print(lr_file.readline())

read_file_n_lines("Module1.txt", 6)
print("------------------------------------------------------------------------")

def read_file_line_no(file_path, line_no):
    with open(file_path, "r") as ar_file:
        lines_list = ar_file.readlines()
        print(lines_list)
        print(lines_list[line_no])

read_file_line_no("Module1.txt", 6)

print("------------------------------------------------------------------------")

