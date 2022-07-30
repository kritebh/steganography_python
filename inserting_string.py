# with open("image.jpg","ab") as f:
#     f.write(b"Hello World")


with open("image.jpg","rb") as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))

    f.seek(offset+2)
    print(f.read())
