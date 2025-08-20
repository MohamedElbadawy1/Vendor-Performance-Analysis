# 📊 Vendor Sales Analysis  

## 📌 Business Problem  
Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies need to ensure that they are not incurring losses due to inefficient pricing, poor inventory turnover, or vendor dependency.  

The goal of this analysis is to:  
- 🔍 Identify underperforming brands that require promotional or pricing adjustments.  
- 🏆 Determine top vendors contributing to sales and gross profit.  
- 📉 Analyze the impact of bulk purchasing on unit costs.  
- 📦 Assess inventory turnover to reduce holding costs and improve efficiency.  
- 💰 Investigate the profitability variance between high-performing and low-performing vendors.  

---

## 📂 Project Structure  
📦 VendorPerformance Analysis
├── data
│ ├── begin_inventory.csv
│ ├── end_inventory.csv
│ ├── purchase_prices.csv
│ ├── purchases.csv
│ ├── sales.csv
│ └── vendor_invoice.csv
├── database
│ └── inventory.db
├── logs
│ ├── ingestion_bd.log
│ └── VendorSalesSummary.log
├── notebooks
│ ├── EDA.ipynb
│ └── Vendor Performance Analysis.ipynb
├── Processed Data
│ ├── brandPerformance.csv
│ └── VendorSalesSummary.csv
└── scripts
├── GetVendorSalesSummary.py
└── ingestDB.py

yaml
Copy
Edit

---

## ⚙️ Tech Stack  
- **Language**: Python  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn  
- **Database**: SQLite3  
- **Visualization**: Power BI, Jupyter Notebooks  
- **Logging**: Python `logging` module  

---

## 🚀 Setup & Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/VendorPerformanceAnalysis.git
   cd VendorPerformanceAnalysis
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
Load raw data into SQLite database

bash
Copy
Edit
python scripts/ingestDB.py
Generate vendor sales summary & processed reports

bash
Copy
Edit
python scripts/GetVendorSalesSummary.py
Explore the analysis

Open notebooks/EDA.ipynb for exploratory data analysis.

Open notebooks/Vendor Performance Analysis.ipynb for detailed vendor performance evaluation.

Open the Power BI dashboard to interact with vendor and brand insights.

📊 Outputs
Processed CSV Reports

Processed Data/brandPerformance.csv → Brand-level performance metrics

Processed Data/VendorSalesSummary.csv → Vendor sales, gross profit, and turnover summary

Database

database/inventory.db → Consolidated sales, purchases, and inventory data

Logs

logs/ingestion_bd.log → Database ingestion logs

logs/VendorSalesSummary.log → Vendor performance reporting logs

Dashboard

Power BI dashboard for interactive visualization of vendor performance, profitability, and inventory turnover

🔮 Future Improvements
Automate ETL pipelines using Airflow or Prefect.

Deploy dashboard using Power BI Service for real-time monitoring.

Integrate forecasting models to predict vendor sales and inventory turnover.

Expand analysis to include seasonality and regional performance.

📌 This project demonstrates end-to-end data analysis — from raw data ingestion and transformation to business-ready insights through Python and Power BI.

yaml
Copy
Edit

---

Would you like me to also **generate a ready `requirements.txt` file code** for you (so anyone can i
