# simple_ransomeware 
# File Encryption/Decryption Script
This is a simple Python script that allows you to encrypt and decrypt files using the cryptography library. It utilizes the Fernet symmetric encryption algorithm for file encryption and decryption.

Prerequisites
Python 3.x
cryptography library
Usage
Encryption
Place the files you want to encrypt in the same directory as the script.
Run the encrypt.py script.
The script will generate a new encryption key and save it in a file named thekey.key.
All files in the directory, except for encrypt.py, thekey.key, and decrypt.py, will be encrypted using the generated key.
The encrypted contents will replace the original file contents.
After the encryption process is completed, a message will be displayed: "All your files are encrypted."
Decryption
Place the encrypted files and the decrypt.py script in the same directory.
Run the decrypt.py script.
The script will check for the presence of the thekey.key file.
If the key file is found, the script will prompt you to enter a secret phrase.
If the correct secret phrase is entered, the encrypted files will be decrypted using the key stored in thekey.key.
The decrypted contents will replace the encrypted file contents.
After the decryption process is completed, a message will be displayed: "Congratulations! Your files have been decrypted."
If an incorrect secret phrase is entered, a message will be displayed: "Sorry! You wrote the wrong secret phrase."
Security Considerations
Keep the thekey.key file secure and do not share it with unauthorized individuals.
It is recommended to choose a strong and memorable secret phrase for decryption.
Contributing
Contributions to this script are welcome. If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

License
This project is licensed under the MIT License.
