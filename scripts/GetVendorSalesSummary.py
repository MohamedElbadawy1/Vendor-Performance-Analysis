import pandas as pd
import sqlite3
import logging
import time
from ingestDB import ingest_db

logging.basicConfig(
    handlers=[logging.FileHandler("logs/VendorSalesSummary.log", mode="a", encoding="utf-8")],
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
        force=True
)
def CreateVendorSalesSummary(conn):
    vendor_sales_summary = pd.read_sql_query("""
WITH FreightSummary AS (
                        SELECT VendorNumber, SUM(Freight) as FreightCost
                        FROM vendor_invoice
                        GROUP BY VendorNumber
                                         ),

PurchaseSummary as
                 (
                  Select p.VendorNumber, p.VendorName, p.Brand, p.PurchasePrice,
                  p.Description,
                  SUM(p.Quantity) as TotalPurchasesQuantity,
                  SUM(p.Dollars) as TotalPurchasesDollars,
                  pp.Volume, pp.Price as ActualPrice
                  From purchases p join purchase_prices pp
                  ON p.Brand = pp.Brand
                  where p.PurchasePrice >0
                  GROUP BY  p.VendorNumber, p.VendorName, p.Brand
                  ORDER BY TotalPurchasesDollars
                                         ),

SalesSummary as
                (SELECT VendorNo, Brand,
                  SUM(SalesQuantity) as TotalQuantitySold,
                  SUM(SalesDollars) as TotalSalesDollars,
                  SUM(SalesPrice) as TotalSalesPrice,
                  SUM(ExciseTax) as TotalExciseTax
                  FROM sales
                  group by VendorNo, Brand)

select 
                  ps.VendorNumber, ps.VendorName, ps.Brand, ps.Description,
                  ps.PurchasePrice, ps.ActualPrice, ps.Volume, ps.TotalPurchasesQuantity,
                  ps.TotalPurchasesDollars, 
                  ss.TotalQuantitySold,ss.TotalSalesDollars,ss.TotalSalesPrice,
                  ss.TotalExciseTax,
                  fs.FreightCost

                  From PurchaseSummary as ps
                  LEFT JOIN SalesSummary as ss
                  on ps.VendorNumber = ss.VendorNo
                  and ps.Brand = ss.Brand
                  LEFT JOIN FreightSummary fs
                  ON ps.VendorNumber = fs.VendorNumber
                  ORDER BY ps.TotalPurchasesDollars DESC
""", conn)
    return vendor_sales_summary

def CleanData(vendor_sales_summary):
    vendor_sales_summary['VendorName'] = vendor_sales_summary['VendorName'].str.strip()
    vendor_sales_summary['Description'] = vendor_sales_summary['Description'].str.strip()
    vendor_sales_summary['Volume'] = vendor_sales_summary['Volume'].astype('float64')
    vendor_sales_summary.fillna(0, inplace=True)
    vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars']-vendor_sales_summary['TotalPurchasesDollars']
    vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit'] / vendor_sales_summary['TotalSalesDollars']) *100
    vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalQuantitySold']/ vendor_sales_summary['TotalPurchasesQuantity']
    vendor_sales_summary['TotalPurchaseRatio'] = vendor_sales_summary['TotalSalesDollars']/ vendor_sales_summary['TotalPurchasesDollars']

    return vendor_sales_summary

if __name__ == '__main__':
    conn = sqlite3.connect('inventory.db')

    logging.info("------Start Creating Vender Sales Summary------")
    summary_df = CreateVendorSalesSummary(conn)
    logging.info(summary_df.head(2))
    logging.info("------Vender Sales Summary Table Created------")

    logging.info("------Start Data Cleaning------")
    clean_df = CleanData(summary_df)
    logging.info(clean_df.head(2))
    logging.info("------Vender Sales Summary cleaned------")

    logging.info("------Ingesting Data------")
    ingest_db(clean_df, 'vendor_sales_summary', conn)
    logging.info("------Completed successfully!------")
    logging.shutdown()


