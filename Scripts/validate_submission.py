"""Check data and required deliverables; no files are modified."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/processed/retail_sales_cleaned.csv')
assert not df.isna().any().any()
assert not df.duplicated().any()
assert not df.order_id.duplicated().any()
assert df.product_name.eq(df.product_name.str.strip()).all()
assert df.discount.between(0,1).all()
assert (df.quantity>0).all()
for path in (ROOT/'notebooks').glob('*.ipynb'):
    notebook=json.loads(path.read_text())
    for cell in notebook['cells']:
        if cell['cell_type']=='code' and ''.join(cell['source']).strip():
            assert cell['execution_count'] is not None, path.name
            assert all(o.get('output_type')!='error' for o in cell['outputs'])
for name in ['README.md','requirements.txt','reports/cleaning/data_cleaning_report.md','reports/cleaning/data_quality_before_after.csv','reports/Week2_Task2.pdf','reports/model/model_evaluation_comparison.csv']:
    assert (ROOT/name).is_file(),name
print(f'PASS: {len(df):,} clean rows; notebook outputs and required files present.')
