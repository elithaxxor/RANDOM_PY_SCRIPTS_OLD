import sys, os

class Colors:
    reset = "\033[0m"

    # Black
    fgBlack = "\033[30m"
    fgBrightBlack = "\033[30;1m"
    bgBlack = "\033[40m"
    bgBrightBlack = "\033[40;1m"

    # Red
    fgRed = "\033[31m"
    fgBrightRed = "\033[31;1m"
    bgRed = "\033[41m"
    bgBrightRed = "\033[41;1m"

    # Green
    fgGreen = "\033[32m"
    fgBrightGreen = "\033[32;1m"
    bgGreen = "\033[42m"
    bgBrightGreen = "\033[42;1m"

    # Yellow
    fgYellow = "\033[33m"
    fgBrightYellow = "\033[33;1m"
    bgYellow = "\033[43m"
    bgBrightYellow = "\033[43;1m"

    # Blue
    fgBlue = "\033[34m"
    fgBrightBlue = "\033[34;1m"
    bgBlue = "\033[44m"
    bgBrightBlue = "\033[44;1m"

    # Magenta
    fgMagenta = "\033[35m"
    fgBrightMagenta = "\033[35;1m"
    bgMagenta = "\033[45m"
    bgBrightMagenta = "\033[45;1m"

    # Cyan
    fgCyan = "\033[36m"
    fgBrightCyan = "\033[36;1m"
    bgCyan = "\033[46m"
    bgBrightCyan = "\033[46;1m"

    # White
    fgWhite = "\033[37m"
    fgBrightWhite = "\033[37;1m"
    bgWhite = "\033[47m"
    bgBrightWhite = "\033[47;1m"

######
color = Colors()
yellow = color.fgYellow
red = color.fgRed
blue = color.fgBlue
bblue = color.fgBrightBlue
cyan = color.fgCyan
reset = color.reset
############


def display_all_files():
    global root, dirs
    print('Enter path to display all files')
    p = input("")
    no_append = ['none', 'n', 'no', 'c', 'cancel']
    path_str = str(p)  ### <--- may have to do that weird object thing
    exclude_extension = [path_str]
    include_extension = ['.txt', '.iso', '.doc', '.rar', '.tar', '.odt',
                         '.gz']  ## might have to take out '', it could pull in folders


    print(f' :: Exclusion list, after being parsed thru glob converter :: ')
    print(f' :: \t\t RE_INCLUDE \t\t\t  RE_EXCLUDE:: ')
    # print(f' :: {re_include} parsed thru glob converter :: ')

    print('X' * 50), print(), print()

    ## glob.glob to print all files
    # if input has . in it add to list, if no . start, restart recursion
    print('X' * 30)
    print(f'{blue} list for os.walk {reset}')
    print(f'{blue}|| -- root--  || -- dirs -- || -- files -- || {reset}')
    for root, dirs, files in os.walk(p):
        print(f'{bblue}{root}, \n\n|| {dirs} ||\n\n {files}{reset}')
        helluvaString = f'\n{root} + \n{dirs} + \n{files}'
        print(f'write_osWalk :: {write_osWalk}')
        print('HELLUVASTRING : ', helluvaString)
        os_walk_parent = get_info.getParentDirectoryFromFile(dirs)
        print(f'File found in :: \n {os_walk_parent}')

    print(), print()
    print('x' * 50)
    print(f'{yellow}** list for glob.glob() {reset}')
    str_p = p
    str_p = str(str_p)
    print('string_p', type(str_p))
    print('string_p', str_p)
    print('root from above', root)
    print('dirs from above', dirs)

    print(f'{yellow}**Globbed-files with wildcard ranges:{reset}')
    print('X' * 50)
    str_p = str(p)
    str_p = str_p + f'**/**'
    print('string_p', str_p)

    for root, dirs, files in os.walk(p, followlinks=True):
        files = [os.path.join(root, f) for f in files]
        print()
        print(f'{yellow} :: root :: {reset}')
        print(root)
        print('X' * 50)
        print(f'{yellow} :: dirs :: {reset}')
        print(dirs)
        print()
        print('X' * 50)
        print(f'{yellow} :: files :: {reset}')
        print(files)
        print()

    str_parent = str_p
    print('string_p', str_p)
    for globbed_files00 in glob.glob(str_p, recursive=True):
        pprint.pprint(globbed_files00)
        print(f'{yellow}globbed_files{reset}')
        print(f'{blue}{globbed_files00}{reset}')
        globbed_parent = get_info.getParentDirectoryFromFile(str_p)
        print(f' :: {yellow} Found File in :: {reset}\n {globbed_parent}')

    for globbed_files01 in glob.glob(str_parent, recursive=True):
        pprint.pprint(globbed_files01)
        print(f'{yellow} globbed_files01 {reset}')
        print(f'{blue} {globbed_files01} {reset}')
        globbed_parent01 = get_info.getParentDirectoryFromFile(str_p)
        print(f' :: {yellow} Found File in :: {reset}\n {globbed_parent01}')

    for globbed_files02 in glob.glob(f'/{str_p}*[0-9].*', recursive=True):
        print(f'{yellow} globbed_files02 {reset}')
        print(f'{blue} {globbed_files02} {reset}')
        globbed_parent02 = get_info.getParentDirectoryFromFile(str_p)
        print(f' :: {yellow} Found File in :: {reset}\n {globbed_parent02}')

    print(), print()
    print('X' * 50)
    print(f'glob {write_glob}')
    print(f'write_globStat {write_globStat}'), print(), print()
    print('X' * 50)


def main():
    display_all_files()

main()
