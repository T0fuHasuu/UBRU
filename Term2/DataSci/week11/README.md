# SPSS Guidelines 
### Variables :
- Name **String**
- Width **Numeric**
- Label **String**
- Value **Numeric range**
- Value Declaration **Case**
- Measure 
    + Norminal
    + Ordinal
    + Scale
---

## Check list
### Display Overall 
`Analye > Description Statistics > Frequency`
### Display Crosstab
`Analye > Description Statistics > Crosstab`
### Check for bigger 
`Analyze > Multiple Response Define variable sets`
## Rating Scale
### Calculate general
`Transform > Compute variable`
### Median
`Analyze > Compare Mean > Means`
### Test
`Analyze > Compare Mean > Independent > Sample Test`
### Range
`Analyze > Compare means > One-way ANOVA`

## To Arrange Condition 
```bash
if(variable value condition)Name='Numeric'
if(variable value condition)Name='Numeric'
...
FREQUENCY
VARIABLES = Name
/ORDER ANLYSIS
```

