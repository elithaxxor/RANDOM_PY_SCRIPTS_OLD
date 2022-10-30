import os, sys

def organize_junk():
    for entry in os.scandir(self.p):
        if os.path.isdir(entry):
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath(file_path))
        removed_dirs = []
        for dir in os.scandir():
            try:
                os.rmdir(dir)
                removed_dirs.append(dir)
                return f'[+] List of Removed Dirs \n {removed_dirs}'
            except:
                return f'[+] List of Removed Dirs \n {removed_dirs}'
                pass


def main():
    organize_junk()
main()
