import hashlib, os, sys, time
import base64

class hashVerify():
    def __init__(self):
        self.hash_list = ["md5","sha1","sha224", "sha256", "sha384", "sha512"]
        self.md5 = hashlib.md5()
        self.sha1 = hashlib.sha1()
        self.sha224 = hashlib.sha224()
        self.sha256 = hashlib.sha256()
        self.sha384 = hashlib.sha384()
        self.sha512 = hashlib.sha512()
        print(f'[+] Enter the dir for hash verification \n\t\t [+]**[CURRENT-DIR] {os.getcwd()}')
        self.path = input(r'')
        print(f'[+] Enter the hash  ')
        self.hash_toVerify = input('')
        #self.hash_toVerify = hashlib.encode(self.hash_toVerify)
        #self.path.hash_toVerify(self.hash_toVerify)
        #self.hash_toVerify=self.hash_toVerify.encode()
        self.hash_toVerify = str.encode(self.hash_toVerify)

    def __enter__(self):
        return f'[+] [Context Manager Called] [+]\n{self}'
       # print(f'[+] {yellow}[is assigned to %r\n{reset}' % open)
        #self.f = open(self.text_loc, self.mode)
        #return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'[-] [EXIT-METHOD CALLED] \n [EXC_TYPE] \n{exc_value} \n\n[-] [exc_value]\n\n[-] [TRACEBACK-ERROR] \n[{traceback.format_exc} [-]]')
    def __iter__(self):
        return f'[+] [+ Generator Called ] [+]{self}'
    def __next__(self):
        if self.list_count <= self.text_len:
            try:
                item = self.lst[self.idx]
            except IndexError:
                raise StopIteration()
            self.idx += 1
            return item

    def verify_hash(self):
        print('\n', 'X' * 50)
        print(f'[+] [Verifying -- byte format] :: \n \t\t[+]**[{self.hash_toVerify}]')
        print(f'\n{"X"*50} [+] List of Hashes to be Verified: \n \t\t[+]**[{self.hash_list}]\n\n')
        print(f'[+] {yellow}[CONTEXT-MANAGER LOCATION] %r\n{reset}' % open)
        print('X' * 50, '\n')

        print(f'[+] {yellow} is assigned to %r\n{reset}' % open)
        with open(self.path, 'rb') as f:
            toVerify = f.read()
            print(f'[+] Verifying :: \n \t\t[{toVerify}]')
            for hash_obj in self.hash_list:
                hash0 = getattr(hashlib, hash_obj)
                m = hashlib.new(hash_obj)
                m.update(self.path)
                print('X'*50)
                print(f'[+] --- [ITERATING] --- [+] ')
                print(f'[+] [OLD HASHES]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.hexdigest()}]')
                print(f'[+] [OLD HASHE]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.digest()}]')
                print(f'[+] [OLD HASH-SIZE]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.digest_size}]')
                print(f'[+] [OLD BLOCK-SIZE]: \n [{self.path}] \n \t\t[{m.name}] :: [{m.block_size}]')
                print('X'*50)

                self.hash_toVerify = m.new(hash_obj)
                #hash_obj.update(toVerify)
                print(f'[+] Hashed Object: \n [{toVerify}] \n \t\t[{m.name}] :: [{m.hexidigest()}]')

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
        #self.path = self.path.encode()

        self.path = str.encode(self.path)

    #  self.h = getattr(hashlib, self.path)


    def create_hash(self):
        print(f'[+] Creating Hashes :: \n \t\t[{self.path}]')
        print(f'\n{"X"*50} [+] List of Hashes to be created: \n \t\t[+]**[{self.hash_list}]')
        print(f'[+] {yellow} is assigned to %r\n{reset}' % open)
        with open(self.path, 'rb') as f:
            content = f.read()
            for hash_obj in self.hash_list:
                hash0 = getattr(hashlib, hash_obj) ## create object
                self.m = hashlib.new(hash_obj)
                self.m.update(self.path)
                print(m)
                print('[+] hash_obj:', hash_obj)
                print('[+] Hash_loc', hash0)
                assert isinstance(hash0(self.path).hexdigest, object)
                print('X'*50)
                print(f'[+] [NEW HASHES]: \n [{self.path}] \n \t\t[{self.m.name}] :: [{self.m.hexdigest()}]')
                print(f'[+] [NEW HASHES]: \n [{self.path}] \n \t\t[{self.m.name}] :: [{self.m.digest()}]')
                print(f'[+] [NEW HASH-SIZE]: \n \t\t[{m.name}] :: [{m.digest_size}]')
                print(f'[+] [NEW BLOCK-SIZE]: \n \t\t[{m.name}] :: [{m.block_size}]')
                print('X' * 50)

                if self.path.hexdigest:
                    print(f'[+] Creating Hashes :: \n \t\t[{self.path}]')
                    encoded_64 = make_base64(self.m.hex_digest())
                    encodedHex_64 = make_base64(self.m.digesat())


                global fake_return
                fake_return = []
                #return encoded_64, encodedHex_64

                # return fake_return
                def make_base64(make, **kwargs):
                    time.sleep(.5)
                    print('X' * 50)
                    if make is None or make == '':
                        print(f'[+] ARGS passed [NONE-TYPE] -- Parsing kwargs ')
                        to_encode = base64.b64encode(make)
                        print(f'[+] [ENCODING] -- [{to_encode}] -- [{self.m.hexdigest()}]')
                        print(f'[+] [ENCODING]: \n [{self.path}] \n \t\t[{self.m.name}] :: [{self.m.hexdigest()}]')
                        print(f'[+] [ENCODING]: \n [{self.path}] \n \t\t[{self.m.name}] :: [{self.m.digest()}]')
                        print(f'[+] [ENCODING]: \n \t\t[{self.path}] :: [{m.digest_size}] :: [{self.m.digest()}]')
                        print(f'[+] [ENCODING]: \n \t\t[{self.path}] :: [{m.block_size}] :: [{self.m.digest()}]')
                        eval(compile(base64.b64decode(myscript), '<string>', 'exec'))
                        return to_encode, b64_encoded

                    elif kwargs:
                        to_encode = base64.b64encode(make)
                        b64_encoded = eval(compile(base64.b64decode(myscript), '<string>', 'exec'))
                        return to_encode, b64_encoded

                    else:
                        to_encode = f'[-] [ERROR] -- [{self.path}] -- [{self.m.hexdigest()}]'
                        b64_encoded = f'[-] [ERROR] -- [{self.path}] -- [{self.m.hexdigest()}]'


                    print('X' * 50)
                    return to_encode, b64_encoded

    ## to decode b64
    @staticmethod
    def debase64(*args):
        f = open('myscript.py')
        encoded = base64.b64encode(*args)




        myscript = """IyBUaGlzIGlzIGEgc2FtcGxlIFB5d
                      GhvbiBzY3JpcHQKcHJpbnQgIkhlbG
                      xvIiwKcHJpbnQgIldvcmxkISIK"""

        eval(compile(base64.b64decode(myscript), '<string>', 'exec'))


#class MakeBases():



        #print(hash0.name)
               # print(hash0.hexidigest())
               #   hash_obj = str.encode(hash_obj)
               #  print(f'[+] [NEW HASHES]: \t\t[{hash0}] :: ')
               #  print(f'[+] [NEW HASHES]: \n [{path}] \n \t\t[{hash_obj.name}] :: [{hash_obj.hexidigest()}]')
               #  print(f'[+] [NEW HASHES]: \n [{path}] \n \t\t[{hash_obj.name}] :: [{hash_obj.digest()}]')
               # hash0.update(content)
    #h = getattr(hashlib, finalHash)

def main():
    verify = hashVerify()
    create = makeHash()
    verifyq = ["verify","Verify","V","v","ver"]
    createq = ["create","Create","C","c","crea"]
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


