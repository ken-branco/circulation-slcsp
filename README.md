# circulation-slcsp
Circulation Engineering Interview Pre-Work  

Since the plan and zip data are large, we'll iterate over them just  
once and store them in dictionary for fast lookups later on. 

# Algorithm for Second Lowest Cost Sliver Plan (SLCSP)

1. for each zip in slcsp.csv
2. find all states/areas for zip
3. for each state/area in zip, gather all silver rates
4. determine 2nd lowest rate
5. add 2nd lowest rate to zip

# Data Structures  
zip_rate 
zip code and Second Lowest Cost Silver Plan (SLCSP)  
```json
{
  "zip_code" : 123.45
}
```
zip_state_area  
source: zips.csv  
Every zip code can be in 1 or more state areas (counties)  
```json
{
  "zip_code" : [
      "state-area1",
      "state-area2",
      "state-area3"
  ]
}
```  

state_area_rate  
source: plans.csv    
Each state area should have just 1 Silver Plan Rate
```json
{
  "state-area1" : 123.45,
  "state-area2" : 678.90
}
```  


