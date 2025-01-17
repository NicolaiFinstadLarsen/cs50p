def main():
    s = input("String: ")
    print(convert(s))

def convert(x):
    x = x.replace(":(","\N{slightly frowning face}")
    x = x.replace(":)","\N{slightly smiling face}")
    return x

    # I dont like this code line, its to long and not easy to read.
    # return x.replace(":(","\N{slightly frowning face}").replace(":)","\N{slightly smiling face}")

main()
