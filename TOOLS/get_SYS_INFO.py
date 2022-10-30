current_platform = platform.system()
platform_name = sys.platform
while True:
    print(f'{yellow}[CHECKING OS]{reset}')
    if 'Darwin' in current_platform:
        print(f'{red} Your OS [{current_platform}] || [{platform_name}] \n* You may run into a few issues-**{reset}')
        period_wait()
        clear()
        break
    elif 'Windows' in current_platform:
        print(f'{red} Your OS [{current_platform}] || [{platform_name}] sucks. \n**FUCK-WINDOWS-**{reset}')
        period_wait()
        clear()
        break
    elif 'Linux' in current_platform or 'Ubuntu' in current_platform or 'Kali' in current_platform:
        print(f'[DETECTED LINUX]')
        print(f'{yellow}**Your OS [{current_platform}] || Platform [{platform_name}]')
        period_wait()
        clear()
        break


try:
    terminal = os.environ.get('TERM')
        width_len = width
        cwd = os.getcwd()
        #  IP_INFO = f"\033[1;35;0m {IPx.IP}"
        current_version = platform.release()
        system_info = platform.platform()
        os_name0 = platform.system()
        current_platform = platform.system()
        platform_name = sys.platform
        ## new adds
        big_names = platform.uname()
        processor = platform.processor()
        architecture = platform.architecture()
        user_id = os.uname()
        login = os.getlogin()

        print()
        print('X'*50)
        print(f'**[SYSTEM INFO]**'.center(width))
        print()
        print(f'\033[1;35;m [CURRENT_PLATFORM]--[{current_platform}]  ...? '.center(width))
        print(f'\033[1;35;m [PLATFORM_NAME]--[{platform_name}]  ...? '.center(width))
        print(f'\033[1;35;m [CURRENT_VERSION]--[{current_version}]  ...? '.center(width))
        print(f'\033[1;35;m [OS-NAME]--[{os_name0}] + [{terminal}] ...? '.center(width))
        print(f'\033[1;35;m [SYSTEM-INFO]--[{system_info}]  ...? '.center(width))
        print(f'\033[1;35;0m [CURRENT-VERSION]--[{current_version}]  ...? '.center(width))
        print(f'\033[1;35;0m [UUID]--[{big_names}]  ...? '.center(width))
        print(f'\033[1;35;0m [PROCESSOR]--[{processor}]  ...? '.center(width))
        print(f'\033[1;35;0m [ARCHITECTURE]--[{architecture}]  ...? '.center(width))
        print(f'\033[1;35;0m [USER-ID]--[{user_id}]  ...? '.center(width))
        print(f'\033[1;35;0m [LOGIN]--[{login}]  ...? '.center(width))
        print('X'*50)
        

except Exception as E:
    traceback.print_exc()
    print(str(E))
