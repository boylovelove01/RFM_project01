import pandas as pd
# 📌 โหลดข้อมูล RFM
rfm_file_path = r"C:\Users\l3oy_\Documents\RFM_Results.xlsx"
rfm_df = pd.read_excel(rfm_file_path)

# 📌 กำหนดคะแนน 1-5 สำหรับ R, F, M โดยใช้ quantile
rfm_df["R_Score"] = pd.qcut(rfm_df["Recency"], q=5, labels=[5, 4, 3, 2, 1])
rfm_df["F_Score"] = pd.qcut(rfm_df["Frequency"], q=5, labels=[1, 2, 3, 4, 5])
rfm_df["M_Score"] = pd.qcut(rfm_df["Monetary"], q=5, labels=[1, 2, 3, 4, 5])

# 📌 รวมคะแนน RFM Score
rfm_df["RFM_Score"] = rfm_df["R_Score"].astype(int) + rfm_df["F_Score"].astype(int) + rfm_df["M_Score"].astype(int)

# 📌 กำหนด Segment ตาม RFM Score
def assign_segment(score):
    if score >= 12:
        return "VIP"
    elif score >= 9:
        return "Loyal"
    elif score >= 6:
        return "Potential"
    else:
        return "Churn"

rfm_df["Segment"] = rfm_df["RFM_Score"].apply(assign_segment)

# 📌 แสดงตัวอย่างข้อมูล
print(rfm_df.head())

# 📌 บันทึกเป็นไฟล์ใหม่
rfm_segment_file = r"C:\Users\l3oy_\Documents\RFM_Segments.xlsx"
rfm_df.to_excel(rfm_segment_file, index=False)
print(f"✅ RFM Segmentation ถูกบันทึกที่: {rfm_segment_file}")
