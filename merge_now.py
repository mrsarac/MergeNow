import os
from datetime import datetime

# Giriş ve çıkış klasörlerinin yolları
inbox_folder = "inbox"
output_folder = "output"

# Kullanıcıdan maksimum dosya boyutunu al
max_file_size_kb = input("Enter the maximum file size in KB (leave empty for no limit): ")
max_file_size = int(max_file_size_kb) * 1024 if max_file_size_kb else None  # Bayt cinsine dönüştür

# Giriş klasöründeki dosyaları al
input_files = [file for file in os.listdir(inbox_folder) if os.path.isfile(os.path.join(inbox_folder, file))]

# Birleştirilmiş içeriği tutacak değişken
merged_content = ""

# Giriş dosyalarını oku ve içeriklerini birleştir
for input_file in input_files:
    input_path = os.path.join(inbox_folder, input_file)
    with open(input_path, "r") as file:
        content = file.read()
        merged_content += content + "\n"

# Birleştirilmiş içeriği parçalara böl
file_parts = []
if max_file_size:
    while len(merged_content) > 0:
        file_part = merged_content[:max_file_size]
        file_parts.append(file_part)
        merged_content = merged_content[max_file_size:]
else:
    file_parts.append(merged_content)

# Parçaları ayrı dosyalara yaz
for i, file_part in enumerate(file_parts):
    output_filename = datetime.now().strftime("%d.%m.%Y") + "-" + str(len(input_files)) + "-" + str(i+1) + ".txt"
    output_path = os.path.join(output_folder, output_filename)
    with open(output_path, "w") as output_file:
        output_file.write(file_part)
    print(f"File part saved: {output_path}")

print("Files have been successfully merged and split into parts.")