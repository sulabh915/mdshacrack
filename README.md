**mdshacrack is a Python-based tool designed to crack MD5,SHA1,SHA256,SHA514 hashes by comparing them against a user-provided wordlist. 
**This utility is useful for security professionals and enthusiasts aiming to test the strength of MD5,SHA1,SHA256,SHA514 passwords.

Features
MDSHAHash Cracking: Attempts to find the original string corresponding to a given MD5 hash by comparing it against entries in a wordlist.
User-Friendly Input: Prompts users to input the target MD5 hash and the path to their wordlist file.
Progress Indication: Displays each word from the wordlist as it's hashed and compared, providing insight into the cracking process.
Saved the all cracked password to file , program always check if the hash is already cracked.

Requirements
Python 3.x: Ensure Python is installed on your system. You can download it from the official website.
pwntools

Installation
Clone the Repository:
git clone https://github.com/sulabhprajapati456/mdshacrack.git

Navigate to the Project Directory:
cd mdshacrack
Install Dependencies: The script uses the hashlib library, which is included in Python's standard library. No additional packages are required.

Usage
Run the Script:

>> Usage : python3 -ht <hash_number> -h <hash> -w wordlists
MD5    : 1
SHA1   : 2
SHA224 : 3
SHA256 : 4
SHA384 : 5
SHA512 : 6


Example:
python3 mdshacrack.py -ht 4 -h 85361f099b282ab22a0d1c8b0d9da0b1e478accc5384aae73fba7a7099be5d35 -w /usr/share/wordlists/rockyou.txt


If the password is found in the wordlist, the script will output:
[+] Attempting to crack 85361f099b282ab22a0d1c8b0d9da0b1e478accc5384aae73fba7a7099be5d35
    
    : Attemps:109999 Cracked : 85361f099b282ab22a0d1c8b0d9da0b1e478accc5384aae73fba7a7099be5d35:romeo5

Wordlist
A wordlist is a text file containing potential passwords, each on a new line. You can create your own or use existing wordlists available online, such as those from the SecLists repository.

Disclaimer
This tool is intended for educational purposes and authorized testing only. Unauthorized use against systems without explicit permission is illegal and unethical.
