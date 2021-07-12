import send2trash
import shutil
import time
import os


source_dir = 'c:\\$Recycle.Bin\\s-1-5-21-329068152-1454471165-1417001333-9095294'
target_dir = 'c:\\users\teodosi.kachakov\\desktop\\test_bin_move'
send2trash.send2trash(r'c:\users\teodosi.kachakov\desktop\test_bin_move\dummy_file.txt')
print('hello?')
time.sleep(5.0)
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)
            
            
