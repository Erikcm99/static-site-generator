import os
import shutil
def copy_recursive(src:str, dest:str):
    if not os.path.exists(src):
        raise Exception("src path not found")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    print(f"src:{src}")    
    list_dir = os.listdir(src)
    if len(list_dir):
        for element in list_dir:
            element_path = os.path.join(src,element)
            if os.path.isfile(element_path):
                shutil.copy(element_path,dest)
            elif os.path.isdir(element_path):
                copy_recursive(element_path,os.path.join(dest,element))

