# python program to get current time,date?



import datetime
date = datetime.datetime.now()
print(date)

python program to create a text file with timestamp?

from datetime import datetime

date = datetime.now().strftime("%y_%m_%d-%I:%S:%M:%p")
print(f"Devops codes_{date}")


# python program to check if an URL is valid or not?


import validators

valid = validators.url('https://www.google.com/')

if valid == True:
    print(url is valid)
else:
    print(url is invalid)


# python program to validate an IP address?


def validate_ip(s):
    if s.count('.')!=3:
        return 'inavlid ip address'
        
    ip_list =list(map(str,s.split('.')))
    
    for elements in ip_list:
        if int(elements)<0 and len(elements)!=1:
            return 'Invald ip address'
    
    return "valid ip address"
    
print(validate_ip('225.1.2.2'))


import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
def check(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
 
    else:
        print("Invalid Email")
if __name__ == '__main__':
 
    email = "ankitrai326@gmail.com"
    
check(email)

# python program to find files having particular extension? (ex:  find ".txt" or ".exe" files in C:/Users/files/ directory)

import os
filename, file_extension = os.path.splitext('/path/to/somefile.ext')
print(filename)
print(file_extension)


# python program to copy odd lines of one file to another

fn = open('Devops codes.txt',  'r')
fn1 = open('nfile.txt', 'w')
cont=fn.readlines()
type(cont)
for i in range (0,len(cont)):
    if i % 2 != 0:
        fn1.write(cont[i])

    else:
        pass
fn1.close()
fn1 = open('nfile.txt' , 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()

#   python program to list a files from directory
   
import os
path = "raju@raju//desktop/"
dir_list = os.dir_list(path)
print("files and directories in '",path,"' :")
print(dir_list)
 
 
 
#  python program to merge two files into third file

   
data = data1=""

with open ('file1.txt') as fp:
    data = fp.read()
    
with open ('file2.txt')as fp:
    data1 = fp.read()
    
data += "/n"
data+= "data1"

with open ('file3.txt' ,'w')as fp:
    fp.write(data)

#   python program to check file size

   
import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)
   
   
   
 
#   implement python program to get a file creation and modification date or time
  
    
  import datetime
import os


path = r"sample.txt"

# file modification timestamp of a file
m_time = os.path.getmtime(path)
# convert timestamp into DateTime object
dt_m = datetime.datetime.fromtimestamp(m_time)
print('Modified on:', dt_m)

# file creation timestamp in float
c_time = os.path.getctime(path)
# convert creation timestamp into DateTime object
dt_c = datetime.datetime.fromtimestamp(c_time)
print('Created on:', dt_c)
  
    
    
    # python program to find the largest file in a directory

    import glob
import os
dir_name = 'C:/Program Files/Java/jdk1.8.0_191/'
# Get list of files in a directory
list_of_files = filter( os.path.isfile,
                        glob.glob(  dir_name + '*') )
# Find the file with max size from the list of files
max_file = max( list_of_files,
                key =  lambda x: os.stat(x).st_size)
print('Max File: ', max_file)
print('Max File size in bytes: ', os.stat(max_file).st_size)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





