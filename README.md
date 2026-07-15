# AutoVal — AI-Powered Used Car Price Predictor 🚗

A full-stack web application that predicts the resale value of used cars in the Indian market using a Gradient Boosting ML model trained on real data from Quikr (1995–2025).

---

## 🚀 Features

- **AI Price Prediction** — Instant estimate using a Gradient Boosting Regressor (R² ≈ 0.69)
- **Confidence Range** — Price range with ±12% margin shown visually
- **Depreciation Chart** — Interactive chart showing how value drops over time
- **Similar Listings** — Shows comparable cars from the dataset
- **Smart Insights** — Car age, km/year average, condition rating
- **Extended Dataset** — 996 data points covering 1995–2025, including Kia, MG, EV models

---

## 📦 Project Structure

```
autoval/
├── application.py              # Flask backend with API endpoints
├── CarPriceModel.pkl           # Trained Gradient Boosting model
├── Cleaned_Car_data_2026.csv   # Extended dataset (1995–2025)
├── requirements.txt
├── templates/
│   └── index.html              # Frontend UI
└── static/
    └── style.css               # Styling
```

---

## 🛠️ Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python application.py
```

Then open `http://localhost:5000` in your browser.

---

## 🧠 Model Details

| Model | R² Score | MAE |
|-------|----------|-----|
| Linear Regression | 0.42 | ₹2,31,225 |
| Random Forest | 0.67 | ₹1,86,132 |
| **Gradient Boosting** ✓ | **0.69** | **₹1,68,454** |

**Features used:** Company, Car Model, Year, Kilometres Driven, Fuel Type

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main UI |
| `/predict` | POST | Returns predicted price + range |
| `/api/models?company=X` | GET | Returns car models for a brand |
| `/api/depreciation` | GET | Returns year-wise value estimates |
| `/api/similar` | GET | Returns 3 similar cars from dataset |
| `/api/stats` | GET | Dataset statistics |

---

## 🎨 Design

- Dark industrial theme with neon yellow accent (#e8ff47)
- Fonts: Syne (display) + DM Sans (body)
- Fully responsive — works on mobile and desktop
- Animated price count-up, depreciation chart via Chart.js

---

## 📊 Dataset

- **Source:** Quikr.com used car listings (India)
- **Extended with:** Manually curated 2020–2025 models including EVs
- **Brands covered:** 28 including Kia, MG, Tata, Citroen, and all major manufacturers
- **Fuel types:** Petrol, Diesel, LPG, Electric

---

## 🎯 Design Thinking Framework

| Phase | Implementation |
|-------|---------------|
| **Empathize** | Used car sellers lack transparent pricing — rely on dealers |
| **Define** | "A first-time car seller needs a reliable price estimate without going to a dealer" |
| **Ideate** | Considered: dealer lookup, price tables, ML model |
| **Prototype** | Flask web app with real ML predictions |
| **Test** | Model evaluated with R², MAE on 20% held-out test set |
