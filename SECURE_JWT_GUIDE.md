# 🛡️ Güvenli JWT (JSON Web Token) Uygulama Rehberi

Modern web uygulamalarında JWT kullanımı yaygındır ancak yanlış yapılandırıldığında kritik güvenlik açıklarına yol açabilir. Aşağıdaki kurallar, JWT tabanlı kimlik doğrulama sistemlerini güvenli hale getirmek için uygulanmalıdır.

## 1. Güçlü Algoritmalar Kullanın
* Asla `none` algoritmasını kabul etmeyin. Sunucu tarafında `alg` başlığını mutlaka doğrulayın.
* Mümkünse simetrik şifreleme (`HS256`) yerine, asimetrik şifreleme (`RS256` veya `ES256`) kullanın. Bu sayede imza oluşturma (Private Key) ve doğrulama (Public Key) birbirinden ayrılır.

## 2. Anahtar (Secret) Güvenliği
* `HS256` kullanıyorsanız, gizli anahtarınız (Secret Key) tahmin edilemez, rastgele oluşturulmuş ve **en az 32 byte (256 bit)** uzunluğunda olmalıdır.
* Anahtarları asla kaynak kodun içine (hardcoded) yazmayın. Çevresel değişkenler (.env) veya güvenli kasa (Vault) sistemleri kullanın.

## 3. Token Süresi (Expiration) ve İptal Mekanizmaları
* Her JWT'nin mutlaka bir `exp` (Expiration Time - Son Kullanma Tarihi) değeri olmalıdır.
* Access Token (Erişim Jetonu) ömrünü kısa tutun (örn: 15-30 dakika).
* Oturum kapatma veya hesap silme işlemleri için "Token Blacklist" (Kara Liste) mekanizması kurun.

## 4. Hassas Veri Barındırmayın
* JWT'nin payload kısmı şifrelenmez (sadece Base64 ile kodlanır). Herhangi biri bu içeriği okuyabilir.
* Token içine **asla** şifre, kredi kartı bilgisi, T.C. Kimlik Numarası gibi hassas veriler koymayın. Sadece kullanıcıyı tanımlayacak minimal veriler (User ID, Role vb.) ekleyin.

## 5. 'Algorithm Confusion' Zafiyetini Önleyin
* Kullandığınız kütüphanenin, token'ı doğrularken algoritmayı Header'dan otomatik okumasına izin vermeyin. Doğrulama fonksiyonunda beklenen algoritmayı *kesin olarak* belirtin. (örn: `jwt.decode(token, key, algorithms=["RS256"])`).