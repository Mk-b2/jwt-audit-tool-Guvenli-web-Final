import jwt

# Gizli anahtarımız çok zayıf bir şifre
SECRET_KEY = "123456"

payload = {
    "sub": "1234567890",
    "name": "Kerem",
    "admin": True
}

# Token'ı HS256 ile imzalıyoruz
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print("\n[+] Zayıf şifreli (123456) token üretildi:")
print(token)
print("\nBu token'ı araca kırmak için verin.\n")