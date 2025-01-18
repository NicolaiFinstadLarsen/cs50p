def main():
    # Stripping withspace and lower case
    name = input("File name: ").strip().lower()
    if name == "":
        exit(1)
    print(extension_mime_replace(name))


def extension_mime_replace(file):
    # Using dict since there was a lot of checks.
    extensions_dict = {".gif": "image/gif",
                       ".jpg": "image/jpeg",
                       ".jpeg": "image/jpeg",
                       ".png": "image/png",
                       ".pdf": "application/pdf",
                       ".txt": "text/plain",
                       ".zip": "application/zip"}
    # Itterate over all items in dict
    for key, value in extensions_dict.items():
        # If string ends with the dict key
        if file.endswith(key):
            # Return the dict value
            return value
    # This else: is not needed, but is in the spirit of the pset focusing on if, else \n
    # statments
    else:
        return "application/octet-stream"


main()
