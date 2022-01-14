# Challenge description

It is April 2020 and COVID testing is just being rolled out. You are working for NHS Digital in partnership with your local hospital trust to collect data about the daily number of new COVID cases and patients in various categories of care.

At the end of each day the hospital staff submit to you a daily report, given as an array of strings representing `Cases`, `Isolating Patients`, `Patients In Care` and `ICU Patients` as explained below:

- `Cases`: Integer of total cases that day, which is calculated as a sum of `Isolating` and `In Care` patients
- `Isolating`: Integer of patients believed to have COVID that are isolating at home. Does not include `In Care` or `ICU` patients.
- `In Care`: Integer of patients believed to have COVID that are currently in hospital. Includes `ICU` patients.
- `ICU`: Integer of people in intensive care. This is always represented as a subset of `In Care` patient numbers.

You must write a method which will take this reporting data and produce an array of integer values representing the number of patients in each category

IMPORTANT: Wherever possible, your solution should attempt to calculate any missing, anomalous or incorrectly entered data based off data which is present.

For example: `["80", "-", "50", "25"]` should return `[80, 30, 50, 25]` as `Cases` is always the sum of `Isolating` and `In Care` patients.

If it is not possible to recover data in this way, or if the total `Cases`  are not equal to the sum of `Isolating` plus `In Care`, the method should record the value for any affected categories of patient as 0.

## Assumptions

- Max integer values - this method is being written for use in individual hospitals, and so the max integer value for any entries will not exceed twenty thousand (20000).
- Any values given as a percentage will always work out to a whole integer value: you will not need to deal with 1/3rd of a patient!
- Any time the `ICU` value is expressed as a percentage, it is representing a percentage of the `In Care` value, and not the `Cases` value.
## Things to consider

### Incorrect data entry
Because of the human element involved in this process data is often collected in varied ways. This may be data entered as a percentage instead of an integer, data entered which is invalid or nonsensical, or data which has simply been omitted. Consider the examples below:

- Some staff give values as a percentage instead of as an integer, represented by `%` immediately after the data value or as a decimal, represented as `0.XX`.
- For example: `["60", "60%", "26", "22"]` - this should return `[60, 36, 26, 22]`.
- This is because percentage is converted to an integer ( `Isolating` patients are always a subset of `Cases`).
- Similarly `["60", "0.6", "26", "22"]` or `["60", "0.60", "26", "22"]` should return `[60, 36, 26, 22]` for exactly the same reason.
- Finally, some hospital staff are treating the number of patients `In Care` and `ICU` exclusively, which is incorrect: `ICU` is a proportion of the `In Care` patient numbers.
- For example: `["60", "36", "4", "20"]` - this should return `[60, 36, 24, 20]`.
- This is because the `ICU` integer must be smaller than the `In Care` integer. Where they are recorded exclusively, `ICU` should be added to the `In Care` value.

### Anomalous data entry 
Sometimes the numbers recorded are valid as integers, but are not consistent with the breakdown of cases by patient category. These kinds of results are anomalous data and should be handled by treating the individual value as zero. Consider the examples below:

- For example: `["50", "70", "5", "2"]` - will return `[50, 0, 5, 2]`.
- This is because the `Isolating` value is a subset of the `Cases` value and so cannot be higher than the `Cases` value.
- Similarly `["50", "70", "80", "8"]` will return `[50, 0, 8, 8]`. 
- This is because the `Isolating` and `In Care` values are both anomalous as they cannot be higher than the `Cases` value cumulatively or individually.
- However, the value for `In Care` can be updated to reflect the fact that `ICU` must be smaller than `In Care`.
- Finally consider: `["60", "36", "10", "20"]` - this should return `[60, 36, 0, 20]`.
- This is because the `In Care` integer has been corrected (as it is smaller than the `ICU` value) and would have been 30.
- This makes the value `In Care`  too large to be correct (as `In Care` should equal `Cases` minus `Isolating`) and so is recorded as 0.
- This is the only example of a time when `In Care` may be lower than `ICU`.


### Missing data entry 
Occasionally some data is missing and is recorded as anything other than a percentage, a decimal or an integer, which may include letters, numbers, and/or symbols. Consider the below:

- Data may have been entered as 0, however it may also have been entered as "none", "unknown", "n/a" or similar.
- For example: `["55", "55", "n/a", "0"]` - this should return `[55, 55, 0, 0]`.
- Additionally sometimes data is simply not recorded. When this happens you should take the values given in the order they are presented (i.e. : the first value is always `Cases`, etc).
- For example: `["50", "50", "0"]` - this should be treated as `[50, 50, 0, 0]` representing the lack of info provided in the report.

It is up to you to take each daily report and ensure that all the values are numerical and represent the correct number of patients so that they can be added to a database in future.