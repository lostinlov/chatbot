from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

kdf = Scrypt(
    salt=b"salt_value",  # Salt değeri
    length=32,           # Anahtar uzunluğu
    n=2**14,             # İşlem gücü
    r=8,                 # Blok boyutu
    p=1,                 # Paralelizasyon
)
key = kdf.derive(b"password_value")  # Şifrelenecek parola
print(key)

