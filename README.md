# 🐱 Cat Tools - Steganografi Analiz Aracı

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Stars](https://img.shields.io/github/stars/lilnecati/Stego)
![Contributors](https://img.shields.io/github/contributors/lilnecati/Stego)

<p align="center">
  <img src="https://raw.githubusercontent.com/lilnecati/Stego/main/banner2.png" alt="Cat Tools Banner" width="600">
</p>

> 🔍 CTF yarışmaları ve güvenlik testleri için geliştirilmiş, kapsamlı steganografi analiz aracı.

## 🌟 Özellikler

### 🖼️ Resim Analizi
- 📏 Boyut, format ve renk modu tespiti
- 🎨 Palette analizi
- 🔍 Detaylı görüntü özellikleri inceleme

### 🔐 LSB Steganografi
- 🕵️ Least Significant Bit analizi
- 📝 Gizli mesaj tespiti
- 🎯 Otomatik mesaj çıkarma

### 📋 Metadata Analizi
- 📊 EXIF veri analizi
- 🏷️ Gömülü metadata tespiti
- 📝 Detaylı metadata raporlama

### 🔤 String Extraction
- 📝 Yazdırılabilir karakter analizi
- 🔍 Gizli metin tespiti
- ⚡ Akıllı string filtreleme

### 🔎 Magic Bytes
- 📁 Dosya türü tespiti
- 🔍 MIME türü analizi
- 🔬 Hex header inceleme

## 🚀 Kurulum

### Sistem Gereksinimleri
- Python 3.8 veya üstü
- 64-bit işletim sistemi
- 2GB RAM (önerilen)

### 📥 Adımlar

1. Repoyu klonlayın:
   ```bash
   git clone https://github.com/lilnecati/Stego.git
   cd Stego
   ```

2. Sanal ortam oluşturun (önerilen):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Kullanım

```bash
python stego.py
```

### 🎮 Ana Menü
```
    /\___/\  
   (  o o  )  STEGO v1.0
   (  =^=  ) 
    (--m--)  
    
[ Cat Tools ]

[*] Ana Menü:
1) Resim Analizi
2) LSB Steganografi
3) Metadata Analizi
4) String Extraction
5) Magic Bytes Kontrolü
6) Çıkış
```

### 📋 Kullanım Örnekleri

#### 🖼️ Resim Analizi
```
[+] Resim Boyutu: (1920, 1080)
[+] Resim Formatı: PNG
[+] Renk Modu: RGB
[+] Palette: Yok
```

#### 🔐 LSB Analizi
```
[+] LSB ile gizlenmiş mesaj bulundu: "gizli_mesaj_123"
```

#### 📊 Metadata
```
[+] Metadata Bilgileri:
    EXIF DateTimeOriginal: 2024:03:15 12:30:00
    EXIF Make: Canon
    EXIF Model: EOS R5
```

## ⚠️ Önemli Not

Bu araç **sadece eğitim amaçlıdır** ve CTF yarışmaları için tasarlanmıştır.
- ❌ İzinsiz sistemlerde kullanmayın
- ❌ Kötü amaçlı kullanım yasaktır
- ✅ Sadece CTF ve eğitim amaçlı kullanın

## 👨‍💻 Geliştirici

Cat Tools - Stego, CTF yarışmacıları ve siber güvenlik araştırmacıları için geliştirilmiş açık kaynaklı bir projedir.

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

## 🤝 Katkıda Bulunma

1. Bu repoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin yeni-ozellik`)
5. Pull Request oluşturun

## 🌟 Yıldız Vermeyi Unutmayın!

Eğer bu proje CTF çözümlerinize yardımcı olduysa, ⭐️ vermeyi unutmayın! 