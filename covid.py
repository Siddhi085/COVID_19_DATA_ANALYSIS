import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(r"C:\Users\Diya\Downloads\COVID19_YSM_DATA_ANALYSIS\covid19_sample_data.xlsx", engine="openpyxl")

print("File loaded:", df.shape)

# Cleaning
df.columns = df.columns.str.strip().str.lower()
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

df["date"] = df["date"].dt.strftime('%Y-%m-%d')


# Step 3️⃣: Save cleaned dataset automatically
cleaned_file_path = r"C:\Users\Diya\Downloads\COVID19_YSM_DATA_ANALYSIS\covid19_cleaned_data.xlsx"
df.to_excel(cleaned_file_path, index=False)
print(f"Cleaned file saved at: {cleaned_file_path}")


# --------------------
# 1. Bar Chart: Total cases per country
total_cases_country = df.groupby("country")["total cases"].max().sort_values(ascending=False)

plt.figure(figsize=(10,6))
total_cases_country.plot(kind="bar", color="skyblue")
plt.title("Total COVID-19 Cases by Country (Bar Chart)")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# --------------------
# 2. Line Chart: New cases over time
new_cases_time = df.groupby("date")["new cases"].sum()

plt.figure(figsize=(12,6))
new_cases_time.plot(kind="line", marker='o', color="orange")
plt.title("Daily New COVID-19 Cases Over Time (Line Chart)")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.grid(True)
plt.show()

# --------------------
# 3. Histogram: Distribution of New Cases
plt.figure(figsize=(10,6))
df["new cases"].plot(kind="hist", bins=30, color="pink")
plt.title("Distribution of New COVID-19 Cases (Histogram)")
plt.xlabel("New Cases")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# --------------------
# 4. Pie Chart: Top 5 Countries by Total Cases
top5_countries = total_cases_country.head(5)

plt.figure(figsize=(8,8))
top5_countries.plot(kind="pie", autopct='%1.1f%%', startangle=140, shadow=True)
plt.title("Top 5 Countries by Total COVID-19 Cases (Pie Chart)")
plt.ylabel("")
plt.show()

# --------------------
# 5. Scatter Plot: Total Cases vs Population
plt.figure(figsize=(10,6))
plt.scatter(df["population"], df["total cases"], alpha=0.5, color='purple')
plt.title("Total Cases vs Population (Scatter Plot)")
plt.xlabel("Population")
plt.ylabel("Total Cases")
plt.grid(True)
plt.show()

# --------------------
# 6. Top 10 Countries by Total Cases on Latest Date (New Requirement)
latest_date = df['date'].max()
latest_data = df[df['date'] == latest_date]

top10_cases = latest_data.sort_values('total cases', ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top10_cases['country'], top10_cases['total cases'], color='teal')
plt.title(f"Top 10 Countries by Total Cases on {latest_date}")

plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
