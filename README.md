# IRR-Calculator


to run test:
`python test.py`
`test.py` imports functions from `irrCalculator.py`
  
### Assumptions
Data on cashflow & initial investment will be received by methods in the form of arrays.  It's assumed that cashflow is already sorted, in ascending order, by date and that initial investment, whose value is negative, is the first element in the array.  

### Limitations
Solution currently works on fixed and changing cash flow but is not ideal in the case of a large number of changing cashflow.  Currently methods require cashflow to be known and entered discretely.  Ideally functionality would be added to allow data to be read from CSV or JSON, so cashflow and initial investment can be extracted by column or keys, and converted to dataframe for sorting.

Solution does not catch the case of multiple IRRS.
