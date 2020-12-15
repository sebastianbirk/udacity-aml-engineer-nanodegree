# Project 2: Operationalizing Machine Learning with AutoML & AML Pipelines

In this project, Azure Machine Learning is used to build and operationalize a classification model that 
utilizes the UCI Bank Marketing dataset (https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv) to predict if a bank client will subscribe to a term deposit with the bank. The focus in this project will be on the operationalization of the best model that
results from an AutoMl training run. Operationalization will cover different aspects such as model deployment, model monitoring & logging, Swagger documentation of the model endpoint, consumption of the
model endpoint as well as creating, publishing and consuming an AML pipeline.

## Architectural Diagram
![architectural_diagram](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/architectural_diagram.png)

## Key Steps
**Step 1: Authentication**

Using the Azure Cloud Shell and the Azure Machine Learning CLI Extension, a Service Principal Account has been created and granted the owner role to the Azure Machine Learning workspace. The necessary commands are documented in the service_principal_setup_instructions.txt file.

Creation of Service Principal ml-auth:
![service_principal_creation](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/service_principal_creation.png)

Service Principal ml-auth has been granted access to the workspace:
![service_principal_access](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/service_principal_access.png)


**Step 2: Automated ML Experiment**

The dataset has been downloaded from https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv and registered as a dataset in the Azure Machine Learning workspace with the appropriate configurations. 

Registered dataset:
![registered_dataset](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/registered_dataset.png)

An AutoMl experiment has been started using the registered dataset. Classification has been selected and the "Explain best model" option has been checked. The "Exit criterion" has been reduced to 1 hour and the "Concurrency" has been set to 5.

Completed experiment:
![automl_run](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/automl_run.png)

Best model:
![best_model](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/best_model.png)


**Step 3: Model Deployment**

The best model has been selected for deployment using Azure Container Instance (ACI). Authentication has been enabled. This has been completed using the Azure Machine Learning studio (the GUI).


**Step 4: Enabling Logging**

Application Insights has been enabled for the deployed model using the Python SDK and logs have been retrieved by running the logs.py script.

Enabling Application Insights:
![application_insights_enabled](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/application_insights_enabled.png)

Retrieving Application Insights Logs:
![application_insights_logs](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/application_insights_logs.png)


**Step 5: Swagger Documentation**

The Swagger JSON file has been downloaded from the deployed model and copied to the swagger directory. The swagger.sh script has been run to download the latest Swagger container and run it on port 9080. Finally, the serve.py script has been run to start a Python server on port 9000 to serve the Swagger JSON file.

Swagger running on localhost showing the HTTP API methods and responses for the model:
![swagger_ui](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/swagger_ui.png)


**Step 6: Consuming Model Endpoint**

The endpoint.py script has been run to interact with the trained model. For this the scoring_uri and key have been modified to match the deployed service.

Running the endpoint.py script against the API producing JSON output from the model:
![consume_endpoint](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/consume_endpoint.png)


**Step 7: Creating and Publishing a Pipeline**

The pipeline_with_automl_step.ipynb notebook has been adjusted and run to create, publish and consume a pipeline.

AML studio pipeline section showing the pipeline REST endpoint with a status of ACTIVE:
![pipeline_endpoints](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/pipeline_endpoints.png)

The bankmarketing dataset with the AutoML module:
![pipeline_run](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/pipeline_run.png)

The "Use RunDetails Widgets" in the Jupyter Notebook showing the step runs:
![run_details_widget](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/run_details_widget.png)

A completed pipeline run:
![pipeline_runs](https://github.com/sebastianbirk/udacity-aml-engineer-nanodegree/blob/master/02_ml_operations/project_2_operationalizing_ml/screenshots/pipeline_runs.png)


**Step 8: Documentation**
A screencast showing the entire process of the working ML application has been created. The link can be found in the next section. In addition, this README has been created which contains an overview of the project, an architectural diagram, a short description of the project main steps as well as a short section on how to improve the project in the future.

## Screen Recording
The screencast containing the project results has been recorded using the Screencast-O-Matic tool and has been uploaded to YouTube: https://www.youtube.com/watch?v=hBo26CPtdIE.

## Improvement Suggestions
- Dataset: The registered dataset can directly point to the URI instead of making use of a local file upload so that when the data gets updated, automatically the new data will be used within the pipeline run.
- Automation: In general, some steps have been completed manually using the AML studio (GUI) such as model deployment of the best model. This can be automated in code and executed by a DevOps pipeline in the future.
- Model: An even better model could be developed by making use of feature engineering or hyperparameter tuning using Hyperdrive.
- Model endpoint: The model endpoint could be benchmarked with the Apache Benchmark command-line tool to ensure the right compute setup.
- Swagger Documentation: The swagger UI could be hosted on a web server instead of on localhost so that other people have access to the model documentation.
- Pipeline: The pipeline could be scheduled to run on a regular basis or execute in a trigger-based manner (e.g. when dataset is updated).
