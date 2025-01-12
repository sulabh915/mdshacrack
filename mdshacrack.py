#python3 filename -ht <sha256num> -h adfsfsdfl -w wordlists
#md5sumhex,sha1sumhex,sha224sumhex,sha256sumhex,sha384sumhex,sha512sumhex
from pwn import *
import sys
import os


def Cracking(hash,wordlist,hash_type):
            """this will crack only md5 hash"""

            if os.path.isfile('./pwnfile.txt'):
                with open('pwnfile.txt','r') as file:
                    lines = file.readlines()

                    for line in lines:
                        index = line.find(hash)
                        if index != -1:
                            print(f"password is already cracked {line.strip()}")
                            exit()

            attempts = 0
            with log.progress(f"Attempting to crack {hash}\n\r") as p:
                with open(wordlist,'r',encoding='latin-1') as passwd:
                    for password in passwd:
                        password = password.strip('\n').encode('latin-1')

                        if int(hash_type) == 1 and len(hash) == 32:
                            what_hash = " MD5 "
                            password_hash  = md5sumhex(password)

                        elif int(hash_type) == 2 and len(hash) == 40:
                            what_hash = " SHA1 "
                            password_hash = sha1sumhex(password)
                        
                        elif int(hash_type) == 3 and len(hash) == 56:
                            what_hash = " SHA224 "
                            password_hash = sha224sumhex(password)
                        
                        elif int(hash_type) == 4 and len(hash) == 64:
                            what_hash = " SHA256 "
                            password_hash = sha256sumhex(password)
                        
                        elif int(hash_type) == 5 and len(hash) == 96:
                            what_hash = " SHA384 "
                            password_hash = sha384sumhex(password)

                        elif int(hash_type) == 6 and len(hash) == 128:
                            what_hash = " SHA512 "
                            password_hash = sha512sumhex(password)
                        
                        else:
                            print(f"\nselect following number of hash type , your hash length is {len(hash)} invalid")
                            help()

                        
                        
                        p.status(f"attempt:{attempts} Cracking...  given{what_hash}hash")
                        if password_hash == hash:
                            p.success(f"Attemps:{attempts} Cracked : {password_hash}:{password.decode('latin-1 ')}")
                            with open('pwnfile.txt','a') as w:
                                w.write(f'{password_hash}:{password.decode('latin-1')}\n')
                            exit()
                        attempts += 1
                    p.failure("password hash not found")
        

def help():

            """Documentation of given script"""

            print(">> Usage : python3 -ht <hash_number> -h <hash> -w wordlists\nMD5    : 1\nSHA1   : 2\nSHA224 : 3\nSHA256 : 4\nSHA384 : 5\nSHA512 : 6")
            exit()
    


def main():
            """main program to executed"""

            #program proper input validation 
            if len(sys.argv) != 7 or sys.argv[1] == '--help' or sys.argv[1] == '-h':
                            help()
            
            arguement_list = (sys.argv[0],'-ht','-h','-w',sys.argv[2],sys.argv[4],sys.argv[6])

            for arg in range(0,len(arguement_list),):
                    if sys.argv[arg] in arguement_list:
                        pass
                    else:
                        print('invalid arugment')
                        help()
            
            
            
            provided_hash = sys.argv[4]
            wordlist = sys.argv[6]
            

            if not os.path.isfile(wordlist):
                        print('invalid wordlits path')
                        exit()
            
            hash_type = sys.argv[2] 
            Cracking(provided_hash,wordlist,hash_type)
            
            


if __name__ == "__main__":
    main()
