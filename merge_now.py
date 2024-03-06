import os
from datetime import datetime

# Giriş ve çıkış klasörlerinin yolları
inbox_folder = "inbox"
output_folder = "output"

# Giriş klasöründeki dosyaları al
input_files = [file for file in os.listdir(inbox_folder) if os.path.isfile(os.path.join(inbox_folder, file))]

# Çıkış dosyasının adını oluştur
output_filename = datetime.now().strftime("%d.%m.%Y") + "-" + str(len(input_files)) + ".txt"
output_path = os.path.join(output_folder, output_filename)

# Çıkış dosyasını oluştur ve giriş dosyalarını birleştir
with open(output_path, "w") as output_file:
    for input_file in input_files:
        input_path = os.path.join(inbox_folder, input_file)
        with open(input_path, "r") as file:
            content = file.read()
            output_file.write(content + "\n")

print(f"Dosyalar başarıyla birleştirildi. Çıkış dosyası: {output_path}")