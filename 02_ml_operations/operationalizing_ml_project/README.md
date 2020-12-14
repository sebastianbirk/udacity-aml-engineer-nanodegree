# Project 2: Operationalizing Machine Learning with AutoML & AML Pipelines

In this project, Azure Machine Learning is used to build and operationalize a classification model that 
utilizes the UCI Bank Marketing dataset (https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) to predict if a bank client will subscribe to a term deposit with the bank. The focus in this project will be on the operationalization of the best model that
results from an AutoMl training run. Operationalization will cover different aspects suchs as model deployment, model monitoring & logging, Swagger documentation of the model endpoint, consumption of the
model endpoint as well as creating, publishing and consuming an AML pipeline.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
Step 1: Authentication

Using the Azure Cloud Shell and the Azure Machine Learning CLI Extension, a Service Principal Account has been created and granted the owner role to the Azure Machine Learning workspace. The necessary commands are documented in the service_principal_setup_instructions.txt file.

![service_principal_creation](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/service_principal_creation.png)

![service_principal_access](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/service_principal_access.png)

Step 2: Automated ML Experiment

![registered_dataset](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/registered_dataset.png)

![automl_run](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/automl_run.png)

![best_model](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/best_model.png)

Step 3: Deploying the Best Model



Step 4: Enabling Logging



Step 5: Swagger Documentation



Step 6: Consuming Model Endpoints



Step 7: Creating and Publishing a Pipeline



Step 8: Documentation


## Screen Recording
A screencast containing the project results has been recorded using the Screencast-O-Matic tool and has been uploaded to YouTube: https://www.youtube.com/watch?v=hBo26CPtdIE.

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
