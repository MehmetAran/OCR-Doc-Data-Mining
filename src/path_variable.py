def init_path():
    import os
    basePath = os.path.abspath(".")
    tesseract_path = basePath + "/resource/Tesseract-OCR"
    otherPaths = os.environ.get("PATH") +";"
    all_paths = otherPaths + tesseract_path;
    all_path_dict = dict()
    all_path_dict['PATH'] = all_paths
    os.environ.update(all_path_dict)
