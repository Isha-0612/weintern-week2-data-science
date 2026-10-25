# Retail Sales Data Cleaning Report

## Dataset overview
- Raw dimensions: 12,185 rows × 21 columns
- Final cleaned dimensions: 11,923 rows × 21 columns

## Cleaning actions
- Exact duplicate rows removed before cleaning: 120
- Additional exact duplicates removed after outlier capping: 65
- Missing sales rows excluded rather than imputing the target: 72
- Rows with missing/unparseable dates excluded: 5
- Invalid transaction rows excluded: 0
- Invalid discounts corrected to the median of valid discounts: 1
- Missing categorical values filled with `unknown`.
- Missing numeric values filled with column medians where needed.
- Product names and identifiers trimmed; exact duplicates rechecked after normalization and capping.
- Column names standardized to lowercase snake_case; dates and numeric columns converted to appropriate types.
- IQR outlier detection performed for quantity, unit_price, discount, sales, and shipping_cost.
- Values capped: quantity=96, unit_price=1,151, shipping_cost=0. Sales outliers were retained for review.
- Categorical variables one-hot encoded in a separate output file.

## Validation
- Remaining duplicate rows: 0
- Remaining missing cells: 0
- Discounts outside [0, 1]: 0
- Non-positive quantities: 0
- Ship date before order date: 0

## Output files
- `retail_sales_cleaned.csv`: cleaned dataset with readable category labels
- `retail_sales_encoded.csv`: one-hot encoded copy
- `data_quality_before_after.csv`: before/after quality comparison
- `outlier_detection_summary.csv`: IQR fences and outlier counts

## Notes
- IQR outliers are statistical flags, not proof of errors. Sales outliers were retained because they may be legitimate transactions.
- This is a synthetic practice dataset; for real data, confirm cleaning decisions with a data owner.
- Do not use `profit` to predict `sales`, because profit is derived from sales and can cause target leakage.
