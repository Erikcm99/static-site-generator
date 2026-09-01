def extract_title(markdown):
    lineas = markdown.split("\n")
    for linea in lineas:
        if linea.startswith("#"):
            return linea[1:].strip()
    raise Exception("Header not found")
