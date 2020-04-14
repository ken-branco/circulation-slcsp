# circulation-slcsp
Circulation Engineering Interview Pre-Work  
Implementation of the [Second Lowest Cost Silver Plan](https://homework.adhoc.team/slcsp/) exercise   

## Development Environment  
Python 3.8.2  
PyCharm Professional 2020.1 

## How to run  
After cloning repo execute this command from root of repo  
```shell script
python ./core/slcsp_by_zip.py
```  

## How to run tests  
Make sure pytest is installed in your environment, run  
```shell script
pip freeze | pytest
```  
You should see output similar to  
```shell script
pytest==5.4.1  
```
If no output from above command, install pytest  

```shell script
pip install pytest
```  
After cloning repo, execute this command from root of repo  

```shell script
pytest ./tests
```  

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
Every zip code can be in 0, 1 or more state areas (counties)  
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
Each state area can have 1 or more Silver Plan rates
```json
{
  "state-area1" : [123.45, 678.90],
  "state-area2" : [345.67, 234.56]
}
```  


