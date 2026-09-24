from fastapi import FastAPI
import pickle
import pandas as pd
from data_model import Water

# API ornegi olusturma
app = FastAPI(
    title = "Water Potability Prediction",
    description = "Predicting Water Potability"
)

# Onceden egitilen modeli yuklemek
with open("/Users/hilalbeyzaertunc/ml_pipeline/model.pkl", "rb") as f:
    model = pickle.load(f)
    
#API nin uc noktası root (r) biri bu noktaya erisirse bu yaziyi gorecek
# Anasayfa gorevi goren root uc noktasi

@app.get("/")
def index():
     return "Welcome to Water Potability Prediction FastAPI"
 
 # Tahmin icin bir uc nokta 
 
@app.post("/predict")
def model_predict(water: Water): 
    sample = pd.DataFrame({
        'ph' : [water.ph],
        'Hardess':[water.Hardness],
        'Solids' : [water.Solids],
        'Chloramines' :[water.Chloramines],
        'Sulfate' : (water.Sulfate),
        'Conductivity' :[water.Conductivity],
        'Organic_carbon' : [water.Organic_carbon],
        'Trihalomethanses' : [water.Trihalomethanses],
        'Turbidity' :[water.Turbidity]
      
    })
    
    predicted_value =model.predict(sample)
    
    if predicted_value == 1:
        return "Water is Consumable"
    else:
        return "Water is not Consumable"