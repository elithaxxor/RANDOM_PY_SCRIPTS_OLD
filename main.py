import os, sys, traceback, io, time
import pyinstaller

# pip3 install pyinstaller

cwd = os.getcwd()
py_name = '/sample.py'
py_path = str(cwd) + py_name
dir_contents = os.listdir(cwd)


def conversion():
    pass

def main():
    print('[!] Py Script to convert file to .exe [change {py_name} in source]')
    print(f'[+] Working on {py_name}\n\n\t{py_path}')


if __name__ == "__main__":
    main()

#  pyinstaller --onefile -w (for gui)
#  pyinstaller --onefile (for cli)

pyinstaller --onefile py_name
