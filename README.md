# 🔍 JWT Security Audit Tool (JWT Güvenlik Denetim Aracı)

Bu proje, JSON Web Token'ların (JWT) içerebileceği güvenlik zafiyetlerini tespit etmek ve analiz etmek amacıyla geliştirilmiş bir Siber Güvenlik aracıdır. Zayıf şifreleme algoritmaları, imza atlatma denemeleri ve hassas veri sızıntılarını otomatik olarak tarar. Hem komut satırından (CLI) hem de modern bir Web Arayüzünden (Web UI) kullanılabilir.

## 🚀 Özellikler (Audit Motoru)
* **Kritik Algoritma Tespiti:** `none` algoritması zafiyetini (Signature Bypass) yakalar.
* **Zayıf Anahtar (Secret) Kırma:** `HS256` token'lar için entegre wordlist ile Brute-Force saldırısı yapar.
* **Süre (Expiration) Kontrolü:** Sonsuza dek geçerli olan (süresiz) token'ları tespit eder.
* **Hassas Veri Sızıntısı:** Payload içinde unutulan şifre, kredi kartı vb. verileri tarar.
* **RS256 -> HS256 Uyarısı:** Asimetrik algoritmalarda yaşanabilecek "Algorithm Confusion" risklerini raporlar.

---

## 🛠️ Kurulum

Projeyi bilgisayarınıza indirdikten sonra, gerekli kütüphaneleri kurmak için terminalde proje dizinindeyken şu komutu çalıştırın:

```bash
pip install -r requirements.txt