DEBUG = False 

if(DEBUG):
    import os
    os.chdir(os.path.dirname(__file__))
    
    global input
    f = open("Sample.txt")
    input = lambda :f.readline().strip()