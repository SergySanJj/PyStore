from PIL import Image, ImageDraw, ImageFont
import os
import shutil


def compress(fileInput, fileOutput, qualityOutput=50):
    try:
        im = Image.open(fileInput)
        im.save(fileOutput, optimize=True, quality=qualityOutput)
    except:
        print("File " + fileInput + " was not compressed")


def isImage(file):
    filename, file_extension = os.path.splitext(file)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if file_extension in image_extensions:
        return True
    return False


def compressSubdirs(rootDirectory, copyUncompressable=True):
    print('*** Compression Started ***')
    totalFileCount = 0
    totalFileCompressedCount = 0
    for subdir, dirs, files in os.walk(rootDirectory):
        for file in files:
            totalFileCount += 1
            compressed_dir = rootDirectory + '_compressed/' + \
                os.path.relpath(subdir, rootDirectory) + '/'

            if not os.path.exists(compressed_dir):
                os.makedirs(compressed_dir)

            if isImage(file):
                compress(os.path.join(subdir, file),
                         compressed_dir + file)
                totalFileCompressedCount += 1
            elif copyUncompressable:
                shutil.copy(os.path.join(subdir, file), compressed_dir + file)

    print('Total files compressed/handled: ' +
          str(totalFileCompressedCount) + "/" +
          str(totalFileCount))
    print('*** Compression Ended ***')
