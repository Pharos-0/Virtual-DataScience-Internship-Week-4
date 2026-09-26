# Data

`processed/telco_churn_clean.csv` is the cleaned IBM Telco Customer Churn dataset
produced in Week 1 by `src/02_data_cleaning.py`
(https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-1).

| Item | Detail |
|---|---|
| Original source | IBM, https://github.com/IBM/telco-customer-churn-on-icp4d (Apache License 2.0) |
| Rows x columns | 7,043 x 22 (21 original columns + `churn_flag`) |
| SHA-256 | `ec3ef03fbe050a90c06893621f92720beaa3136176ef5e91e1b5fc4d40164fec` |
| Target | `Churn` (Yes/No); `churn_flag` = 1 if Churn is Yes |

`src/data_utils.py` checks the SHA-256 value every time the file is loaded, so
the model is always trained on exactly the Week 1 output.

Cleaning applied in Week 1: the 11 blank `TotalCharges` values (all customers
with `tenure = 0`) were set to 0, `SeniorCitizen` was recoded from 0/1 to No/Yes,
text columns were converted to categories and `churn_flag` was added. No rows
were removed. The full data dictionary and the Apache 2.0 licence text are in
the Week 1 repository (`data/README.md` and `data/raw/`).

IBM describes the dataset as belonging to a fictional telecom company, and
describes churn as the customer leaving within the last month.
