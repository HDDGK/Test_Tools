import os
# libs={"numpy","pillow","sklearn","requests","pydf2","pyqt5"}
libs={""}
try:
    for lib in libs:
        os.system("pip install "+lib)
    print("successful")
except:
    print("failed")