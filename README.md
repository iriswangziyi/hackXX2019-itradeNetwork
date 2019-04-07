# hackXX2019-itradeNetwork

ML model predicting whether a certain shipment of produce will be rejected

## Inspiration

Maximize the efficiency of fresh produce distribution is both important for farmers and customers. The work ItradeNetwork does inspire us to come up with a model that can predict the rejection of certain produce order. With the model, we can help reduce the current world issue about food waste.

## What it does
Based on the exsiting dataset, we built and trained a failure prediction model. Given a set of features as inputs:
* 'Category Name' -- name of the produce 
  * (i.e. Apples)
* 'Vendor Name' -- name of the Vendor prodiving that produce 
  * (i.e. Vendor 1c47447e)
* 'Shipping Warehouse' -- code refers to the Shipping Warehouse 
  * (i.e Warehouse 60268bc9)
* 'Inspector'-- name of the Inspector 
  * (i.e Inspector afbf7591)
* 'Shipping Time'-- duration of the shipment 
  * (i.e 3)
* 'Season' -- season of the shipment 
  * (i.e Spring)
Our model predicts whether more than 90% of the cases will be failed.

## How we built it
We used Jupyter note with Python 3 to process our dataset given by ItradeNetwork. We cleaned the data, take a quick look at the characteristics of our data, created list of features to develop a Machine Learning model. We trained our model with 80% dataset we have and tested with the rest 20% of the dataset. 

## Challenges we ran into
1.  parsing out features that have reality applications
2. process a have high dimension of categorical data.
3.  see how good is our model, find the best test
4.  linking the backend with the front end

## Accomplishments that we're proud of
Our team pulled out each one's strength and we were very supportive to each other.  We all learned a lot in this application of data science.

## What we learned
1. we learned a lot of ML tests for different goals. 
2. we learned how to use python better
3. we learned how to link front and back end together.

## What's next for HackXX with ItradeNetwork
1. We can continue training the model to make our prediction better. 
2. Creating better webpage for user interation
3. Develop a clear way of explanation of the model output
