from PIL import Image, ImageOps
import sys

ERRORMESSAGE = "Not a valid file extension, or in and out file not same " \
    "extension"
USEABLE_EXTENSIONS = (".jpg", ".jpeg", ".png")


def main():
    # if the user does not specify exactly two command-line arguments,
    if len(sys.argv) != 3:
        sys.exit("Usage pyton shirt.py 'infile' 'outfile'")

    in_file = sys.argv[1].lower()
    out_file = sys.argv[2].lower()

    '''
    TODO
    - If the input's and output's names do not end in
    .jpg, .jpeg, or .png, case-insensitively
    - If the input's name does not have the same
    extension as the output's name, or
    '''
    if not (
        in_file.endswith(USEABLE_EXTENSIONS) and
        out_file.endswith(USEABLE_EXTENSIONS)
    ):
        sys.exit(f"Valid file formats are {USEABLE_EXTENSIONS}")

    # This one I do feel good about!
    # index -1 is last index.
    if in_file.split(".")[-1] != out_file.split(".")[-1]:
        sys.exit("In- and outfile not same extension")

    converted_image = convert(in_file)

    pasted_image = overlay_image(converted_image)

    save_image(pasted_image, out_file)


def convert(raw_background_file):
    with Image.open(raw_background_file) as im:
        x = ImageOps.fit(im, (600, 600), centering=(0.5, 0.5))
        return x


def overlay_image(background):
    with Image.open("shirt.png") as im:

        '''
        I dont need the box if i just want to use 0,0
        I'll keep it as a reminder

        Since shirt.png has its own alpha channel,
        it is ok to pass it in a the mask value'
        '''

        background.paste(im, (0, 0), im)
        return background


def save_image(picture, outfile):
    picture.save(outfile)


if __name__ == "__main__":
    main()
