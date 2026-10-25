# Retail Sales Analysis and Forecasting
**Ishita Misra · WeIntern Data Science · Week 2**

A synthetic retail-sales project covering data cleaning, exploratory data analysis, and one-day-ahead completed-order sales prediction.

## Repository contents

Folder names are case-sensitive. The current repository uses the following layout:

| Path | Contents |
|---|---|
| `Data/Raw/retail_sales_raw.csv` | Original synthetic transactions |
| `Data/Processed/` | Uploaded cleaned and encoded CSV snapshots; see the consistency note below |
| `Notebooks/Week2_Task1.ipynb` | Cleaning, whitespace normalization, duplicate removal, validation, and encoding |
| `Notebooks/Week2_Task2.ipynb` | Statistics, distributions, category/region comparisons, trends, and insights |
| `Notebooks/Week2_Task3_Sales_Prediction.ipynb` | Historical benchmarks, regression models, time-series tuning, and evaluation |
| `Reports/` | PDF exports, cleaning report, data-quality comparison, outlier summary, and EDA insights |
| `Model Outputs/` | Saved evaluation tables, predictions, feature importance, and evaluation summary |
| `Docs/` | Assignment handbook, data dictionary, and review notes |
| `Scripts/` | Notebook runner and submission validator; currently written for the original lowercase layout |
| `requirements.txt` | Python dependencies |

## Current consistency status

The three notebooks contain saved execution results and no recorded execution errors. Task 3 includes `GridSearchCV` and Random Forest feature importance.

However, the repository is not yet fully consistent for a fresh checkout:

- The uploaded `Data/Processed/retail_sales_cleaned.csv` is still the older **11,928-row** snapshot. The corrected notebook run and reports describe **11,923 rows** after trimming product-name whitespace and removing five additional repeated transactions.
- The notebooks look for lowercase `data/raw/` and `data/processed/`, and write results to lowercase `reports/`. Those paths differ from the capitalized upload folders.
- `Scripts/run_notebooks.py` searches lowercase `notebooks/`, while the uploaded folder is `Notebooks/`. `Scripts/validate_submission.py` also expects the original lowercase directory structure.
- The root-level `run_notebooks.py` is a duplicate with an incorrect root calculation for its current location. Do not use it.
- `Data/Processed/retail_sales_encoded.csv` is now present. Regenerate it together with the final cleaned CSV in Task 1 so both files correspond to the same run.

Use the reproduction procedure below to generate a consistent working dataset and fresh results. Before submission, replace the older uploaded cleaned CSV with the regenerated version and ensure that notebooks, reports, PDFs, and CSVs refer to the same run.

## Reproduce locally

Use Python 3.11 or newer. Clone the repository, enter its root folder, and install the dependencies:

```bash
git clone https://github.com/Isha-0612/weintern-week2-data-science.git
cd weintern-week2-data-science
python -m pip install -r requirements.txt
```

The following Python block accommodates the current capitalized upload layout without editing the notebooks. Run it from the repository root, either in a Python session or as a temporary local script:

```python
from pathlib import Path
import shutil
import nbformat
from nbclient import NotebookClient

root = Path.cwd()
source = root / "Data/Raw/retail_sales_raw.csv"
if not source.is_file():
    raise FileNotFoundError("Run this from the repository root.")

# Prepare the lowercase paths expected by the notebooks.
(root / "data/raw").mkdir(parents=True, exist_ok=True)
(root / "data/processed").mkdir(parents=True, exist_ok=True)
target = root / "data/raw/retail_sales_raw.csv"
if source.resolve() != target.resolve():
    shutil.copy2(source, target)

# Execute the actual uploaded notebooks in dependency order.
names = [
    "Week2_Task1.ipynb",
    "Week2_Task2.ipynb",
    "Week2_Task3_Sales_Prediction.ipynb",
]
for name in names:
    path = root / "Notebooks" / name
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(
        notebook,
        timeout=1200,
        kernel_name="python3",
        resources={"metadata": {"path": str(root)}},
    ).execute()
    nbformat.write(notebook, path)
    print("Executed", name)
```

