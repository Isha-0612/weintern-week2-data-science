# Retail Sales Analysis and Forecasting
**Ishita Misra · WeIntern Data Science · Week 2**

A reproducible synthetic retail-sales project covering data cleaning, exploratory analysis, and one-day-ahead completed-order sales prediction.

## Repository layout
| Path | Purpose |
|---|---|
| `data/raw/` | Original synthetic CSV (unchanged) |
| `data/processed/` | Cleaned CSV and separate encoded copy |
| `notebooks/Week2_Task1.ipynb` | Cleaning, validation, encoding, exports |
| `notebooks/Week2_Task2.ipynb` | EDA, six chart types, computed insights |
| `notebooks/Week2_Task3_Sales_Prediction.ipynb` | Baselines, ML, time-series tuning, final evaluation |
| `reports/cleaning/` | Cleaning report, quality comparison, outlier summary |
| `reports/eda/` | Grouped summaries and written insights |
| `reports/model/` | Validation/test comparison, predictions, importance |
| `reports/figures/` | Exported figures |
| `reports/*.pdf` | Readable exports of all three executed notebooks |
| `docs/` | Handbook, submission checklist, review notes |
| `scripts/` | Reproduction and validation commands |

## Run locally
Use Python 3.11 or newer. Extract the ZIP or clone the repository, then open a terminal at the project root.

```bash
python -m pip install -r requirements.txt
python scripts/run_notebooks.py
python scripts/validate_submission.py
```

Alternatively launch `jupyter notebook` from the root and run Tasks 1, 2, and 3 in that order. Each notebook can locate the root from either the root folder or `notebooks/`. Outputs are written to the paths in the table above.

## Run in Google Colab
Extract the complete folder to `MyDrive/retail-sales-week2`. Open each notebook in Colab, add a temporary first cell with:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Then run Tasks 1 → 2 → 3. The notebooks detect `/content/drive/MyDrive/retail-sales-week2` automatically. Opening the ZIP alone without extracting it is insufficient.

## Verified results
- Original data: 12,185 rows × 21 columns.
- Corrected clean data: 11,923 rows × 21 columns; no missing values, exact duplicates, or repeated order IDs.
- Product-name whitespace is standardized; five previously retained duplicate transactions are removed.
- EDA includes histograms/KDE, a correlation heatmap, bar charts, box plots, monthly lines, scatter plots, status-aware totals, and four computed action points.
- Task 3 uses chronological 80/20 splitting and expanding-window GridSearchCV on training days only. All candidate selection uses mean validation-fold RMSE. The test set is reserved for final reporting.
- Validation selects the training-mean benchmark. Test RMSE: 179,908.09; MAE: 134,709.96; R²: -0.0049.
- Best validation-selected ML candidate: Tuned Ridge. Its test R² is -0.0082. The ML methods do not beat the selected simple benchmark on this test period.

## Interpretation and limitations
This synthetic dataset is for practice. Negative R² is reported honestly. The workflow is complete, but useful forecasting skill and operational readiness are not established. Do not describe the constant benchmark as a trained ML model; the notebook also trains and evaluates Linear Regression, Ridge, Random Forest, and Gradient Boosting.

One-day-ahead test predictions use observed sales through the preceding day. This is not a multi-day forecast from a single starting date. Missing calendar days are zero-filled as an explicit assumption. Sales outliers are retained. IQR capping of price and quantity can break arithmetic relationships with recorded sales/profit, which are not recomputed. Forecasting uses recorded sales history, not price/quantity-derived targets or profit.

EDA totals across all statuses are recorded transaction amounts, not net accounting revenue. Unknown regions are not ranked as geographic regions. No causal effects are claimed.
