# Instagram Pending Requests Canceler

Cancel all your pending Instagram follow requests in bulk with human-like behavior to avoid detection.

## English

### Features

- Bulk cancel pending follow requests
- Human-like behavior with random delays and actions
- Progress tracking and detailed statistics
- Browser automation using existing Chrome session
- Safe operation with breaks to avoid rate limiting

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- Instagram account logged in Chrome

### Installation

1. Clone the repository
```bash
git clone https://github.com/mobilteknolojileri/instagram-pending-requests-canceler.git
cd instagram-pending-requests-canceler
```

2. Install required packages
```bash
pip install -r requirements.txt
playwright install chromium
```

### How to Get Your Instagram Data

1. Open Instagram on web browser
2. Go to **Settings** → **Accounts Center**
3. Select **Your information and permissions**
4. Click on **Download your information** 
5. Select your Instagram account
6. Choose **Download or transfer information** → **Some of your information**
7. Select **Followers, following and follow requests**
8. Set date range to **All time**
9. Format: **JSON**
10. Submit request and wait for download link

After downloading and extracting, you'll find your data in a folder structure like:
```
instagram-username-2025-10-23-xxeadawdvb/
└── connections/
    └── followers_and_following/
        └── pending_follow_requests.json
```

### Usage

1. Get your Chrome user agent from [https://iplogger.org/useragents/](https://iplogger.org/useragents/)

2. Update `launch_chrome.bat` with your user agent:
```batch
--user-agent="YOUR_USER_AGENT_HERE"
```

3. Launch Chrome in debug mode:
```bash
launch_chrome.bat
```

4. Login to Instagram in the opened Chrome window

5. Run the script:
```bash
python cancel_requests.py
```

6. Enter the path to your `pending_follow_requests.json` file when prompted

### How It Works

The script performs the following actions for each pending request:
1. Navigates to user profile
2. Clicks "Requested" button
3. Selects "Unfollow" option
4. Implements random delays between actions
5. Takes breaks every 20 and 50 users

### Safety Features

- 2-3 seconds delay between each user
- 20-30 seconds break every 20 users
- 60-90 seconds break every 50 users
- Random scrolling and waiting to mimic human behavior
- Uses existing Chrome session to maintain cookies and session

### Notes

- Keep Chrome window visible during operation
- Don't interact with the browser while script is running
- Processing time approximately 20-25 minutes per 500 users
- Check results at: Profile → Following → Pending

---

## Türkçe

### Özellikler

- Toplu takip isteği iptali
- İnsan benzeri davranış ile tespit edilmeme
- İlerleme takibi ve detaylı istatistikler
- Mevcut Chrome oturumu üzerinden tarayıcı otomasyonu
- Güvenli çalışma modu

### Gereksinimler

- Python 3.8 veya üstü
- Google Chrome tarayıcı
- Chrome'da açık Instagram hesabı

### Kurulum

1. Repoyu klonlayın
```bash
git clone https://github.com/mobilteknolojileri/instagram-pending-requests-canceler.git
cd instagram-pending-requests-canceler
```

2. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
playwright install chromium
```

### Instagram Verilerinizi İndirme

1. Instagram'ı web tarayıcıda açın
2. **Ayarlar** → **Hesaplar Merkezi** yolunu izleyin
3. **Bilgilerin ve izinlerin** seçeneğini tıklayın
4. **Bilgilerini dışa aktar** üzerine tıklayın
5. Instagram hesabınızı seçin
6. **Bilgilerini indir veya aktar** → **Bilgilerinin bazıları** seçin
7. **Takipçiler, takip edilenler ve takip istekleri** seçeneğini işaretleyin
8. Tarih aralığını **Tüm zamanlar** olarak ayarlayın
9. Format: **JSON**
10. İsteği gönderin ve indirme bağlantısını bekleyin

İndirip açtıktan sonra verileriniz şu klasör yapısında olacaktır:
```
instagram-kullaniciadi-2025-10-23-xxeadawdvb/
└── connections/
    └── followers_and_following/
        └── pending_follow_requests.json
```

### Kullanım

1. Chrome user agent bilginizi alın: [https://iplogger.org/useragents/](https://iplogger.org/useragents/)

2. `launch_chrome.bat` dosyasını güncelleyin:
```batch
--user-agent="YOUR_USER_AGENT_HERE"
```

3. Chrome'u debug modunda başlatın:
```bash
launch_chrome.bat
```

4. Açılan Chrome penceresinde Instagram'a giriş yapın

5. Scripti çalıştırın:
```bash
python cancel_requests.py
```

6. Sizden istendiğinde `pending_follow_requests.json` dosya yolunu girin

### Nasıl Çalışır

Script her bekleyen istek için şu işlemleri yapar:
1. Kullanıcı profiline gider
2. "İstek Gönderildi" butonuna tıklar
3. "Takibi Bırak" seçeneğini seçer
4. İşlemler arasında rastgele gecikmeler uygular
5. Her 20 ve 50 kullanıcıda mola verir

### Güvenlik Özellikleri

- Her kullanıcı arasında 2-3 saniye gecikme
- Her 20 kullanıcıda 20-30 saniye mola
- Her 50 kullanıcıda 60-90 saniye uzun mola
- İnsan davranışını taklit için rastgele kaydırma ve bekleme
- Oturum bilgilerini korumak için mevcut Chrome oturumu kullanımı

### Notlar

- İşlem sırasında Chrome penceresi görünür durumda olmalı
- Script çalışırken tarayıcıyla etkileşime girmeyin
- 500 kullanıcı için yaklaşık 20-25 dakika sürer
- Sonuçları kontrol edin: Profil → Takip Edilenler → Beklemede

## Disclaimer / Sorumluluk Reddi

### English
This tool is developed for **educational and research purposes only**. It demonstrates browser automation techniques and interaction with web interfaces. 

- This tool is intended to help users manage their own Instagram account data exported through Instagram's official data export feature
- Users are responsible for compliance with Instagram's Terms of Service
- The author is not responsible for any consequences arising from the use of this tool
- Use at your own risk and discretion
- Consider this as a proof of concept for learning web automation with Playwright

**Recommended Use Cases:**
- Learning browser automation and web scraping techniques
- Understanding how to process exported social media data
- Research on social media data management
- Testing automation strategies in controlled environments

### Türkçe
Bu araç **yalnızca eğitim ve araştırma amaçlı** geliştirilmiştir. Tarayıcı otomasyonu teknikleri ve web arayüzleri ile etkileşimi göstermektedir.

- Bu araç, kullanıcıların Instagram'ın resmi veri dışa aktarma özelliği ile aldıkları kendi hesap verilerini yönetmelerine yardımcı olmak için tasarlanmıştır
- Kullanıcılar Instagram Kullanım Şartları'na uymaktan kendileri sorumludur
- Geliştirici, bu aracın kullanımından doğacak sonuçlardan sorumlu değildir
- Riski size ait olmak üzere kullanın
- Bunu Playwright ile web otomasyonu öğrenmek için bir kavram kanıtı olarak değerlendirin

**Önerilen Kullanım Alanları:**
- Tarayıcı otomasyonu ve web scraping tekniklerini öğrenme
- Dışa aktarılan sosyal medya verilerinin nasıl işleneceğini anlama
- Sosyal medya veri yönetimi üzerine araştırma
- Kontrollü ortamlarda otomasyon stratejilerini test etme

## Educational Purpose / Eğitsel Amaç

This project serves as a practical example of:
- Web automation using Playwright
- Processing JSON data from social media exports
- Implementing human-like behavior in automation scripts
- Managing browser sessions and cookies
- Error handling and rate limiting strategies

Bu proje şunlar için pratik bir örnek teşkil eder:
- Playwright kullanarak web otomasyonu
- Sosyal medya dışa aktarımlarından JSON verilerini işleme
- Otomasyon scriptlerinde insan benzeri davranış implementasyonu
- Tarayıcı oturumları ve çerezleri yönetme
- Hata yönetimi ve hız sınırlama stratejileri

## License

MIT License - See [LICENSE](LICENSE) file for details

## Author

[mobilteknolojileri](https://github.com/mobilteknolojileri)