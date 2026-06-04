import json
import base64
import jwt

def decode_base64_url(data):
    padding = '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data + padding).decode('utf-8')

def analyze_token_web(token, wordlist_path=None):
    out = []
    out.append("[*] JWT Analizi Başlıyor...\n" + "-"*50)
    
    parts = token.split('.')
    if len(parts) != 3:
        return "[!] Hata: Geçersiz JWT formatı. Lütfen 3 parçalı bir token girin."

    header_b64, payload_b64, signature_b64 = parts

    try:
        header = json.loads(decode_base64_url(header_b64))
        payload = json.loads(decode_base64_url(payload_b64))
        
        out.append("[+] Header:")
        out.append(json.dumps(header, indent=4))
        out.append("\n[+] Payload:")
        out.append(json.dumps(payload, indent=4))
        
        out.append("\n[*] Güvenlik Taraması Sonuçları:\n" + "-"*50)
        
        alg = header.get("alg", "").upper()
        if alg == "NONE":
            out.append("[!] KRİTİK: 'none' algoritması tespit edildi! İmza atlatılabilir.")
        elif alg == "HS256":
            out.append("[!] UYARI: 'HS256' kullanılıyor. Zayıf secret riski.")
        elif alg == "RS256":
            out.append("[i] BİLGİ: 'RS256' algoritması tespit edildi. RS256 -> HS256 atlatması test edilmelidir!")

        if "exp" not in payload:
            out.append("[!] YÜKSEK: 'exp' (son kullanma tarihi) değeri yok!")

        sensitive_keys = ["password", "pass", "credit_card", "ssn", "secret"]
        for key in payload.keys():
            if key.lower() in sensitive_keys:
                out.append(f"[!] ORTA: Payload içinde hassas veri bulundu: '{key}'")
        
        out.append("-" * 50)

        if alg == "HS256" and wordlist_path:
            out.append("\n[*] Kaba Kuvvet (Brute-Force) Saldırısı Başlıyor...")
            try:
                with open(wordlist_path, 'r', encoding='utf-8') as f:
                    passwords = f.read().splitlines()
                
                found = False
                for password in passwords:
                    try:
                        jwt.decode(token, password, algorithms=["HS256"])
                        out.append(f"[+] BAŞARILI! Zayıf secret kırıldı: '{password}'")
                        found = True
                        break
                    except jwt.ExpiredSignatureError:
                        out.append(f"[+] BAŞARILI! Zayıf secret kırıldı: '{password}' (Süresi dolmuş)")
                        found = True
                        break
                    except jwt.InvalidTokenError:
                        continue
                if not found:
                    out.append("[-] Başarısız. Wordlist içindeki hiçbir şifre eşleşmedi.")
            except Exception as e:
                out.append(f"[!] Wordlist okunamadı: {e}")

    except Exception as e:
        out.append(f"[!] Hata oluştu: {e}")

    return "\n".join(out)