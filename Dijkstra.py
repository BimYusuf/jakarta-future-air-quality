# import library
import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier, XGBRegressor
from datetime import datetime


def inputMachinery(lokasi, date, month, year):

    # data preprocessing 
    # 1. buat dataframe untuk tiap dataset
    dki1 = pd.read_csv("data/ispu_dki1.csv")
    dki2 = pd.read_csv("data/ispu_dki2.csv")
    dki3 = pd.read_csv("data/ispu_dki3.csv")
    dki4 = pd.read_csv("data/ispu_dki4.csv")
    dki5 = pd.read_csv("data/ispu_dki5.csv")
    list_df = [dki1, dki2, dki3, dki4, dki5]

    # 2. buang data 2010, banyak kosong bro
    def remove_year(list_df):
        for i, df in enumerate(list_df):
            df['tanggal'] = pd.to_datetime(df['tanggal'])
            list_df[i] = df[df['tanggal'].dt.year != 2010]
            list_df[i].reset_index(drop=True, inplace=True)

    remove_year(list_df)

    # 3. buang kolom stasiun, ga butuh buat prediksi 
    for df in list_df:
        df.drop('stasiun', axis= 1, inplace= True)
        
    # 4. pindah pm25 ke kolom ke 6 (indexing python base zero, jadi secara riil sebenarnya kolom ke 7)
    for i, df in enumerate(list_df):
        move_pm25 = df.pop("pm25")
        list_df[i].insert(6, "pm25", move_pm25)
    
    # 5. taking care of Missing Value in each features/columns/particles using iterative imputer
    imp = IterativeImputer(random_state=10, max_iter = 100)
    column = list_df[0].columns[1:7]
    for i, df in enumerate(list_df):
        for col in column:
            list_df[i][col] = imp.fit_transform(df[[col]])
        
    # 6. Fill the max column
    def get_max(df):
        df_temp = df.drop(['tanggal', 'critical', 'categori'], axis= 1)
        df['max'] = df_temp.apply(lambda row: row.max(), axis=1)
        return df

    for i, df in enumerate (list_df):
        list_df[i] = get_max(df)

    # 7. # Fill Critical column
    def get_max_column(row):
        return row.idxmax()

    def get_critical(df):
        df_temp = df.drop(['tanggal', 'critical', 'categori'], axis= 1)
        df['critical'] = df_temp.apply(get_max_column, axis=1)
        return df

    for i, df in enumerate(list_df):
        list_df[i] = get_critical(df)

    # 7. encode category variable using LabelEncoder for better experience
    category_mapping = {'BAIK': 0, 
                        'SEDANG': 1,
                        'TIDAK SEHAT': 2,
                        'SANGAT TIDAK SEHAT': 3,
                        'BERBAHAYA': 4,
                        'TIDAK ADA DATA': 5}

    le = LabelEncoder()
    le.fit(list(category_mapping.keys()))
    for i, df in enumerate(list_df):
        list_df[i]['categori'] = df['categori'].map(category_mapping)

    # 8. Handling the 'TIDAK ADA DATA/5' value
    xg_class = XGBClassifier()

    for i, df in enumerate(list_df):
        list_df[i]['categori'].replace(5, np.nan, inplace=True)
        
        list_df[i]['categori'] = df['categori'].astype(float).astype('Int64')
        df_train = df.dropna(subset=['categori'])
        df_test = df[df['categori'].isnull()]

        features = ['pm10', 'so2', 'co', 'o3', 'no2', 'pm25']
        target = 'categori'

        X_train = df_train[features]
        y_train = df_train[target]

        xg_class.fit(X_train, y_train)
        
        if not df_test.empty:
            X_test = df_test[features]
            df_test['categori'] = xg_class.predict(X_test)

            df.update(df_test)

        df.reset_index(drop=True, inplace=True)
        list_df[i] = df.copy()
    
    # 9. buat 3 kolom baru daru kolom tanggal jadi kolom year, month, and date 
    for i, df in enumerate(list_df):
        list_df[i]['year'] = df['tanggal'].dt.year
        list_df[i]['month'] = list_df[i]['tanggal'].dt.month
        list_df[i]['date'] = list_df[i]['tanggal'].dt.day
        list_df[i].drop('tanggal', axis=1, inplace=True)

    # 10. input option, to switch the predicted location

    option = lokasi

    while(option < 1 or option > 5):
        print("Input tidak valid, coba lagi!")
        option = int(input("> "))

    option = option - 1

    # train the model using regression and classsification
    xg = XGBRegressor()
    xg_class = XGBClassifier()

    X_class = list_df[option].drop(['categori', 'year','month','date','critical','max'], axis= 1)
    y_class = list_df[option]['categori']

    num_col = ['pm10','so2','co','o3','no2','pm25']
    X = list_df[option].drop(['pm10','so2','co','o3','no2','pm25','max','critical','categori'], axis=1)

    lokasi = ['Bundaran HI', 'Kelapa Gading', 'Jagakarsa', 'Lubang Buaya', 'Kebon Jeruk']

    def train_xgb(df, year_input, month_input, date_input):
        list_predict = []
        for col in num_col:
            xg.fit(X, df[col]) 
            list_predict.append(xg.predict([[year_input, month_input, date_input]])[0])

        df_predict = pd.DataFrame(np.array(list_predict).reshape(1, -1), columns= num_col)

        xg_class.fit(X_class, y_class)
        return xg_class.predict(df_predict) , xg_class.predict_proba(df_predict)

    # error handling untuk input
    def validate_date_future(year, month, day):
        try:
            # validasi tanggal secara umum
            if not (1 <= int(year) <= 9999):
                raise ValueError("Tahun harus antara 1 dan 9999")

            if not (1 <= int(month) <= 12):
                raise ValueError("Bulan harus antara 1 dan 12")

            if not (1 <= int(day) <= 31):
                raise ValueError("Tanggal harus antara 1 dan 31")

            if int(month) in [4, 6, 9, 11] and int(day) > 30:
                raise ValueError(f"Bulan {month} hanya memiliki maksimal 30 hari")

            if int(month) == 2:
                if int(day) > 29 or (int(day) > 28 and not (int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0))):
                    raise ValueError(f"Februari pada tahun {year} hanya memiliki maksimal 28 atau 29 hari")

            # Validasi tanggal agar hanya predict di masa depan
            current_date = datetime.now().date()
            input_date = datetime(int(year), int(month), int(day)).date()

            if input_date <= current_date:
                raise ValueError("Tanggal harus di masa depan")

        except ValueError as e:
            print(f"Error: {e}")
            return False

        return True

    # input dan output
    date_input = date
    month_input = month
    year_input = year

    tuple_bulan = ('Januari', 'Februari', 'Maret', 'April', 'Mei','Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')

    data = {
        'date' : date,
        'bulan' : tuple_bulan[int(month-1)],
        'year' : year,
        'lokasi' : lokasi[option],
        'partikulat' : {
            'pm10' : 0,
            'so2' : 0,
            'co' : 0,
            'o3' : 0,
            'no2' : 0,
            'pm25' : 0
        }
    }

    def generate_output(df, year_input, month_input, date_input):
        list_predictions = []
        for col in num_col:
            xg.fit(X, df[col])
            prediction = xg.predict([[year_input, month_input, date_input]])[0]
            list_predictions.append({col: prediction})
        return list_predictions

    if not validate_date_future(year_input, month_input, date_input):
        return "Input tidak valid. Program berhenti."
    else:
        predictions = generate_output(list_df[option], int(year_input), int(month_input), int(date_input))

        for prediction in predictions:
            for particle, concentration in prediction.items():
                data['partikulat'][particle] = f'{round(concentration, 2):.2f}'


        cat, proba = train_xgb(list_df[option], int(year_input), int(month_input), int(date_input))
        data['prediksi'] = round(proba[0][cat][0] * 100, 2)

        tuple_cat = ('BAIK', 'SEDANG', 'TIDAK SEHAT', 'SANGAT TIDAK SEHAT', 'BERBAHAYA')
        data['cat'] = tuple_cat[cat[0]]
    return data
       


# tmp = (inputMachinery(1, 1, 1, 2029), 
# inputMachinery(2, 1, 1, 2029), 
# inputMachinery(3, 1, 1, 2029), 
# inputMachinery(4, 1, 1, 2029), 
# inputMachinery(5, 1, 1, 2029))

ttgl = 1
bln = 5

all = {}
for i in range(2025, 2029):
    tmp = (inputMachinery(1, ttgl, bln, i), 
    inputMachinery(2, ttgl, bln, i), 
    inputMachinery(3, ttgl, bln, i), 
    inputMachinery(4, ttgl, bln, i), 
    inputMachinery(5, ttgl, bln, i))
    all[i] = tmp 

print(all)

