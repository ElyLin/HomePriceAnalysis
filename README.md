# Home Prices Analysis King County, Washington
### By: Wayne Harrison, Ely Lin, Brooke Smyth
## Introduction
The Bank of Seattle is going through a major tech transformation and would like to have a predictive model of housing
prices in King County. The goal of this analysis is to inform the bank which housing features have the biggest impact
on the value of a house.
## Business Understanding
__Stakeholder:__  Bank of Seattle\
__Problem:__  Before a bank can agree to handing out a mortgage, they want to make sure that the client is buying a 
home that has a value equal to or greater than the value of the requested mortgage, due to the unfortunate possibility
that the client would not be able to pay all of their mortgage payments, in which case the bank would take the house 
as collateral.\
__Subproblem:__ Houses have numerous features so it is dfficult to narrow down which exact features result in higher 
priced homes.\
__Assumptions:__ 
- The size of a house has a positive linear relationship with price.

- The better the condition of a house is, the more valuable it will be.
## Data Understanding
For this analysis, we will use a csv file which contains data about the features and sale prices of homes in King County.
As we looked through the data, we discovered that the dataset contains 21,597 records with 21 different features, which 
describe the different characteristics of the houses in King County, such as square footage, whether or not there is a good
view, etc.
## Modelling
For this project, we conducted several linear and multiple linear regressions to determine which features of homes had the
highest impact on the sale price of the home. For each regression, we looked at the R2 value, error measurements, multicollinearity of features, and other metrics which reflected the quality of our regression. 
## Regression Results
The model which yielded the best regression results was a multiple linear regression model which contained various features,
of which the most impactful were distance from Bellevue (a high-demand living area close to Seattle), grade of home (quality of
construction), and square-footage of home. This model was able to explain 76.6% of the variation in sale price of home, and
is about $184,000 off from predicting the true sale price of a home, on average.
## Conclusions
__Recommendations:__ The specifics of how the top home features impact sale price are as follows:
- Controlling for all other features, for every mile away from Bellevue that a house is the price decreases by 3.4% on average.
- Keeping all other features constant, for every increase of 100 square feet of living area, the price increases by 1.5%.
- Accounting for all other features, a one unit increase in grade results in a price increase of 16.462746%.
- On average, our model is off by 189 thousand dollars for our training data and 168 thousand dollars for our testing data.
The model can help mortgage agents to decide whether the house as a collateral is valuable enough for resale if heaven forbid 
the home owner defaults on their mortgage. It can also integrate easily into the internal risk management system of the bank. 
Even though the model is not precise, it would do a good job managing risk exposure of the bank because the scale of its business allows 
for errors to cancel each other out on average.

__Future Steps:__
- Reduce error
- Explore ways to reduce multicollinearity
- Analyze how the time of year affects home prices

## How to Navigate the Repository:
The notebook which contains the most important information is called "HousingAnalysisMain", which is in the main branch. There are also 
supplementary notebooks in a folder called Notebooks, which contain experimental analysis. The data we used for this analysis is in the data
folder of the main branch.

