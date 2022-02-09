# Flood risk detection 

Final project for the Building AI course: Flood risk detection

## Summary

Aim is to investigate flood risk in a certain location using machine learning tecnhiques. Results could be used to identify potential flood risk areas, find ways to mitigate
risk in this specific location and possibly find early indicators of increasing risks. Tool could be used to increase discussion about the severity of possible future 
natural catasrofies and have locals identify the risks and possible reguired action to lower the risks before the happen. 


## Background

Flood risks are one of the most common natural disasters and there are indicators that climate change might alter the risks in different areas in the future.
There are already areas in the US where natural catastrophies have become so frequent that the properties in the area have become too expencive to insure due the high risk.
In this case the whole risk of damage stays with the property owners. They are in risk of losing their homes or jobs. Could this have been foreseen? Are there areas in Europe
or possibly in Finland where such change in risk could occur? Is there something that local governments or towns could do to in advance?

Some problems one could possibly investigate:
* What areas are currently high, moderate or low risk areas (in Finland)?
* What indicater could warn us early of a potential flood?


## How is it used?

This approach could provide insurance companies, building companies, banks or even household buyers additional tools evaluating the flood risk of the property the engaging with.
This approach could provide decision makes, whether it is the insurance agends, bank official, retailer or local politician, additional information about the risks in their 
area which they coudl then be aware of in make their decisions based on this information.


## Data sources and AI methods

Insurance companies hold lots of potentially interesting data. Open source data could be available from local metheorological institutes.
Contents and dataformats might vary a lot country by country. 

Interesting data to be considered could be:
* rainfall amounts
* temparature changes
* humidity
* nearby sea level
* snow amount at nearby mountain peaks
* did the flood occur 
* if so how severe it was (increase in water level) 
* how large were the damages (in euros?)

Some methods worth considering could be:
* k-Nearest Neighbours
* Support Vector Machine

## Challenges

It is likely that areas of interest and severity of flood risk are to change due climate change. It might be that ML-approaches might not recognice the slowly occuring changes
in the environment. Also if the process is not transparent is likely that local decision makers can trust the results they are provided? 

From the insurance company perspective, could souch methods be used to price the risk? Are there some concerns related to transperity of the pricing or could the local financial supervicors accept this kind of solution in pricing?

## What next?

Potentially data gathering and searching what kind of open data there is to get started with. Secondly dig up some past flooding data and possibly try to dig up some additional
featuers that could indicate flooding in the future.


## Acknowledgments

* Solvency II -framework (https://www.eiopa.europa.eu/browse/solvency-2_en)
* [Methodological paper on potential inclusion of climate change in the Nat Cat standard formula] (https://www.eiopa.europa.eu/document-library/methodology/methodological-paper-potential-inclusion-of-climate-change-nat-cat_en)

Potentially interesting papers to look at:
* [Machine learning approach for flood risks prediction] (https://ijai.iaescore.com/index.php/IJAI/article/viewFile/20363/12916)
* [Application of machine learning algorithms for flood susceptibility assessment and risk management] (https://iwaponline.com/jwcc/article/12/6/2608/81443/Application-of-machine-learning-algorithms-for)
