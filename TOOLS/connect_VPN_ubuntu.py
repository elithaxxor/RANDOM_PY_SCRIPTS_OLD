def connect_vpn():
    print('X' * 50)
    subprocess.run("auto_vpn.sh")
    subprocess.run(["sudo", "expressvpn", "connect"],text=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('X' * 50)
    

    connect_vpn()
    