This prepares and executes the workflow; it does not replace the older capitalized CSV uploads or regenerate PDF exports automatically. On a case-sensitive filesystem, the newly created lowercase folders are separate from the capitalized folders. On a case-insensitive filesystem, they may resolve to the same folders.

### Generated outputs

| Path | Generated contents |
|---|---|
| `data/processed/` | Corrected cleaned CSV and separate one-hot encoded CSV |
| `reports/cleaning/` | Cleaning report, before/after quality table, and IQR outlier summary |
| `reports/eda/` | Statistical tables, grouped summaries, and computed insights |
| `reports/model/` | Validation/test comparisons, tree importance, predictions, and evaluation summary |

Check the regenerated data:

```python
import pandas as pd

df = pd.read_csv("data/processed/retail_sales_cleaned.csv")
assert df.shape == (11923, 21)
assert not df.isna().any().any()
assert not df.duplicated().any()
assert not df["order_id"].duplicated().any()
assert df["product_name"].eq(df["product_name"].str.strip()).all()
print("Cleaned data checks passed.")
```

For manual exploration, launch `jupyter notebook` from the root and run Tasks 1 → 2 → 3 after preparing the lowercase data paths above.

## Google Colab

Extract or clone the complete repository into Drive. Mount Drive, change the working directory to the actual repository root, and prepare the lowercase raw/processed paths as above. Then run Tasks 1 → 2 → 3. The working directory must contain `data/raw/retail_sales_raw.csv` for notebook root detection to succeed.

Do not assume that opening an individual notebook also makes its datasets available. All required files must be accessible in the same project tree.

## Results from the corrected run

The following figures describe the corrected **11,923-row** run, not the older uploaded cleaned CSV:

| Measure | Result |
|---|---:|
| Raw dimensions | 12,185 rows × 21 columns |
| Corrected cleaned dimensions | 11,923 rows × 21 columns |
| Remaining missing cells | 0 |
| Remaining exact duplicate rows | 0 |
| Remaining repeated order IDs | 0 |
| Validation-selected overall benchmark | Training mean |
| Benchmark test MAE | 134,709.96 |
| Benchmark test RMSE | 179,908.09 |
| Benchmark test R² | −0.0049 |
| Best validation-selected ML candidate | Tuned Ridge |
| Tuned Ridge test R² | −0.0082 |

Task 2 includes histograms/KDE, a correlation heatmap, bar charts, box plots, monthly line charts, scatter plots, and computed recommendations.

Task 3 trains Linear Regression, Ridge, Random Forest, and Gradient Boosting, alongside historical benchmarks. It uses a chronological 80/20 split and expanding-window `GridSearchCV` within the training period. Candidate selection uses mean validation-fold RMSE; the test period is reserved for final reporting. Tuning scores are model-selection estimates rather than independent performance estimates.

## Interpretation and limitations

- The selected training-mean benchmark is a simple historical reference, not a trained ML model. The trained candidates do not beat it on this test period.
- Negative R² is reported honestly. Useful forecasting skill and operational readiness are not established.
- Test predictions use sales observed through the preceding day. This is a rolling one-day-ahead evaluation, not a multi-day forecast from one starting date.
- Missing calendar dates are represented as zero sales under an explicit assumption.
- Sales outliers are retained. Independent IQR capping of price and quantity can break arithmetic relationships with recorded sales/profit, which are not recomputed.
- Profit is excluded as a forecasting predictor to avoid target leakage.
- EDA totals across all order statuses are recorded transaction amounts, not net accounting revenue. Unknown regions are excluded from geographic rankings.
- Findings are descriptive and do not establish causal effects.

## Submission review

Use the assignment handbook in `Docs/` as the submission reference. Include the notebooks, original and final cleaned datasets, cleaning report, before/after comparison, PDF exports, and README. Refresh PDF exports if the notebooks or results change.

The handbook describes real-world data; this project uses synthetic practice data. Confirm that the dataset source is accepted, review the implementation, and be prepared to explain the analysis and its limitations.
