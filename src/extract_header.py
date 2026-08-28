def extract_title(markdown):
    lineas = markdown.split("\n")
    print(f"lineas {lineas}")
    if len(lineas):
        for linea in lineas:
            if linea.startswith("# "):
                return linea[1:].strip()
        raise Exception("Header not found")
