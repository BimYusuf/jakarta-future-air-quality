
def data_5_tahun_kedepan():
    part = {'pm10', 'no2', 'co',  'so2', 'o3', 'pm25'}

    # tahun
    #     lokasi
    #         partikel

    future = {
    '2025' : ({'date': 1, 'bulan': 'Januari', 'year': 2025, 'lokasi': 'Bundaran HI', 'partikulat': {'pm10': '40.65', 'so2': '28.48', 'co': '6.88', 'o3': '33.54', 'no2': '13.35', 'pm25': '52.83'}, 'prediksi': 99.97, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2025, 'lokasi': 'Kelapa Gading', 'partikulat': {'pm10': '38.67', 'so2': '2.53', 'co': '11.21', 'o3': '71.60', 'no2': '7.28', 'pm25': '57.98'}, 'prediksi': 100.0, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2025, 'lokasi': 'Jagakarsa', 'partikulat': {'pm10': '47.58', 'so2': '15.23', 'co': '10.90', 'o3': '30.84', 'no2': '5.44', 'pm25': '57.22'}, 'prediksi': 99.66, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2025, 'lokasi': 'Lubang Buaya', 'partikulat': {'pm10': '41.72', 'so2': '36.15', 'co': '16.54', 'o3': '38.44', 'no2': '3.78', 'pm25': '93.94'}, 'prediksi': 99.96, 'cat': 'BAIK'}, {'date': 1, 'bulan': 'Januari', 'year': 2025, 'lokasi': 'Kebon Jeruk', 'partikulat': {'pm10': '39.07', 'so2': '19.60', 'co': '13.40', 'o3': '22.19', 'no2': '4.63', 'pm25': '79.45'}, 'prediksi': 88.44, 'cat': 'BAIK'}),
    '2026' : ({'date': 1, 'bulan': 'Januari', 'year': 2026, 'lokasi': 'Bundaran HI', 'partikulat': {'pm10': '40.65', 'so2': '28.48', 'co': '6.88', 'o3': '33.54', 'no2': '13.35', 'pm25': '52.83'}, 'prediksi': 99.97, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2026, 'lokasi': 'Kelapa Gading', 'partikulat': {'pm10': '38.67', 'so2': '2.53', 'co': '11.21', 'o3': '71.60', 'no2': '7.28', 'pm25': '57.98'}, 'prediksi': 100.0, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2026, 'lokasi': 'Jagakarsa', 'partikulat': {'pm10': '47.58', 'so2': '15.23', 'co': '10.90', 'o3': '30.84', 'no2': '5.44', 'pm25': '57.22'}, 'prediksi': 99.66, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2026, 'lokasi': 'Lubang Buaya', 'partikulat': {'pm10': '41.72', 'so2': '36.15', 'co': '16.54', 'o3': '38.44', 'no2': '3.78', 'pm25': '93.94'}, 'prediksi': 99.96, 'cat': 'BAIK'}, {'date': 1, 'bulan': 'Januari', 'year': 2026, 'lokasi': 'Kebon Jeruk', 'partikulat': {'pm10': '39.07', 'so2': '19.60', 'co': '13.40', 'o3': '22.19', 'no2': '4.63', 'pm25': '79.45'}, 'prediksi': 88.44, 'cat': 'BAIK'}),
    '2027' : ({'date': 1, 'bulan': 'Januari', 'year': 2027, 'lokasi': 'Bundaran HI', 'partikulat': {'pm10': '40.65', 'so2': '28.48', 'co': '6.88', 'o3': '33.54', 'no2': '13.35', 'pm25': '52.83'}, 'prediksi': 99.97, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2027, 'lokasi': 'Kelapa Gading', 'partikulat': {'pm10': '38.67', 'so2': '2.53', 'co': '11.21', 'o3': '71.60', 'no2': '7.28', 'pm25': '57.98'}, 'prediksi': 100.0, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2027, 'lokasi': 'Jagakarsa', 'partikulat': {'pm10': '47.58', 'so2': '15.23', 'co': '10.90', 'o3': '30.84', 'no2': '5.44', 'pm25': '57.22'}, 'prediksi': 99.66, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2027, 'lokasi': 'Lubang Buaya', 'partikulat': {'pm10': '41.72', 'so2': '36.15', 'co': '16.54', 'o3': '38.44', 'no2': '3.78', 'pm25': '93.94'}, 'prediksi': 99.96, 'cat': 'BAIK'}, {'date': 1, 'bulan': 'Januari', 'year': 2027, 'lokasi': 'Kebon Jeruk', 'partikulat': {'pm10': '39.07', 'so2': '19.60', 'co': '13.40', 'o3': '22.19', 'no2': '4.63', 'pm25': '79.45'}, 'prediksi': 88.44, 'cat': 'BAIK'}),
    '2028' : ({'date': 1, 'bulan': 'Januari', 'year': 2028, 'lokasi': 'Bundaran HI', 'partikulat': {'pm10': '40.65', 'so2': '28.48', 'co': '6.88', 'o3': '33.54', 'no2': '13.35', 'pm25': '52.83'}, 'prediksi': 99.97, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2028, 'lokasi': 'Kelapa Gading', 'partikulat': {'pm10': '38.67', 'so2': '2.53', 'co': '11.21', 'o3': '71.60', 'no2': '7.28', 'pm25': '57.98'}, 'prediksi': 100.0, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2028, 'lokasi': 'Jagakarsa', 'partikulat': {'pm10': '47.58', 'so2': '15.23', 'co': '10.90', 'o3': '30.84', 'no2': '5.44', 'pm25': '57.22'}, 'prediksi': 99.66, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2028, 'lokasi': 'Lubang Buaya', 'partikulat': {'pm10': '41.72', 'so2': '36.15', 'co': '16.54', 'o3': '38.44', 'no2': '3.78', 'pm25': '93.94'}, 'prediksi': 99.96, 'cat': 'BAIK'}, {'date': 1, 'bulan': 'Januari', 'year': 2028, 'lokasi': 'Kebon Jeruk', 'partikulat': {'pm10': '39.07', 'so2': '19.60', 'co': '13.40', 'o3': '22.19', 'no2': '4.63', 'pm25': '79.45'}, 'prediksi': 88.44, 'cat': 'BAIK'}),
    '2029' : ({'date': 1, 'bulan': 'Januari', 'year': 2029, 'lokasi': 'Bundaran HI', 'partikulat': {'pm10': '40.65', 'so2': '28.48', 'co': '6.88', 'o3': '33.54', 'no2': '13.35', 'pm25': '52.83'}, 'prediksi': 99.97, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2029, 'lokasi': 'Kelapa Gading', 'partikulat': {'pm10': '38.67', 'so2': '2.53', 'co': '11.21', 'o3': '71.60', 'no2': '7.28', 'pm25': '57.98'}, 'prediksi': 100.0, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2029, 'lokasi': 'Jagakarsa', 'partikulat': {'pm10': '47.58', 'so2': '15.23', 'co': '10.90', 'o3': '30.84', 'no2': '5.44', 'pm25': '57.22'}, 'prediksi': 99.66, 'cat': 'SEDANG'}, {'date': 1, 'bulan': 'Januari', 'year': 2029, 'lokasi': 'Lubang Buaya', 'partikulat': {'pm10': '41.72', 'so2': '36.15', 'co': '16.54', 'o3': '38.44', 'no2': '3.78', 'pm25': '93.94'}, 'prediksi': 99.96, 'cat': 'BAIK'}, {'date': 1, 'bulan': 'Januari', 'year': 2029, 'lokasi': 'Kebon Jeruk', 'partikulat': {'pm10': '39.07', 'so2': '19.60', 'co': '13.40', 'o3': '22.19', 'no2': '4.63', 'pm25': '79.45'}, 'prediksi': 88.44, 'cat': 'BAIK'})
    }
    rata_rata = {}

    rata_part = {
        'pm10' : 0,
        'no2' : 0,
        'co' : 0,
        'so2' : 0,
        'o3' : 0,
        'pm25' : 0
    }

    for y in future: #tahun
        rata_rata[y] = {}
        for d in future[y]: #lokasi
            for p in part: #partikulat
                rata_part[p] = rata_part[p]  + float(d['partikulat'][p])
                print(rata_part[p])
        rata_part = {key : 0 for key in rata_part}    
            
data_5_tahun_kedepan()