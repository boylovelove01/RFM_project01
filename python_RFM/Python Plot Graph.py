# Re-import required libraries since execution state was reset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 โหลดข้อมูล RFM Segmentation
rfm_segment_file = r"C:\Users\l3oy_\Documents\RFM_Segments.xlsx"

# 📌 ตรวจสอบว่าไฟล์สามารถโหลดได้หรือไม่
try:
    rfm_df = pd.read_excel(rfm_segment_file)
except FileNotFoundError:
    raise FileNotFoundError("❌ ไม่พบไฟล์ RFM Segments.xlsx โปรดตรวจสอบที่อยู่ไฟล์!")

# 📌 ตรวจสอบว่ามีคอลัมน์ Segment อยู่หรือไม่
if "Segment" not in rfm_df.columns:
    raise ValueError("❌ คอลัมน์ 'Segment' ไม่พบในไฟล์ โปรดตรวจสอบข้อมูล!")

# 📌 นับจำนวนลูกค้าในแต่ละกลุ่ม
segment_counts = rfm_df["Segment"].value_counts()

# 📌 สร้าง Pie Chart สำหรับ Segmentation
plt.figure(figsize=(8, 6))
segment_counts.plot.pie(autopct='%1.1f%%', startangle=140, cmap="Set2")
plt.ylabel("")
plt.title("Customer Segmentation Distribution")

# 📌 แสดงกราฟ
plt.show()

# 📌 สร้าง Bar Chart สำหรับ RFM ค่าเฉลี่ยของแต่ละ Segment
plt.figure(figsize=(12, 6))
rfm_avg = rfm_df.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean()
rfm_avg.plot(kind="bar", figsize=(12, 6), colormap="viridis")

plt.title("Average RFM Values by Segment")
plt.xlabel("Segment")
plt.ylabel("Average Value")
plt.xticks(rotation=45)
plt.legend(title="RFM Metrics")

# 📌 แสดงกราฟ
plt.show()

# 📌 แสดงผลข้อมูลแบบ DataFrame
#import ace_tools as tools

# 📌 Boxplot ของ RFM เพื่อวิเคราะห์ค่ากระจายตัวของแต่ละ Segment
plt.figure(figsize=(15, 6))

plt.subplot(1, 3, 1)
sns.boxplot(x="Segment", y="Recency", data=rfm_df, palette="Set2")
plt.xticks(rotation=45)
plt.title("Recency Distribution by Segment")

plt.subplot(1, 3, 2)
sns.boxplot(x="Segment", y="Frequency", data=rfm_df, palette="Set2")
plt.xticks(rotation=45)
plt.title("Frequency Distribution by Segment")

plt.subplot(1, 3, 3)
sns.boxplot(x="Segment", y="Monetary", data=rfm_df, palette="Set2")
plt.xticks(rotation=45)
plt.title("Monetary Distribution by Segment")

plt.tight_layout()
plt.show()

# 📌 Scatter Plot เพื่อดูความสัมพันธ์ระหว่าง Frequency และ Monetary
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Frequency", y="Monetary", hue="Segment", data=rfm_df, palette="Set1", alpha=0.7)
plt.xlabel("Frequency")
plt.ylabel("Monetary")
plt.title("Frequency vs Monetary by Segment")
plt.legend(title="Segment")
plt.show()

# 📌 Scatter Plot ของ Recency และ Monetary
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Recency", y="Monetary", hue="Segment", data=rfm_df, palette="Set2", alpha=0.7)
plt.xlabel("Recency")
plt.ylabel("Monetary")
plt.title("Recency vs Monetary by Segment")
plt.legend(title="Segment")
plt.show()
