# Analysis of Dog Behavior and Breed Bias
#### Anna Bellizzi and Nicole George
#### CST383-30_SP23

## Introduction
<br>
  A common perception is that pitbulls are one of the most dangerous dog breeds, so we wanted to explore some data behind this idea. With this in mind, we also want to use machine learning techniques to predict the likelihood of a bite incident occurring based on dog breed and size (height and weight) data within dog bite datasets. From the research article, "Ancestry-inclusive dog genomics challenges popular breed stereotypes" (Alonso et Al.) published on [Science.org](https://www.science.org/doi/10.1126/science.abk0639)
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

## Methods

Numpy, Pandas, Matplotlib, and Seaborn for data preparation, analysis and plotting
Google Colaboratory for development and project environment, versioned in GitHub
Scikit: KNeighborsClassifier, Naive Bayes, Logistic Regression

## Results
Pitbulls are the breed that bites the most in our data set, but that does not mean they are the only breed that bites at a high rate or the only breed that is the most dangerous. What we can not determine from the dataset is whether pitbulls are more dangerous based on single bite incidents. Is there a mortality rate associated with incidence of bite? Is incidence of a single bite a true indicator of lifelong agression? What we can glean from our research is that while pitbulls may be the most reported breed in bite incidents, we can accumulate bit incidents of multiple breeds and come up with similar statistic when considering age and gender data that we had on hand.


## Discussion and Summary

There are many factors that contribute to dog temperment and behavior. Based on preparatory reading done on the topic, experts in the field- animal behaviorists and veterinarians- have proven that  breed is not a reliable predictor of future dog behavior. In running through the data during the initial data preparation phase, it's clear that there are patterns in reported incidents, but a few additional questions come to mind, even looking at data that supports the opposite of what we are arguing:<br>
1. Are there regional or statewide differneces in breed bans? It is intersting to note the difference from coast to coast on top bit incident count.
2. Are there different reporting laws? Does a bite have to be reported if law enforcement or  hospital visit are not involved? Who is legally required to report bites in each location?
3. Is breed popularity regional? It owuld be interesting to look at adoption rates of certain breeds regionally. If there are more adoptable or adopted pitbulls in one region versus another? By virtue of volume, bite incidents would be greater when more pitbulls are present.
4. What triggers a bite incident, and what are the environmental factors that have contributed to a dog's overall temperament? Was it rescued? Surrendered? Seized for cruelty? This additional data would certainly paint a richer picture.
<br>
Portraying all breeds as equally tempered would help prevent abandonment and bias in adoptions. Shelters are well-known for being overwhelmed most of the time, and the longer animals stay in shelter, the less likely that are to be adopted over that time. If it were more commonly known that breed is not an indicator of future behavior, shelters could use that and work with behaviorists to educate the public interested in adopting. While it is true that breeds do have lifestyle-specific needs, that has no bearing on future behavior if they are provided with the environment they need to thrive.

