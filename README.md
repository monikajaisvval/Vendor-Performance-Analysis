# 📊 Vendor Performance Analysis

## 📌 Project Overview

The Vendor Performance Analysis project focuses on evaluating vendor efficiency, profitability, inventory utilization, and sales performance to support data-driven business decisions.

Using SQL, Python, and Power BI, this project integrates multiple inventory and sales datasets to uncover hidden patterns, identify business risks, and recommend strategies for improving profitability and operational efficiency.

---

## 🎯 Business Problem

Retail and wholesale organizations often struggle with:

- Excess inventory and slow-moving stock.
- Over-dependence on a few vendors.
- Inefficient pricing strategies affecting profitability.
- Difficulty identifying high-performing and underperforming vendors.

The objective was to analyze vendor, inventory, and sales data to optimize purchasing decisions, reduce inventory costs, and improve profitability. :contentReference[oaicite:0]{index=0}

---

## 📂 Dataset Information

### Dataset Size

The analysis was performed on **2.8+ million transactional records** collected from multiple business datasets:

| Dataset | Records |
|----------|---------|
| Purchases | 2,372,474 |
| Begin Inventory | 206,529 |
| End Inventory | 224,489 |
| Purchase Prices | 12,261 |
| Vendor Invoice | 5,543 |
| Vendor Sales Summary | 10,692 |

---

## 🛠️ Tools & Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **SciPy**
- **SQLite / SQL**
- **SQLAlchemy**
- **Power BI**
- **Jupyter Notebook**

---

## ⚙️ Project Workflow

1. Loaded and integrated multiple CSV datasets into SQLite database.
2. Performed data cleaning and preprocessing.
3. Created vendor summary tables using SQL joins and aggregations.
4. Engineered business metrics including:
   - Gross Profit
   - Profit Margin
   - Stock Turnover
   - Sales-to-Purchase Ratio
5. Conducted Exploratory Data Analysis (EDA).
6. Performed statistical hypothesis testing.
7. Built an interactive Power BI dashboard.

---

## 📊 Dashboard Preview

![Vendor Performance Dashboard](images/dashboard.png)

---

## 🔍 Key Business Questions Answered

- Which vendors contribute the most to sales and profitability?
- Which brands require promotional or pricing adjustments?
- How does bulk purchasing impact unit costs?
- Which vendors exhibit low inventory turnover?
- Is there a statistically significant difference between high- and low-performing vendors?

---

## 💡 Key Insights

### 1. Vendor Dependency Risk

The top 10 vendors account for **65.69% of total purchases**, indicating excessive dependence on a small vendor base and potential supply chain risks. :contentReference[oaicite:1]{index=1}

### 2. Inventory Optimization Opportunity

The business holds approximately **$2.71M in unsold inventory capital**, negatively impacting cash flow and storage costs. :contentReference[oaicite:2]{index=2}

### 3. Pricing & Promotion Opportunities

Identified **198 brands** with low sales but high profit margins, making them ideal candidates for targeted promotions and pricing optimization. :contentReference[oaicite:3]{index=3}

### 4. Bulk Purchasing Advantage

Large-volume purchases reduced unit costs by approximately **72%**, demonstrating significant cost-saving opportunities through bulk procurement. :contentReference[oaicite:4]{index=4}

### 5. Inventory Efficiency

A near-perfect correlation (**0.999**) between purchase quantity and sales quantity confirmed effective inventory movement for most products. :contentReference[oaicite:5]{index=5}

---

## 📈 Quantifiable Outcomes

✅ Identified **$2.71M** worth of slow-moving inventory.

✅ Discovered that **10 vendors contribute 65.69%** of total purchases.

✅ Uncovered **198 underperforming brands** requiring pricing or marketing intervention.

✅ Demonstrated **72% lower unit cost** through bulk purchasing strategies.

✅ Statistically validated significant profit margin differences between top and low-performing vendors using hypothesis testing. :contentReference[oaicite:6]{index=6}

---

## 🚀 Business Recommendations

- Diversify vendor partnerships to reduce supply chain risk.
- Optimize slow-moving inventory through promotions and revised purchasing strategies.
- Leverage bulk purchasing discounts for cost reduction.
- Improve marketing efforts for low-performing vendors.
- Reassess pricing strategies to maximize profitability. :contentReference[oaicite:7]{index=7}

---

## 👩‍💻 Author

**Monika Jaiswal**

- GitHub: https://github.com/monikajaisvval
- LinkedIn: https://www.linkedin.com/in/monika-jaisvval

---

⭐ If you found this project useful, please give it a star.