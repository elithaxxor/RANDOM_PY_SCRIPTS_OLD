
def is_WindowsAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def getRoot():
    while True:
        if 'Linux' in platform.system():  ## get root for linux
            try:
                print('X' * 35)
                print(f' {red} It Seems Like your on a Linux Distro, Please start with escalate privledge. {reset} ')
                if not 'SUDO_UID' in os.environ.keys():  ##
                    print(f'**{red}Must have SU Privledges.{reset}')
                    print('[SYSTEM] Commencing Login Process. \n Enter your Password: ')
                    print('X' * 35)
                    password = getpass('* ')
                    print()
                    proc = Popen('sudo -S apache2ctl restart'.split(), stdin=PIPE, stderr=PIPE)
                    proc.communicate(password.encode())
                    if proc.communicate:
                        print(f'**{yellow}Sudo Escelation Succesfull, moving on.. {reset}')
                        break
                    print(f'{red}** Sudo failed, attempting to run w/out privledges.. {reset}')
                    break
            except Exception as e:
                traceback.print_exc()
                print('IO ERROR - MUST BE SUPER USER()): ', e)
                sys.exit(1)

        if 'Windows' in platform.system():
            print(f' {red} It Seems Like your on a Windows Distro, Checking if you are admin. {reset} ')
            if is_admin():  ## windows login
                print(f'{yellow}**cool you are admin.. moving on.{reset}')
                break
            else:
                print(f'{yellow}** Attempting To Escelate Privledges{reset}')
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                if ctypes.windll.shell32.ShellExecuteW:
                    print(f'{yellow} Windows Admin Escalation Succesful, moving on.. {reset}')
                    break
                else:
                    print(f'{red}**[ERRNO]Cannot escalate.. proceeding without privledge.. ')
                    break
        if 'Darwin' in platform.system():  ## get root for Mac
            try:
                print('X' * 35)
                print(f' {red} It Seems Like your on a Linux Distro, Please start with escalate privledge. {reset} ')
                if not 'SUDO_UID' in os.environ.keys():  ##
                    print(f'**{red}Must have SU Privledges.{reset}')
                    print('[SYSTEM] Commencing Login Process. \n Enter your Password: ')
                    print('X' * 35)
                    password = getpass('* ')
                    print()
                    proc = Popen('sudo -S apache2ctl restart'.split(), stdin=PIPE, stderr=PIPE)
                    proc.communicate(password.encode())
                    if proc.communicate:
                        print(f'**{yellow}Sudo Escelation Succesfull, moving on.. {reset}')
                        break
                    print(f'{red}** Sudo failed, attempting to run w/out privledges.. {reset}')
                    break
            except OSError as ose:
                print(str(ose))
            except Exception as E:
                traceback.print_exc()
                print(str(E))
                print('IO ERROR - MUST BE SUPER USER()): ', e)
                sys.exit(1)

def install():
    sucessfull_install = []
    subprocess.check_call([sys.executable, "-m", "pip", "install", threading])
    if subprocess.check_call:
        print(f'{yellow} Sucessfully Installed PIP')
        sucessful_install.append('pip')
    subprocess.check_call([sys.executable, "-m", "tqdm", "install", tqdm])
    if subprocess.check_call:
        print(f'{yellow} Sucessfully Installed TQDM')
    subprocess.check_call([sys.executable, "-m", "pip", "datetime", datetime])
    if subprocess.check_call:
        print(f'{yellow} Sucessfully Installed datetime')

    print('')


def main():
    is_WindowsAdmin()
    getRoot()
    install()
    
if __name__ == '__main__':
    main()
