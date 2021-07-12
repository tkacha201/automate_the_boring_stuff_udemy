import os
arr = os.listdir('C:\\Users\\teodosi.kachakov\\Desktop\\automateTheBoringStuff')
for file in arr:
    if file.startswith('error'):
        os.remove((os.path.join("C:\\Users\\teodosi.kachakov\\Desktop\\automateTheBoringStuff\\", file)))
        
