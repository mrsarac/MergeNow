This application was created by ClaudeAI.

# MergeNow - File Merge Application

This application reads all files in the specified input folder and merges them into a single file. The merged file is saved in the output folder.

## How does it work?

1. All files under the `inbox` folder are read.
2. The contents of the read files are merged.
3. The merged content is written to a new file under the `output` folder.
4. The name of the output file is created in the format `GG.AA.YYYYY-N.txt`. Here:
   - `GG`: Two-digit numeric value of the day
   - `AA`: Two-digit numeric value of the month
   - `YYYYY`: Four-digit numeric value of the year
   - `N`: Number of merged files

How to use ##

1. Place the files you want to merge under the `inbox` folder.
2. In Terminal, run `python merge_now.py` in the project's home directory.
3. The merged file will be created under the `output` folder.

## Requirements

- Python 3.x

---

When the application is run, it will read the files in the `inbox` folder and save the merged file in the `output` folder in the specified format.

---

# MergeNow - Dosya Birleştirme Uygulaması

Bu uygulama, belirtilen giriş klasöründeki tüm dosyaları okur ve tek bir dosya olarak birleştirir. Birleştirilen dosya, çıkış klasörüne kaydedilir.

## Nasıl Çalışır?

1. `inbox` klasörü altındaki tüm dosyalar okunur.
2. Okunan dosyaların içerikleri birleştirilir.
3. Birleştirilen içerik, `output` klasörü altında yeni bir dosyaya yazılır.
4. Çıkış dosyasının adı, `GG.AA.YYYY-N.txt` formatında oluşturulur. Burada:
   - `GG`: Günün iki haneli sayısal değeri
   - `AA`: Ayın iki haneli sayısal değeri
   - `YYYY`: Yılın dört haneli sayısal değeri
   - `N`: Birleştirilen dosya sayısı

## Nasıl Kullanılır?

1. `inbox` klasörü altına birleştirmek istediğiniz dosyaları yerleştirin.
2. Terminal'de projenin ana dizininde `python merge_now.py` komutunu çalıştırın.
3. Birleştirilen dosya `output` klasörü altında oluşturulacaktır.

## Gereksinimler

- Python 3.x

---

Uygulama çalıştırıldığında, `inbox` klasöründeki dosyaları okuyacak ve `output` klasörüne belirtilen formatta birleştirilmiş dosyayı kaydedecektir.
