
This project uses K-means clustering to sort different medical schools into different clusters to determine the most optimal medical schools for pre-meds to apply to based on in-state matriculation percentage, MCAT score, and GPA. A web application was created using Flask to allow people to see which list of medical schools they should apply for. The web application was deployed to Google Cloud to allow for access by anyone. 




<h1>Key Steps:<h1>

<h3>Scaling the Dataset</h3>
The dataset of medical schools had the values scaled so that the mean of the values was equal to zero.

<h3>Principal Component Analysis</h3>
Principal Component Analysis (PCA) performs a linear transformation on a dataset to reduce the number of dimensions of the dataset. This reduces the computational time needed for the machine learning model to analyze and utilize the model for predictions. PCA allows for greater clustering capabiity as well, allowing for the different medical schools to be separated into categories more easily. The dataset was reduced, so that the dataset only had 2 features, since 2 is the minimum number of features that allows for adequate clustering and captures much of the variance from the original dataset

<h3>K-means Clustering</h3>
K-means Clustering was utilized, as it allows for the production of distinct clusters. K means clustering separates the med schools by grouping the closest points together into the same cluster. More specifically, it groups the different medical schools to the cluster with the nearest mean. After the points are clustered, the mean of the new cluster is calculated. After calculation, the points are reclustered to the closest cluster mean. This process is repeated until no points are reclassified to a different cluster. Four clusters allows for a non-trivial amount of clusters, while still allowing for the clusters to be distinct from each other.

<h1>Website</h1>
https://med-school-cluster.onrender.com/methodology

