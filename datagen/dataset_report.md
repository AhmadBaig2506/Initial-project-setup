# Dataset report

Label files: 27. Topics retrieved: 480.

| Split | Items | answerable | partial | unanswerable | seed | gen | hard_neg | partial (type) | offtopic_neg |
|---|---|---|---|---|---|---|---|---|---|
| train | 1579 | 849 | 151 | 579 | 427 | 431 | 432 | 146 | 143 |
| val | 87 | 48 | 7 | 32 | 24 | 24 | 24 | 7 | 8 |
| test | 87 | 46 | 9 | 32 | 24 | 24 | 24 | 7 | 8 |

`test_v2.jsonl` = 87 new test items + 27 baseline items = 114.

Rejected: 6

| Reason | Count |
|---|---|
| answer shares no key words with the question | 4 |
| 1 uncited sentence(s) | 1 |
| duplicate question | 1 |

Answer length (train+val, non-refusal): mean 56 words, max 90.
