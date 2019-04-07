# Feature description 
## (Trends based on given dataset, LAHacks.Deidentified.csv)

## %Failure / 90%rejected
		1.2554% of all the shipments experienced rejection from the inspector, and it's either rejected with > 90% of
 it's cases or being accepted 100%. Thus, we developed a new category '90%rejected' in [0, 1] to see whether there's
 a rejection. It's valueble to see whether >90% of the total case for a certain prodeuce is rejected, because it will
 will be a waste for all those shipment; It will be helpful to investigate the reason for such high rejection, so that
 future rejection can be avioded.
 		Our model will predict whether a certain shipment of produce will be rejected given a set of features as inputs.
		
## Category Name 
		Category Name (type of the produce) impacts rejection as we think different kinds of fruit or vegitable has different
	intrinsic biotic characterists such as lifespan and softness. 
	
## Vendor Name / Shipping Warehouse
		The quility of the vendor's produce might be a importent factor for rejection. The facility condition of Shipping 
	Warehouse (i.e. capacity) might be affecting rejection.Based on the existing data, we found certain vendor and certain 
	has Shipping Warehouse very high %rejection.  
		
## Inspector
		The strickness of Inspector can affect rejection, as inspector has different criteria to decide a rejection.

## Shipping Season
		Shipping Season (Spring/Summer/Fall/Winter) affects rejection, as different produce are naturally rape in 
different season.

## Shipping time
		Duration of the shipment affects the rejection, as longer shipment time decrease the freshness and the quality of the 
produce.
