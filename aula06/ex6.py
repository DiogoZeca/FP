from tkinter import filedialog

def main():
    f1 = filedialog.askopenfilename(title="Choose File")
    f2 = filedialog.askopenfilename(title="Choose File")

    print(compareFiles(f1, f2))

def compareFiles(fileName1, fileName2):
    with open(fileName1, 'rb') as file1:
        with open(fileName2, 'rb') as file2:
            while True:
                f1 = file1.read(1024)
                f2 = file2.read(1024)
                if f1 != f2:
                    return False
                if not f1:
                    return True

main()