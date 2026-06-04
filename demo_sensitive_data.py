import jwt

# Geliştirici hatası: Şifre ve kredi kartı bilgisi payload içine konulmuş!
payload = {
    "sub": "1001",
    "name": "Kerem",
    "role": "user",
    "password": "MySuperSecretPassword123!",
    "credit_card": "4532-1111-2222-3333"
}

# Token normal bir şekilde şifreleniyor
token = jwt.encode(payload, "guvenli_bir_anahtar_olsa_bile_farketmez", algorithm="HS256")

print("\n[+] İçinde hassas veriler barındıran zafiyetli token üretildi:")
print(token)
print("\nBu token'ı araca analiz ettirin.\n")