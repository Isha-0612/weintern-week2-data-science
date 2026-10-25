# Review notes

All three notebooks were executed sequentially against the supplied raw CSV on 25 October 2026. No execution errors occurred. Raw bytes are preserved. After whitespace normalization and final duplicate removal, the cleaned dataset has 11,923 rows. Summary checks require zero missing cells, exact duplicates, and repeated order IDs.

The previous EDA PDF had horizontal clipping. These PDF exports wrap source and table text and scale figures within the page. Notebook outputs use text tables and embedded figures.

The final model benchmark has test R² -0.0049. This is not a successful operational forecast; it is a reproducible negative result. Models and targets were not changed to manufacture a positive score. Time-series CV scores used for tuning are not independent accuracy estimates. Test metrics are the independent historical evaluation.

Synthetic-data acceptance and the handbook's original-work expectations remain the student's responsibility to confirm and understand. AI-assisted code should be reviewed and disclosed where required by the course.
