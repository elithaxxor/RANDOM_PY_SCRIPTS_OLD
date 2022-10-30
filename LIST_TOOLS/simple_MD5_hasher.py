def hashfile(*args, blocksize=65536):
    print('enter list or path') 
    path = input('')
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

hashfile()
          

  
