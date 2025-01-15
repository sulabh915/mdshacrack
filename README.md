
# mdshacrack

mdshacrack is a Python-based tool designed to crack MD5,SHA1,SHA256,SHA514 hashes by comparing them against a user-provided wordlist. 
This utility is useful for security professionals and enthusiasts aiming to test the strength of MD5,SHA1,SHA256,SHA514 passwords.


## Features
MDSHAHash Cracking: 
Attempts to find the original string corresponding to a given MD5 hash by comparing it against entries in a wordlist.

User-Friendly Input: Prompts users to input the target MD5 hash and the path to their wordlist file.

Progress Indication: Displays each word from the wordlist as it's hashed and compared, providing insight into the cracking process.

Saved the all cracked password to file , program always check if the hash is already cracked.



## Requirements:
    1. Python 3.x: Ensure Python is installed on your system. You can download it from the official website.

    2. pwntools

    

## Installation

Here step by step guide.

```bash
git clone https://github.com/sulabhprajapati456/mdshacrack.git
cd mdshacrack
pip install -r requirement.txt
python3 mdshacrack.py -h
```
    
## Usage/Examples

```python
Usage : python3 -ht <hash_number> -h <hash> -w wordlists 
```

Example: 

```python
python3 mdshacrack.py -ht 4 -h 85361f099b282ab22a0d1c8b0d9da0b1e478accc5384aae73fba7a7099be5d35 -w /usr/share/wordlists/rockyou.txt
```
## Video guide

https://github.com/user-attachments/assets/73ba39c9-4c03-41b0-ba5a-db28b9cb032a

## Disclaimer
This tool is intended for educational purposes and authorized testing only. Unauthorized use against systems without explicit permission is illegal and unethical.
