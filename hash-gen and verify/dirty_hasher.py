import hashlib, os, sys, time

'''
Need to set up two static methods for file detection. 
1. scandir + hash for same filenames 
2. glob/**/glob for simular file names / structure. 

## MAKE SURE FILE PATH AS BINARY IS BEING PASSED. DO NOT HASH THE FILENAME/STR. HASH THE BINARY OBJECT. 

'''


## sample code ## 
    def scanDirs00(self, file_name):
        print("Files and Directories in '% s':" % self.vid_loc)
        # glob.isglob to find all files recursivly
        global file_names
        file_counter = 0
        ## try both isfile() and exists ##
        for root, dirs, files in tqdm(os.walk(p), followlinks=True):
            if file_name in files and file_name.isfile(p):
                file_names = [os.path.join(root, f) for f in files]
                print(
                    f' ** Found {yellow} [{file_counter}] {reset} files with the name {yellow} [{file_name}] {reset} ** \n {red}{files}{reset}')
                print(f'{file_names}')
                for entry in dirs:
                    if entry.is_dir()
                        print('DIR FOUND', entry.name)
                    elif entry.is_file():
                        print('DIR FOUND', entry.name)
            file_counter += 1
            return file_names

    def scanDirs01(self, file_name):
            file_list = []
            with os.scandir(path) as ls:
                for item in ls:
                    if item.is_file():
                        filename = str(item.name)
                        if ext == '':
                            file_list.append(filename)
                            interrogative = "Select a file: "
                        elif filename.endswith(ext):
                            file_list.append(filename)
                            interrogative = "Select " + ext + " file: "
            i = 1
            for file in file_list:
                print("[" + str(i) + "] " + file)
                i += 1
            selected = validate_selection(interrogative, file_list)
            return selected

        ### EOsample Code ###

