# Capstone Project: Azure Machine Learning

In this capstone project of the Azure Machine Learning Engineer Nanodegree, a classification model is built to predict whether employees are at risk of leaving a company, a phenomenon called attrition. The model is trained on the IBM HR Analytics Employee Attrition & Performance dataset from Kaggle (https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset). Both AutoML & Hyperdrive are used to train different
models and tune their hyperparameters. The best performing model is deployed to Azure Container Instances (ACI) and it is shown how the model endpoint can be interacted with. The chosen evaluation metric is AUC_weighted as the dataset is characterized by imbalance in the class label.

## Project Set Up and Installation

The prerequisites to run/reproduce this project are:
- Create an Azure Subscription
- Create an Azure Machine Learning Workspace
- Create an Azure Machine Learning Compute Instance
- Clone this git repository to the Azure Machine Learning Compute Instance file system
- Provision the conda development environment as jupyter kernel:
There are two conda environment files ("*.yml") provided in the "dependencies" folder, one for model development and one for model training. The environment for model development should be provisioned as jupyter kernel in the following way:
  - Run ```conda env create -f dev_environment.yml```in the terminal to create a conda environment from the dev_environment.yml file. The name of the conda environment will be     attrition_dev. 
  - Activate your conda environment with ```conda activate attrition_dev```.
  - Provision the environment as a jupyter kernel using ```python -m ipykernel install --user --name=attrition_dev```.
  - Select the attrition_dev kernel inside the jupyter notebook when running the notebooks.
- Run the "explorative_data_analysis.ipynb" notebook to register the data as a tabular dataset in the Azure Machine Learning Workspace

## Dataset

### Overview
I am using the IBM HR Analytics Employee Attrition & Performance dataset from Kaggle (https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset). The dataset contains the target class "Attrition" as well as demographic, job-specific, geographic and socioeconomic feature columns. It is a fictional dataset created by IBM Data Scientists. In total the dataset has 1470 rows and 35 columns. I have set aside 20% for testing and have registered 80% as training dataset in the AML workspace (check "explorative_data_analysis.ipynb" for details).

### Task
The dataset is used for the binary classification task of predicting whether an employee is at risk of leaving the company, a phenomenon that is called attrition. It is important to detect the risk of attrition early to be able to action appropriate countermeasures. A high employee turnover is negative for the company culture and, in addition, hiring new employees is more costly than retaining existing ones and comes with additional onboarding and learning overhead.

### Access
The data has been downloaded from Kaggle and added to the github repository as it is a static dataset of small size. The "explorative_data_analysis.ipynb" notebook registers the data in the Azure Machine Learning workspace from where it can be accessed with ease using the Dataset class from the Azure Machine Learning SDK.

## Automated ML
The AutoML run settings and configuration can be found in "automl.ipynb". 
- Early stopping is enabled to save resources and stop non-promising training runs early.
- The experiment timeout is set to 90min, which I believe is enough time to train a well-performing model while considering resource constraints.
- The maximum concurrent iterations are set to 4 since the compute cluster that is used has 5 nodes, and this number should be smaller than the compute cluster nodes.
- I used AUC_weighted as evaluation metric as the prediction target "Attrition" shows a class imbalance. Using accuracy is therefore inappropriate.
- I used 20% of the training data as validation set. I did this consistently through all model training attempts (including the baseline models, the automl models and the hyperdrive models) to ensure fair comparability.
- Featurization is set to auto to allow AutoML to do automatic featurization

### Results
The best AutoML model was a VotingEnsemble with an AUC_weighted of 0.835. Compared to the baseline models and the hyperdrive run this is a very good result, which is why this model was also used for deployment to Azure Container Instances (ACI). The most important parameter n_estimators was set to 10, which means that this is an ensemble of 10 models. Specific hyperparameters and weights can be found in the "automl.ipynb" notebook in the section "Best Model" or in the screenshot below.
The model could probably be further improved by increasing the experiment timeout and thus allowing AutoML to train more different models.

RunDetails widget:
![automl_run_widget](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/03_aml_capstone/capstone_project_azure_machine_learning_engineer/screenshots/automl_run_widget.png)

Best model:
![best_automl_model](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/03_aml_capstone/capstone_project_azure_machine_learning_engineer/screenshots/best_automl_model.png)

## Hyperparameter Tuning
For the Hyperdrive run I chose an XGBoost classifier as this algorithm is in general on of the best-performing ones for classification tasks. Also, the AutoML run showed that the XGBoost classifier is quite promising as it had multiple XGBoost models among the top performers. 
For the specific hyperparameters that I tuned as well as their ranges I have taken https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/#:~:text=XGBoost%20has%20a%20very%20useful,rate%20and%20number%20of%20trees as an inspiration, which is a very detailed guide to hyperparameter tuning for XGBoost models. Some of the tuned hyperparameters were integers while others had continuous ranges. Details can be found in the "hyperparameter_tuning.ipynb" notebook in the section "Hyperdrive Configuration".

### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?
The best trained XGBoost classifier had an AUC_weighted of 0.739, which is quite good compared to the baseline model but falls short of the model that was trained using AutoML. Therefore, this model was not deployed. The specific hyperparameters of the best model can be found in the "hyperparameter_tuning.ipynb" notebook and in the screenshot below.
I think the model could have been further improved by doing feature engineering, for example with the boruta_py library.

RunDetails widget:
![hyperdrive_run_widget](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/03_aml_capstone/capstone_project_azure_machine_learning_engineer/screenshots/hyperdrive_run_widget.png)

Best model:
![best_hyperdrive_model](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/03_aml_capstone/capstone_project_azure_machine_learning_engineer/screenshots/best_hyperdrive_model.png)

## Model Deployment
As mentioned in above sections, the best AutoML model was also the best model overall and has thus been deployed to Azure Container Instances (ACI). The model deployment is implemented at the bottom of the "automl.ipynb" notebook and it is also demonstrated how the model endpoint can be queried using the Python requests library. A final concatenated dataframe shows the model prediction results next to the actual target and feature variables.

Model Endpoint:
![model_endpoint](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/03_aml_capstone/capstone_project_azure_machine_learning_engineer/screenshots/model_endpoint.png)

## Screen Recording
The screencast containing the project results has been recorded using the Screencast-O-Matic tool and has been uploaded to YouTube:
https://www.youtube.com/watch?v=eFuYskgSQsI

## Improvement Suggestions
- The model can be converted to ONNX format.
- Further models (other classification algorithms) can be trained with hyperdrive.
- Additional feature engineering could be done, for example using the boruta_py library.

