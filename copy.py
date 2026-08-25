import os
def copy(src:str, dest:str):
    if not os.path.exists(src):
        raise Exception("src path not found")
    if not os.path.exists(dest):
        raise Exception("dest path not found")

