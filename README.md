# Atari Oyunu – Python (Turtle)

Bu proje, Python'un `turtle` modülü ile geliştirilmiş basit bir Atari benzeri oyundur. 
Oyuncu, hareket eden bir paleti (paddle) kontrol eder ve topu düşürmemeye çalışır.

## Özellikler
- Paddle (raket) hareketleri
- Top çarpma mekaniği
- Skor takibi (scoreboard)
- Temiz, modüler Python kod yapısı (`main.py`, `top.py`, `paddle.py`, `scoreboard.py`)

##  Nasıl Çalıştırılır?
1. Python 3.13 yüklü olmalı
2. Gerekirse `turtle` modülünü yükleyin (genelde Python ile gelir)
3. `main.py` dosyasını çalıştırın

##  Dosya Açıklamaları
- `main.py` → Oyunun ana kontrol dosyası
- `paddle.py` → Oyuncunun kontrol ettiği raket sınıfı
- `top.py` → Top sınıfı ve hareketi
- `scoreboard.py` → Skor güncelleme ve oyun sonu mesajı
