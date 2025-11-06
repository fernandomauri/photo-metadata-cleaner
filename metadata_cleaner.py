"""
Author: Fernando Mauri
Maintainer: Fernando Mauri
Purpose: The following program is meant to do very simple image duplication in which EXIF metadata will be accessed and deleted.
"""

import os
import sys
import time

from spinner import loading

from PIL import Image


def get_format(image_file):
    """
    We want to parse the image file name to retrieve its extension.
    This will be useful for checking if an extension is valid and for saving the scrubbed image.
    """
    format_start = image_file.index(".")
    format = image_file[format_start:]

    return format


def is_valid_filetype(image_file):
    """
    The Pillow library does have support for many image filetypes, but some only have read permissions.
    We want to verify that the image file passed to the function has a valid extension with write permissions.
    """
    pil_formats = Image.registered_extensions()
    valid_file_types = [extension for extension, file_type in pil_formats.items() if file_type in Image.SAVE]
    file_format = get_format(image_file)

    if file_format in valid_file_types:
        return True
    else:
        return False


def scrub_image(image_file):
    """
    This will create a blank image, then copy the original image contents to the blank one.
    Doing so will strip the image of its EXIF (Exchangeable Image File Format), which includes device and sometimes GPS information.
    """
    format = get_format(image_file)
    try:
        opened_image = Image.open(image_file)
        pixels = list(opened_image.getdata())
        scrubbed_image = Image.new(opened_image.mode, opened_image.size)
        scrubbed_image.putdata(pixels)
        scrubbed_image.save(f"{image_file[:image_file.index('.')]}-SCRUBBED{format}")
    except Exception as e:
        print(f"Oh no! Image `{image_file}` could not be scrubbed. Error => {e}")
    else:
        print(f"Metadata for photo `{image_file}` has been successfully scrubbed.")


def check_path(image_path):
    """
    First check if the user input is valid and if so, label it as either a file or a directory.
    """
    if os.path.exists(image_path):
        if os.path.isfile(image_path):
            path_type = "file"
        elif os.path.isdir(image_path):
            path_type = "dir"
    else:
        return False

    return path_type


def scrub_directory(directory):
    """
    Traverse the directory contents and scrub each image file individually with other functions.
    """
    print("The path you entered is a directory. Scrubbing metadata from its contents...")
    directory = os.listdir(directory)
    try:
        for file in directory:
            print(file)
            check_and_scrub_file(file)
            loading()
    except Exception as e:
        print(f"Exception occurred while scrubbing directory items\' metadata. Error => {e}")
        raise
    else:
        print("Success! Directory scrub complete.")
        return


def check_and_scrub_file(image_file):
    """
    Before going through the process of trying to duplicate the image file, we want to make sure that it's the right file type. Otherwise, Pillow will try to work on unsupported file types and produce errors.
    """
    try:
        if is_valid_filetype(image_file):
            scrub_image(image_file)
            time.sleep(1)
        else:
            return
    except Exception as e:
        print(f"Whoops! There was an error while loading image file => {e}")
        raise
    else:
        return


def main():
    """
    This main function first checks if the input for the image(s) is a file or directory, then treats the input accordingly.
    I added two hardcoded image paths to feed into the function: the first is a directory, the second is a file.
    I also added a third option to run on user-defined filepaths with custom images.
    To test different outputs for `image_path`, comment and uncomment examples.
    """
    ### EXAMPLE 1 ###
    image_path = '/app/images'

    ### EXAMPLE 2 ##
    # image_path = '/app/images/crying_seal.jpeg'

    ### EXAMPLE 3 ###
    # image_path = str(input("Enter the path where the images are stored (ex. /app/my-images/my-image.jpeg) => "))

    file_or_dir = check_path(image_path)
    if file_or_dir == "dir":
        os.chdir(image_path)
        scrub_directory(image_path)
    else:
        try:
            check_and_scrub_file(file_or_dir)
        except Exception as e:
            print(f"Unable to load image. Error => {e}")


if __name__ == "__main__":
    main()
    sys.exit(0)
