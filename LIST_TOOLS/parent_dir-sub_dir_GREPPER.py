import os, sys 

def getParentDirectoryFromFile(absolutePathToFile):
    splitResutsFromZeroToNMinus1 = absolutePathToFile.split(os.sep)[:-1]
    pprint.pprint(splitResutsFromZeroToNMinus1)
    return f'** {yellow}file found in {reset} \n {os.sep.join(splitResutsFromZeroToNMinus1)}'

  
    
def display_subdirs(absolutePathToFile):
    subdirs = [x for x in p.iterdir(absolutePathToFile) if x.is_dir()]
    subdirs.sort()
    pprint.pprint(subdirs)
    return subdirs

    
absolutePathToFile = os.getcwd()
parent_dir = getParentDirectoryFromFile(absolutePathToFile)
sudbdir = display_subdirs(absolutePathToFile)

print(parent_dir)
print(subdir) 

                    
