import store


if __name__ == "__main__":
    rootdir = r'/media'

    store.compressSubdirs(rootdir,copyUncompressable=False)
