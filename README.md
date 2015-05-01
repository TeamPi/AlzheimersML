# AlzheimersML

This work aims to define the progression of Alzheimer's disease and explore the predictors for the disease by analyzing the functional magnetic resonance imaging
(fMRI) images. The dataset is used for constructing a regression model mapping the features extracted from fMRI images to the Mini Mental State Examination (MMSE)
score.

To run the scripts first pip install the pip_dependencies.pip file to get the required dependencies and then type the following command:

python run.py fMRI_train.csv fMRI_test.csv

The information below was given to us for the assignment:

References
[1] Gong, Pinghua, Jieping Ye, and Changshui Zhang. "Robust multi-task feature learning." Proceedings of the 18th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2012.

----------------------------
----------------------------
Training sample size : 800
    Training data is in fMRI_train.xlsx. Each row is an example and each column is a feature. The features in each row are used to describe the corresponding example.


Test sample size : 200
    Test data is in fMRI_test.xlsx.xlsx

----------------------------
----------------------------
Number of features : 285
    These features are normalized so that each feature has a 0 mean and standard deviation of 1.

----------------------------
----------------------------
Labels : MMSE scores
    Labels of each patient (correspondingly their fMRI image) are the real-valued scores.


----------------------------
----------------------------
File format:
    For both training and test data files, the first row gives the feature names. The first column gives the example ID which is not a feature, and you should not
    use it when training your model. The second column gives the label for each image (or patient) as explained above, and the values are real numbers.  This is the target variable that you
    want to predict based on other features of each patient.


Your task is to train a regression model using a machine learning method studied in our class. You should only build your model from the training data, and then
test your model on the test data. You can either write your own codes to implement the method or download some existing machine learning packages. If you decide to
use downloaded package, please state the source of your download so TA can understand. If you decide to use a downloaded package, you might need to adapt it to the
given data. You are welcome to also try to figure out some other methods not studied in our class that perform better than our studied techniques. This will bring
extra credits of 5 points additional to the 40 total points. You need to make sure a in-class-studied technique is used first to compare with your other methods.
