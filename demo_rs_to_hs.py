import base64
import json

# Header'da algoritma RS256 olarak ayarlanıyor
header = {"alg": "RS256", "typ": "JWT"}
payload = {
    "sub": "admin_user",
    "name": "Kerem",
    "admin": True
}

def encode_b64(data):
    json_data = json.dumps(data).encode('utf-8')
    return base64.urlsafe_b64encode(json_data).decode('utf-8').rstrip('=')

# Sahte bir asimetrik imza ekliyoruz
token = f"{encode_b64(header)}.{encode_b64(payload)}.sahte_rsa_imzasi_demo_amacli"

print("\n[+] 'RS256' Algoritmalı Token Üretildi:")
print(token)
print("\nBu token'ı araca analiz ettirin.\n")