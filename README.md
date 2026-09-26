# Virtual DataScience Internship - Week 4

## Machine Learning Model Development and Evaluation

Week 4 of the Virtual Data Science with Python Apprentice Internship. A classifier
that predicts customer churn is built, evaluated and diagnosed. It uses the data
cleaned in Week 1 and the findings of Weeks 2 and 3.

| Week | Repository |
|---|---|
| 1 | [Virtual-DataScience-Internship-Week-1](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-1): data acquisition, cleaning and EDA |
| 2 | [Virtual-DataScience-Internship-Week-2](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-2): visualization and storytelling |
| 3 | [Virtual-DataScience-Internship-Week-3](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-3): hypothesis testing |
| **4** | **Machine learning (this repository)** |
| 5 | [Virtual-DataScience-Internship-Week-5](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-5): final project |

## Dataset

The cleaned **IBM Telco Customer Churn** dataset: 7,043 customers, target `churn_flag` (26.5%
positive), checksum verified on load. Original source:
[IBM/telco-customer-churn-on-icp4d](https://github.com/IBM/telco-customer-churn-on-icp4d) (Apache 2.0).

## Method

- **Features:** 16 categorical variables (one-hot encoded, first level as reference) and numeric
  `tenure`, `MonthlyCharges` and `log_tenure` (standardised). `customerID` and the text target are
  excluded, and "No internet/phone service" labels are recoded to "No".
- **Feature selection:** 5-fold CV ROC-AUC on the training set only. Adding `log_tenure` raised it
  from 0.846 to 0.850. Dropping `TotalCharges` (r = 0.83 with tenure) made no difference.
- **Split:** stratified 80/20 (5,634 / 1,409 rows), `random_state = 42`. The test set was used once.
- **Leakage prevention:** all preprocessing sits inside a scikit-learn `Pipeline` / `ColumnTransformer`,
  so it is fitted on the training folds only.
- **Models:** majority-class baseline, **logistic regression** (main model), logistic regression with
  balanced class weights, and a decision tree tuned by grid search (`max_depth = 6`,
  `min_samples_leaf = 50`).
- **Threshold:** 0.34, chosen by maximum out-of-fold F1 on the training set.

## Results (held-out test set, n = 1,409)

| Model | Threshold | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|---|
| Baseline (always "no churn") | 0.50 | 0.735 | 0.000 | 0.000 | 0.000 | 0.500 |
| Logistic regression | 0.50 | 0.805 | 0.668 | 0.527 | 0.589 | 0.848 |
| **Logistic regression** | **0.34** | 0.780 | 0.567 | **0.727** | **0.637** | 0.848 |
| Logistic regression (balanced) | 0.50 | 0.740 | 0.507 | 0.797 | 0.620 | 0.848 |
| Decision tree (tuned) | 0.50 | 0.800 | 0.709 | 0.417 | 0.525 | 0.828 |

- Accuracy alone is misleading here: the baseline reaches 73.5% while catching no churners.
- Logistic regression shows almost no train/validation gap (CV ROC-AUC 0.850 vs training 0.854) and is
  well calibrated.
- The model is weakest for churners on longer contracts and with long tenure, where churn is rare.
- The largest odds ratios are two-year contract 0.20 and one-year 0.49 (vs month-to-month), fibre optic
  3.04 (vs DSL), and 0.44 per SD of `log_tenure`.

## Repository structure

```
|-- README.md
|-- requirements.txt
|-- data/
|   |-- README.md
|   `-- processed/telco_churn_clean.csv     # Week 1 output (checksum verified)
|-- notebooks/
|   |-- Week_4_Churn_Model.ipynb            # executed notebook (same code as src/)
|   `-- build_notebook.py
|-- src/
|   |-- config.py  data_utils.py  plot_style.py
|   `-- 06_modeling.py
|-- outputs/
|   |-- figures/   # confusion matrices, ROC/PR curves, threshold analysis, learning curves,
|   |              # calibration, odds ratios, error analysis (fig4_1 ... fig4_6)
|   |-- tables/    # CV results, test metrics, coefficients, error tables, test-set predictions
|   |-- models/    # fitted logistic-regression pipeline + threshold (joblib)
|   `-- results/model_results.json
`-- screenshots/   # 11 screenshots of the executed notebook
```

## How to reproduce

Tested with Python 3.11.9 (scikit-learn 1.9.1, pandas 3.0.6, NumPy 2.4.6, joblib 1.6.0).

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python src/06_modeling.py            # training, CV, test evaluation, figures, tables (< 1 minute)
python notebooks/build_notebook.py   # optional: rebuild and execute the notebook
```

The split, the cross-validation folds and the decision tree all use `random_state = 42`, so
results are reproducible. Load the saved model with the same scikit-learn version.

## Notebook and screenshots

`notebooks/Week_4_Churn_Model.ipynb` is built from `src/06_modeling.py` (Jupytext percent format)
and executed, so it contains the same code. The images in `screenshots/` are crops of the
executed notebook (pipeline, training output, metrics, confusion matrix, ROC curve, diagnostics).

## Limitations

- One snapshot of a fictional company (per IBM). Performance on real customers, or over time, is untested.
- Coefficients describe associations, not causal effects. `MonthlyCharges` largely reflects the
  services a customer buys, so the price and service coefficients are entangled.
- Only two model families were compared. Other algorithms are untested.

The written report for this week is submitted separately through the internship portal.
