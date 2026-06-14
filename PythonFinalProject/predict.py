import joblib
from tensorflow.keras.models import load_model
import pandas as pd
from helper import Helper

model = load_model("cardio_nn.keras")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

print("\nEnter Patient Details\n")
helper = Helper()

age_years = helper.get_btwn_range(prompt="Enter Age (in years): ", min_val=0, max_val=120, keyword="age")
height = helper.get_btwn_range(prompt="Enter height (in cms): ", min_val=60, max_val=250, keyword="height")
weight = helper.get_btwn_range(prompt="Enter weight (in kgs): ", min_val=20, max_val=210, keyword="weight")
gender = helper.get_gender(prompt="Gender (1 = Female, 2 = Male): ")
ap_hi = helper.get_btwn_range(prompt="Systolic Blood Pressure (ap_hi): ", min_val=80, max_val=250, keyword="Systolic BP")
ap_lo = helper.get_btwn_range(prompt="Diastolic Blood Pressure (ap_lo): ", min_val=40, max_val=150, keyword="Diastolic BP")
cholesterol = helper.get_three_categorical(prompt="Cholesterol (1 = Normal, 2 = Above Normal, 3 = Well Above Normal): ")
gluc = helper.get_three_categorical(prompt="Glucose (1 = Normal, 2 = Above Normal, 3 = Well Above Normal): ")
smoke = helper.get_binary(prompt="Smoking? (0 = No, 1 = Yes): ")
alco = helper.get_binary(prompt="Alcohol Intake? (0 = No, 1 = Yes): ")
active = helper.get_binary(prompt="Physically Active? (0 = No, 1 = Yes): ")

bmi = weight / ((height / 100) ** 2)

df = pd.DataFrame([{
    "gender": gender,
    "height": height,
    "weight": weight,
    "ap_hi": ap_hi,
    "ap_lo": ap_lo,
    "cholesterol": cholesterol,
    "gluc": gluc,
    "smoke": smoke,
    "alco": alco,
    "active": active,
    "bmi": bmi,
    "age_years": age_years
}])

df = df.reindex(columns=feature_columns)

df_scaled = scaler.transform(df)

conf = model.predict(df_scaled)[0][0]
pred = int(conf > 0.5)

if pred == 1:
    print("You are prone to Cardiovascular disease")
else:
    print("You are not prone to Cardiovascular disease")

print("confidence:", conf)