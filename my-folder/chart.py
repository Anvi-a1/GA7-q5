import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# 1. Generate synthetic business data
# -------------------------------
np.random.seed(42)
n_customers = 200

# CAC typically ranges $50–$500
cac = np.random.uniform(50, 500, n_customers)

# CLV depends positively on CAC but with variability
clv = cac * np.random.uniform(3, 10, n_customers) + np.random.normal(0, 500, n_customers)

# Create customer segments
segments = np.random.choice(['High Value', 'Medium Value', 'Low Value'], size=n_customers, p=[0.3, 0.5, 0.2])

# DataFrame
df = pd.DataFrame({
    'Customer Acquisition Cost (CAC)': cac,
    'Customer Lifetime Value (CLV)': clv,
    'Segment': segments
})

# -------------------------------
# 2. Professional Seaborn styling
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Set2")

# -------------------------------
# 3. Create scatterplot
# -------------------------------
# Ensure exactly 512x512 pixels → 512/64 = 8 inches
plt.figure(figsize=(8, 8), dpi=64)

ax = sns.scatterplot(
    data=df,
    x='Customer Acquisition Cost (CAC)',
    y='Customer Lifetime Value (CLV)',
    hue='Segment',
    palette=palette,
    s=80,
    alpha=0.8,
    edgecolor='k'
)

plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=16, weight='bold')
plt.xlabel("Customer Acquisition Cost (CAC) [$]", fontsize=13)
plt.ylabel("Customer Lifetime Value (CLV) [$]", fontsize=13)

plt.legend(title="Customer Segment", loc="upper left", frameon=True)

# -------------------------------
# 4. Save chart with exact dimensions (no bbox_inches)
# -------------------------------
plt.savefig("chart.png", dpi=64)
plt.close()
