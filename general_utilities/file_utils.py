import os


def generate_unique_filename(folder_path, base_filename):
    suffix = 1
    filename = base_filename
    file_ext = os.path.splitext(base_filename)[1]

    while os.path.exists(os.path.join(folder_path, filename)):
        filename = f"{os.path.splitext(base_filename)[0]}_{suffix}{file_ext}"
        suffix += 1

    return filename
