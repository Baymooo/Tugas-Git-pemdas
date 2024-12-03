data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# Tampilkan seluruh data panen
print(data_panen)

# Tampilkan data untuk lokasi2
lokasi2_data = data_panen['lokasi2']['hasil_panen']['jagung']
print(lokasi2_data)

# Tampilkan nama lokasi dari lokasi 3
lokasi3_nama = data_panen['lokasi3']['nama_lokasi']
print(lokasi3_nama)

# Percabangan untuk lokasi memerlukan perhatian khusus
for id_lokasi, info in data_panen.items():
    nama = info['nama_lokasi']
    padi = info['hasil_panen']['padi']
    jagung = info ['hasil_panen']['jagung']
    
    print(f"nama lokasi: {nama} \n Jumlah panen padi: {padi} \n Jumlah panen jagung: {jagung}")

    if padi > 1300 or jagung > 800:
        print(f"Lokasi {nama} memerlukan perhatian khusus")
    else:
        print(f"Lokasi {nama} dalam kondisi baik")
