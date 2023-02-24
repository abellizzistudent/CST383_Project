# Analysis of Dog Behavior and Breed Bias
#### Anna Bellizzi and Nicole George
#### CST383-30_SP23

## Introduction
<br>
  A common perception is that pitbulls are one of the most dangerous dog breeds, so we wanted to explore some data behind this idea. With this in mind, we also want to use machine learning techniques to predict the likelihood of a bite incident occurring based on dog breed and size (height and weight) data within dog bite datasets. From the research article, "Ancestry-inclusive dog genomics challenges popular breed stereotypes" (Alonso et Al.) published on [Science.org](https://www.science.org/doi/10.1126/science.abk0639#:~:text=Most%20behavioral%20traits%20are%20heritable,9%25%20of%20variation%20in%20behavior.):
<br><br><i>"...dog breed is generally a poor predictor of individual behavior and should not be used to inform decisions relating to selection of a pet dog." </i>
<br><br>
We hypothesize that by training a model based on breed, size, and age we will discover the same- that breed is not a good predictor of behavior, and therefore pitbull breeds and mixes pose no grater risk than any other breed or mix. In doing so, we may help people adopt dogs that are better suited for them, and ultimately have every dog end up in a Forever Home.

## Selection of Data
<br>
  The data comes from three datasets, two of which are city-specific bite reports from San Francisco and New York, which were downloaded in February 2023. Each of these sets had different features, with one common feature of breed group. Each row of the set is a reported bite incident. We kept unique features from each set because they are valueable in our analysis even though the amount of available data might be smaller. The third dataset in use contains a collection of breed groups and their average size, weight, and lifespan data. We merged this set into the SF and NY data and ended up with 21,911 rows that contain record of a bite incident and the average height, weight and lifespan of the breed identified in the record.
  <br>
  Rows indicating unknown dog breed were dropped from the dataset. Since we are looking at breed-specific incidents, unknown breed bite records are not relevant. The age column data was formatted to remove alpha characters and fractional representations and converted to years in decimal format. Gender codes were simplified to numeric 1 or 2 for Male or Female and Spayed and Neutered gender were absorbed into these two columns accordingly.
  <br>
  The data has 8 numeric features: dataset, breed_group, bite_code, gender, age, average height, average_weight, lifespan and 3 categorical features: breed_group_S, primary_breed, and bite_severity<br><br>
  Null values are set to 0 in all numeric features except bite_code, where a bite code of 0 is significant. A null bite code is set to -1.

Methods

Numpy, Pandas, Matplotlib, and Seaborn for data preparation, analysis and plotting
Google Colaboratory for development and project environment, versioned in GitHub
Scikit: KNeighborsClassifier, Naive Bayes, Logistic Regression

Results

What answer was found to the research question; what did the study find? Was the tested hypothesis true? Any visualizations?

Discussion

What might the answer imply and why does it matter? How does it fit in with what other researchers have found? What are the perspectives for future research? Survey about the tools investigated for this assignment.

Summary

Most important findings.