class hashVerify():
    def __init__(self):
        self.hash_list = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
        self.md5 = hashlib.md5()
        self.sha1 = hashlib.sha1()
        self.sha224 = hashlib.sha224()
        self.sha256 = hashlib.sha256()
        self.sha384 = hashlib.sha384()
        self.sha512 = hashlib.sha512()
        print(f'[+] Enter the dir for hash verification \n\t\t [+]**[CURRENT-DIR] {os.getcwd()}')
        self.path = input(r'') ## cha
        self.path = b'self.path'
        
        print(f'[+] Enter the hash  ')
        self.hash_toVerify = input('')
        # self.hash_toVerify = hashlib.encode(self.hash_toVerify)
        # self.path.hash_toVerify(self.hash_toVerify)
        # self.hash_toVerify=self.hash_toVerify.encode()
        self.hash_toVerify = str.encode(self.hash_toVerify)

    @staticmethod
    def scan_duplicates(self, p, file_name):
        print('[+] Enter the Directory to scan: ')
        global duplicates
        file_counter = 0
        ## try both isfile() and exists ##
        for root, dirs, files in tqdm(os.walk(p), followlinks=True):
            if file_name in files and file_name.isfile(p):
                duplicates = [os.path.join(root, f) for f in files]
                print(
                    f' ** Found {yellow} [{file_counter}] {reset} files with the name {yellow} [{file_name}] {reset} ** \n {red}{files}{reset}')
                print(f'{duplicates}')
            file_counter += 1
            return duplicates

    def verify_hash(self):
        print(f'[+] [Verifying -- byte format] :: \n \t\t[+]**[{self.hash_toVerify}]')
        print(f'\n{"X" * 50} [+] List of Hashes to be Verified: \n \t\t[+]**[{self.hash_list}]')
        with open(self.path, 'rb') as f:
            toVerify = f.read()
            print(f'[+] Verifying :: \n \t\t[{toVerify}]')
            for hash_obj in self.hash_list:
                print(f'Make sure filepath name is being passed as binary. DO NOT HASH STRING, HASH THE ACTUAL FILE.) 
                
                      print(f'Currenlty Hashing, [{hash_obj}]
                hash0 = getattr(hashlib, hash_obj)
                m = hashlib.new(hash_obj)
                m.update(self.path)
                print('X' * 50)
                print(f'[+] --- [ITERATING] --- [+] ')
                print(f'[+] [OLD HASHES]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.hexdigest()}]')
                print(f'[+] [OLD HASHE]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.digest()}]')
                print(f'[+] [OLD HASH-SIZE]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.digest_size}]')
                print(f'[+] [OLD BLOCK-SIZE]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.block_size}]')
                print('X' * 50)
                
                hashlib.md5(open('filename.exe','rb').read()).hexdigest()
'd41d8cd98f00b204e9800998ecf8427e'

                self.hash_toVerify = m.new(hash_obj)
                # hash_obj.update(toVerify)
                print(f'[+] Hashed Object: \n [{toVerify}] \n \t\t[{m.name}] :: [{m.hexidigest()}]')
                
                m.new(open('/insert/path/to/file/filename.exe','rb').read()).hexdigest()

                if m.hexidigest() == self.hash_toVerify:
                    print('X' * 50)
                    print(f'[+] Matching Hashes Detected \n {self.toVerify}\n\t{m.name}\t\t{m.hexidigest()}')
                    print(f'[+] Matching Hashes Detected \n {self.toVerify}\n\t{m.name}\t\t{m.digest()}')
                    print('X' * 50)
                    break


class makeHash():
    def __init__(self):
        self.hash_list = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
        self.md5 = hashlib.md5()
        self.sha1 = hashlib.sha1()
        self.sha224 = hashlib.sha224()
        self.sha256 = hashlib.sha256()
        self.sha384 = hashlib.sha384()
        self.sha512 = hashlib.sha512()
        print(f'[+] Enter the dir for hash verification ')
        self.path = input(r'')
        # self.path = self.path.encode()

        self.path = str.encode(self.path)

    #  self.h = getattr(hashlib, self.path)

    def create_hash(self):
        print(f'[+] Creating Hashes :: \n \t\t[{self.path}]')
        print(f'\n{"X" * 50} [+] List of Hashes to be created: \n \t\t[+]**[{self.hash_list}]')
        with open(self.path, 'rb') as f:
            content = f.read() ## converrdata 
            print(type(content) # remove later 
            print(content) # remove later
            for hash_obj in self.hash_list:
                hash0 = getattr(hashlib, hash_obj)  ## create object
                m = hashlib.new(hash_obj)
                m.update(self.path)
                print(m)
                print('[+] hash_obj:', hash_obj)
                print('[+] Hash_loc', hash0)
                assert isinstance(hash0(self.path).hexdigest, object)
                print('X' * 50)
                print(f'[+] [NEW HASHES]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.hexdigest()}]')
                print(f'[+] [NEW HASHES]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.digest()}]')
                print(f'[+] [NEW HASH-SIZE]: \n \t\t[{m.name}] :: [{m.digest_size}]')
                print(f'[+] [NEW BLOCK-SIZE]: \n \t\t[{m.name}] :: [{m.block_size}]')
                print('X' * 50)
                            
                ''' create new obj for b(content), see if hash-values match ^'''          
                m.update(content)
                print('[+] hash_obj:', hash_obj)
                print('[+] Hash_loc', hash0)
                assert isinstance(hash0(self.path).hexdigest, object)
                print('X' * 50)
                print(f'[+] [NEW HASHES]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.hexdigest()}]')
                print(f'[+] [NEW HASHES]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.digest()}]')
                print(f'[+] [NEW HASH-SIZE]: \n \t\t[{m.name}] :: [{m.digest_size}]')
                print(f'[+] [NEW BLOCK-SIZE]: \n \t\t[{m.name}] :: [{m.block_size}]')
                print('X' * 50)

def main():
    verify = hashVerify()
    create = makeHash()
    verifyq = ["verify", "Verify", "V", "v", "ver"]
    createq = ["create", "Create", "C", "c", "crea"]
    print(f'[+] :: [DIRTY HASHER] :: \n \t\t[{time.ctime()}]')
    print(f'[+] Verify or Create Hash? ')
    ans = input('**')
    if ans in verifyq:
        print(f'[+] -- [Initiating Verification Process] -- ')
        verify.verify_hash()

    elif ans in createq:
        print(f'[+] -- [Initiating Hash Creation Process] -- ')
        create.create_hash()


if __name__ == '__main__':
    main()







             # print(hash0.name)
            # print(hash0.hexidigest())
            #   hash_obj = str.encode(hash_obj)
            #  print(f'[+] [NEW HASHES]: \t\t[{hash0}] :: ')
            #  print(f'[+] [NEW HASHES]: \n [{path}] \n \t\t[{hash_obj.name}] :: [{hash_obj.hexidigest()}]')
            #  print(f'[+] [NEW HASHES]: \n [{path}] \n \t\t[{hash_obj.name}] :: [{hash_obj.digest()}]')
            # hash0.update(content)
# h = getattr(hashlib, finalHash)

