# Project 2: Operationalizing Machine Learning with AutoML & AML Pipelines

In this project, Azure Machine Learning is used to build and operationalize a classification model that 
utilizes the UCI Bank Marketing dataset (https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) to predict if a bank client will subscribe to a term deposit with the bank. The focus in this project will be on the operationalization of the best model that
results from an AutoMl training run. Operationalization will cover different aspects such as model deployment, model monitoring & logging, Swagger documentation of the model endpoint, consumption of the
model endpoint as well as creating, publishing and consuming an AML pipeline.

## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
**Step 1: Authentication**

Using the Azure Cloud Shell and the Azure Machine Learning CLI Extension, a Service Principal Account has been created and granted the owner role to the Azure Machine Learning workspace. The necessary commands are documented in the service_principal_setup_instructions.txt file.

Creation of Service Principal ml-auth:
![service_principal_creation](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/service_principal_creation.png)

Service Principal ml-auth has been granted access to the workspace:
![service_principal_access](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/service_principal_access.png)


**Step 2: Automated ML Experiment**

The dataset has been downloaded from https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv and registered as a dataset in the Azure Machine Learning workspace with the appropriate configurations. 

Registered dataset:
![registered_dataset](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/registered_dataset.png)

An AutoMl experiment has been started using the registered dataset. Classification has been selected and the "Explain best model" option has been checked. The "Exit criterion" has been reduced to 1 hour and the "Concurrency" has been set to 5.

Completed experiment:
![automl_run](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/automl_run.png)

Best model:
![best_model](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/best_model.png)


**Step 3: Deploying the Best Model**

The best model has been selected for deployment using Azure Container Instance (ACI). Authentication has been enabled. This has been completed using the Azure Machine Learning studio (the GUI).


**Step 4: Enabling Logging**

Application Insights has been enabled for the deployed model using the Python SDK and logs have been retrieved by running the logs.py script.

Enabling Application Insights:
![application_insights_enabled](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/application_insights_enabled.png)

Retrieving Application Insights Logs:
![application_insights_logs](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/application_insights_logs.png)


**Step 5: Swagger Documentation**

The Swagger JSON file has been downloaded from the deployed model and copied to the swagger directory. The swagger.sh script has been run to download the latest Swagger container and run it on port 9080. Finally, the serve.py script has been run to start a Python server on port 9000 to serve the Swagger JSON file.

Swagger running on localhost showing the HTTP API methods and responses for the model:
![swagger_ui](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/swagger_ui.png)


**Step 6: Consuming Model Endpoints**

The endpoint.py script has been run to interact with the trained model. For this the scoring_uri and key have been modified to match the deployed service.

Running the endpoint.py script against the API producing JSON output from the model:
![consume_endpoint](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/operationalizing_ml_project/screenshots/consume_endpoint.png)


**Step 7: Creating and Publishing a Pipeline**



Step 8: Documentation


## Screen Recording
A screencast containing the project results has been recorded using the Screencast-O-Matic tool and has been uploaded to YouTube: https://www.youtube.com/watch?v=hBo26CPtdIE.

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
