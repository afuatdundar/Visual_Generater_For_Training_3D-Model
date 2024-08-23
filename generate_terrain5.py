import pyautogui
import time
import os

# Seed değerlerinin başlangıç, bitiş ve artış miktarı
start_seed = 0
end_seed = 30000
step = 100

# Fotoğrafların kaydedileceği klasör
output_dir = 'C:/Users/Asus/Desktop/4km/island_Form'

# Klasör yoksa oluştur
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def set_seed_and_generate(seed, x, y):
    # Seed kutusuna git ve değeri ayarla
    pyautogui.click(x=x, y=y)  # Seed kutusunun koordinatları

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(str(seed))
    pyautogui.press('enter')
    time.sleep(2)  # Değişikliklerin uygulanması için bekle

def export_terrain(file_number):
    # Export terrain butonuna git ve tıkla
    pyautogui.click(x=83, y=439)  # Export terrain butonunun koordinatları
    time.sleep(2)

    # Dosya adını belirle
    file_name = f'{file_number}'
    pyautogui.click(x=1878, y=205)  # Dosya adı kutusunun koordinatları
  
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(file_name)
    pyautogui.press('enter')
    time.sleep(1)

    # Export now butonuna tıkla
    pyautogui.click(x=1750, y=612)  # Export now butonunun koordinatları
    time.sleep(2)  # Export işlemi için bekle

    # "Export completed" mesajını kapat
    pyautogui.click(x=953, y=562)  # "Close" butonunun koordinatları
    time.sleep(3)

# Dosya numaralandırma için sayaç
file_counter = 1

# Her bir Billowy noise elemanı için işlemi tekrarla
for seed in range(start_seed, end_seed + step, step):
    # İlk Billowy noise elemanı için
    pyautogui.click(x=92, y=280)  # İlk Billowy noise elemanının koordinatları
    time.sleep(2)
    set_seed_and_generate(seed, 1650, 1009)
    
    
    
    # Export işlemi
    export_terrain(file_counter)
    
    print(f'Seed {seed} için arazi modeli oluşturuldu ve "{output_dir}/{file_counter}.png" konumuna kaydedildi.')
    
    # Dosya numaralandırma sayacını artır
    file_counter += 1

