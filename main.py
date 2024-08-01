import random

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SIGMA": "Sosok Seorang yang baik dan independen",
            "ROFL": "Tanggapan terhadap lelucon"
            }
            
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    pass
    print(meme_dict[word])
    
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("Kata kunci tidak ditemukan")
