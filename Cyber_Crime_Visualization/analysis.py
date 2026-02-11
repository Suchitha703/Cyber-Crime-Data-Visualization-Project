import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Program started successfully")

# Load dataset
df = pd.read_excel("cyber_crime_data.xlsx")

print("\nDataset Preview:")
print(df.head())

# Group data
city_cases = df.groupby("City")["Number_of_Cases"].sum()
crime_type = df.groupby("Cyber_Crime_Type")["Number_of_Cases"].sum()
city_loss = df.groupby("City")["Financial_Loss"].sum()

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 12))

# 1️⃣ PIE CHART – City-wise cases
axs[0, 0].pie(
    city_cases.values,
    labels=city_cases.index,
    autopct="%1.1f%%",
    startangle=140
)
axs[0, 0].set_title("City-wise Cyber Crime Distribution")

# 2️⃣ LINE GRAPH – Year-wise trend by city
sns.lineplot(
    data=df,
    x="Year",
    y="Number_of_Cases",
    hue="City",
    marker="o",
    ax=axs[0, 1]
)
axs[0, 1].set_title("Year-wise Cyber Crime Trend by City")

# 3️⃣ BAR GRAPH – Crime type
axs[1, 0].bar(crime_type.index, crime_type.values)
axs[1, 0].set_title("Cyber Crime Type-wise Cases")
axs[1, 0].tick_params(axis='x', rotation=45)

# 4️⃣ BAR GRAPH – Financial loss by city
axs[1, 1].bar(city_loss.index, city_loss.values)
axs[1, 1].set_title("City-wise Financial Loss")
axs[1, 1].set_ylabel("Loss (₹)")

plt.tight_layout()
plt.show()

print("Program executed successfully")




