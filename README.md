# Coral-Classification-WatsonX-Challenge
Team: Elijah Ramsey, Taylor Sperry, Farhad Siraj, Robbie Hanson, Ana Tivadar, Chase Brock, Liam Atkins, Meegan Conrad, Stephen Smigelsky, Sean Knipe    

Track: Watsonx.data (Track 4)     

Utilizing: OpenCV, Scikit-learn, Watsonx Jupyter notebook, fill in more here    

Data: [Reef Renewal USA](https://reefrenewalusa.org)

 
# Overview 
Just this month, Manatee Bay in the Florida Keys recorded an ocean temp of an astonishing 101.1°. No sensor has ever recorded a temperature of 101° anywhere in the world's oceans. 

The effects of rising ocean temperatures have caused coral bleaching events all over the world, including the Florida Key's Reef Tract, the largest barrier reef in the United States. Coral reefs support some of the most biodiverse ecosystems on the planet, and are home to a quarter of all marine animals. Humans also depend on coral reefs as a food source and income from tourism. 

Reef Renewal is an organization based in the Florida Keys who are trying to restore the coral population by growing thousands of fragments in underwater nurseries and outplanting healthy corals into the dying reefs. 

# Our Goal
Help Reef Renewal create a data pipeline that monitors newly outplanted corals and predicts the health of the reefs. After the data is analyzed, a report needs to be generated in order to recieve government grants to continue funding their work. This report contains coral area cover, coral species and coral health.  

# Our Solution
Data is collected in the form of photos during dives using a GoPro. Outplanting dives are done in a designated area of a reef, and photos are taken continuously swimming along the topside of the reef. Photos are taken before and after outplanting.   
Our solution contains 2 parts: an image classification ML model followed by an automated report generation process using Watsonx. 

# Part 1: Image Classification
Using OpenCV, Reef Renewal's photos will be used to label coral area cover, coral species and coral health. Then, this data will be used to train a model in Scikit-learn. The model will then be able to analyze and predict the health of the reef. 

# Part 2: Report Generation
From the data analysis phase done by the model, the results will be used to generate a report used to get grants from the government. Using Watsonx (fill in more details), a sample report will be automatically generated using the results of the previous model. 
