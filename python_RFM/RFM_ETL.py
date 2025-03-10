import pandas as pd
from datetime import datetime, timedelta

# 📌 กำหนดที่อยู่ไฟล์
file_path = r"C:\Users\l3oy_\Documents\True_Money_Deposit_Transactions.xlsx"

# 📌 อ่านข้อมูลจากไฟล์ Excel
df = pd.read_excel(file_path)

# 📌 ตรวจสอบคอลัมน์ของไฟล์
print("Columns in dataset:", df.columns)

# 📌 แปลงคอลัมน์วันที่ให้เป็น datetime
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

# 📌 กำหนดวันที่อ้างอิงสำหรับการวิเคราะห์ RFM (วันล่าสุด +1)
reference_date = df["Transaction_Date"].max() + timedelta(days=1)

# 📌 คำนวณค่า RFM
rfm_df = df.groupby("Customer_ID").agg(
    Recency=("Transaction_Date", lambda x: (reference_date - x.max()).days),  # จำนวนวันที่ผ่านมาตั้งแต่ธุรกรรมล่าสุด
    Frequency=("Transaction_Date", "count"),  # จำนวนครั้งที่ฝากเงิน
    Monetary=("Deposit_Amount", "sum")  # จำนวนเงินรวมที่ฝาก
).reset_index()

# 📌 แสดงตัวอย่างข้อมูล RFM
print(rfm_df.head())

# 📌 บันทึกผลลัพธ์เป็นไฟล์ใหม่
rfm_file_path = r"C:\Users\l3oy_\Documents\RFM_Results.xlsx"
rfm_df.to_excel(rfm_file_path, index=False)
print(f"✅ RFM Model ถูกบันทึกที่: {rfm_file_path}")
