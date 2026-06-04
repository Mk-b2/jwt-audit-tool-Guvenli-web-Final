import jwt

# Geliştirici hatası: Payload içine 'exp' (son kullanma tarihi) eklenmemiş.
# Bu token ele geçirilirse, sonsuza dek kullanılabilir.
payload = {
    "sub": "1234567890",
    "name": "Kerem",
    "role": "user"
}

# Token oluşturuluyor
token = jwt.encode(payload, "super_gizli_anahtar", algorithm="HS256")

print("\n[+] Süresiz (Sonsuza dek geçerli) zafiyetli token üretildi:")
print(token)
print("\nBu token'ı araca analiz ettirin.\n")