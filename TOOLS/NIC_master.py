def available_nics():
    try:
        print('X' * 50)
        print(f'{yellow} Available  NICS  {reset}')
        with open("NIC_INFO.txt", 'a') as f:
            output01 = subprocess.run(["sudo", "lsusb", "-v", ], stdin=f,
                                      text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(output01)

            output02 = subprocess.run(["sudo", "lshw", "-C", "network" "-short"], stdin=f,
                                      text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(output02)
            time.sleep(2)
            print('X' * 50)
            f.close()
        print(output01, output02)

    except subprocess.TimeoutExpired as sub1:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub1)}')
    except subprocess.SubprocessError as sub2:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub2)}')

    except subprocess.SubprocessError as sub0:
        traceback.print_exc()
        print(f'{red} SUBPROCESS CALL ERROR {reset}\n{str(sub0)}')


def interface_info():
    print(f'{yellow}**Checking NIC Info {reset}')
    with open("NIC_INFO.txt", 'a') as f:
        output = subprocess.run(["sudo", "nmcli", "SSID,BSSID,DEVICE", "dev", "wifi"], stdin=f,
                                text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pprint.pprint(output)
        f.close()


def nic_status():
    time.sleep(2)
    print('X' * 50)

    print(f'{yellow} Checking General Status {reset}')
    with open("NIC_INFO.txt", 'a') as f:
        output = subprocess.run(["sudo", "nmcli", "general" "status"], stdin=f,
                                text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output)
        f.close()
    # output full tree to .XML / do not read to terminal
    subprocess.run(["sudo", "lshw", "-C", "network" "-xml"])  # capture_output=True, text=True, check=True)
    time.sleep(2)
    print('X' * 50)


def check_usbStatus():
    time.sleep(2)
    print('X' * 50)
    print(f'{yellow}**Checking Radio Status {reset}')
    with open("NIC_INFO.txt", 'a') as f:
        output01 = subprocess.run(["sudo", "lsusb"], stdin=f, text=True, check=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        print(output01)
        output02 = subprocess.run(["sudo", "lspci"], stdin=f, text=True, check=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        print(output02)
        f.close()
        time.sleep(2)
        print('X' * 50)


def radio_status():
    time.sleep(2)
    print('X' * 50)
    print(f'{yellow}**Checking Radio Status {reset}')
    with open("NIC_INFO.txt", 'a') as f:
        output = subprocess.run(["sudo", "nmcli", "radio", "all"], stdin=f, text=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(output)
        f.close()
        time.sleep(2)
        print('X' * 50)
    if f:
        return f'{yellow}**Sucessfully Parsed Radio Status{reset}'
    else:
        return f'{red}**Did not parse Radio Status Successfully {reset}'


def get_nic_permissions():
    time.sleep(2)
    print('X' * 50)
    print(f'{yellow} Reading NIC PERMISSIONS {reset}')
    with open("NIC_INFO.txt", 'a') as f:
        output = subprocess.run(["sudo", "nmcli", "general", "permissions"], stdin=f, text=True, check=True,
                                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(output)
        f.close()
    time.sleep(2)
    print('X' * 50)
    if f:
        return f'{yellow}**Sucessfully Parsed NIC Permissions {reset}'
    else:
        return f'{red}**Did not parse Radio Permissions Successfully {reset}'


def find_signals():
    print('X' * 50)
    print(f'{yellow}  Listening for  current  ESSID/AP Status {reset}')
    print(f'{yellow} Finding A Signal {reset}')
    time.sleep(7)
    print('X' * 50)
    with open("AVAIL_SIGNALS.txt", 'a') as f:
        print('X' * 50)
        output01 = subprocess.Popen(["sudo", "iwlist", "wlo1", "scan", "grep" "ESSID"], stdin=f, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        print(f'{yellow} List of available networks {reset}')
        print(output01)
        time.sleep(2)
        print('X' * 50)

        output02 = subprocess.Popen(["sudo", "iwlist", "wlx0013eff5483f", "scan", "grep" "ESSID"], stdin=f,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f'{yellow} List of available networks {reset}')
        print(output02)
        time.sleep(2)
        print('X' * 50)

        output03 = subprocess.Popen(["sudo", "iwlist", "wlan0", "scan", "grep" "ESSID"], stdin=f,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)
        print('X' * 50)
        print(f'{yellow} List of available networks {reset}')
        print(output03)
        time.sleep(2)
        print('X' * 50)
        f.close()
        if f:
            return f'{yellow}**Sucessfully Parsed [FIND-SIGNALS]  {reset}'
        else:
            return f'{red}**Did not parse [FIND-SIGNALS] Successfully {reset}'




def main():
    available_nics()
    interface_info()
    check_usbStatus()
    radio_status()
    get_nic_permissions()
    find_signals()


if __name__ == '__main__':
    main()

