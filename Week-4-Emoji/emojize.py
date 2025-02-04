import emoji

def main():
    my_string = emoji.emojize(input("Emoji: "), language="alias")
    print(my_string)

main()

