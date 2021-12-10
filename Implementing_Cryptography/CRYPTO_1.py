from cryptography.fernet import Fernet


print('LLAVE 1')
key1 = Fernet.generate_key()
print(key1)
print('LLAVE 2')
key2 = Fernet.generate_key()
print(key2)


print('PRUEBA 1.1')
f1= Fernet(key1)
token= f1.encrypt(b"A really secret message")
print(token)
f1.decrypt(token)
print(f1.decrypt(token))
print('PRUEBA 1.2')
f1= Fernet(key1)
token= f1.encrypt(b"A really secret message")
print(token)
f1.decrypt(token)
print(f1.decrypt(token))

print('PRUEBA 2')
f2= Fernet(key2)
token2= f2.encrypt(b"A really secret message")
print(token2)
f2.decrypt(token2)
print(f2.decrypt(token2))




#cADA VEZ SE GENERA UNA LLAVE AL AZAR
#Una misma llave genera una hash diferente en l a misma palabra cada vez

