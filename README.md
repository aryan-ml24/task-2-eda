# Task 2 — Exploratory Data Analysis (EDA)

## Objective
Understand a dataset using statistics and visualizations.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

## Dataset
The project uses Plotly's built-in **Tips** dataset and includes the exact CSV in `data/tips.csv`.

**Rows:** 244  
**Columns:** 7

### Columns
`total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size`

## EDA performed
1. Dataset shape and structure
2. Data types
3. Missing-value and duplicate checks
4. Descriptive statistics
5. Median and skewness
6. Histograms
7. Boxplots and outlier inspection
8. Correlation matrix / heatmap
9. Feature relationship analysis
10. Feature-level conclusions

## Main observations
- Total bill and tip show a positive correlation of **0.68**.
- Total bill and party size show a positive correlation of **0.60**.
- Average tip at dinner is **$3.10**, compared with **$2.73** at lunch.
- The dataset contains **0 missing values**.
- Boxplots help flag unusually high or low observations; these should be investigated rather than automatically deleted.
- Correlation indicates association, not causation.

## Outputs
The `outputs/` folder contains:
- Numeric distributions
- Boxplots
- Correlation heatmap
- Tip vs total bill
- Total bill by day
- Tip by meal time and sex

## Run locally
```bash
pip install -r requirements.txt
python eda_tips.py
```

Open `task2_eda.ipynb` in Jupyter or VS Code for the complete step-by-step EDA.

## Interview Questions

### 1. What is the purpose of EDA?
EDA helps understand data quality, distributions, relationships, outliers, and patterns before machine-learning modeling.

### 2. How do boxplots help?
They show the median, quartiles, spread, and potential outliers, making it easy to compare distributions.

### 3. What is correlation and why is it useful?
Correlation measures the strength and direction of a linear relationship between two numeric variables. It is useful for identifying related features, but correlation does not prove causation.

### 4. How do you detect skewness?
Use histograms, boxplots, and a numerical skewness measure such as `Series.skew()`.

### 5. What is multicollinearity?
It is strong dependence among predictor variables. It can make regression coefficients unstable and harder to interpret. Correlation matrices and VIF are common diagnostics.

### 6. What tools do you use for EDA?
Pandas and NumPy for data work; Matplotlib and Seaborn for visualization; Plotly for interactive charts.

### 7. Can you explain a time when EDA helped find a problem?
For example, a boxplot can reveal extreme observations and a missing-value check can reveal incomplete records before model training. EDA lets us investigate these issues before they affect a model.

### 8. What is the role of visualization in ML?
Visualization helps identify distributions, relationships, anomalies, and possible feature-engineering opportunities, and makes findings easier to communicate.

## GitHub submission
Create a new GitHub repository named something like `task-2-eda`, upload this entire project, and submit the repository URL in the internship submission form.
