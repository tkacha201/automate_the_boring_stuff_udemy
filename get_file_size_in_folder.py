import os

total_size = 0
for filename in os.listdir('C:\\Users\\teodosi.kachakov\\Desktop\\info\\img'):
    if not os.path.isfile(os.path.join('C:\\Users\\teodosi.kachakov\\Desktop\\info\\img', filename)):
                          continue
    total_size = total_size + os.path.getsize(os.path.join('C:\\Users\\teodosi.kachakov\\Desktop\\info\\img', filename))
print(total_size)
