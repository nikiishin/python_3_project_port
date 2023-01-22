import pyAesCrypt

password = input('Введите пароль для файла')

# encrypt
# pyAesCrypt.encryptFile('Анна.txt', 'Анна.txt.aes', password)

pyAesCrypt.decryptFile('Анна.txt.aes', 'Анна_расшифр.txt', password)