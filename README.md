# Wine-Quality-Prediction-End-to-End-Project# End-to-end-Machine-Learning-Project-with-MLflow


## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```

'''export MLFLOW_TRACKING_URI="https://dagshub.com/AsifIkbal1/Wine-Quality-Prediction-End-to-End-Project"

export MLFLOW_TRACKING_USERNAME="AsifIkbal1" 

export MLFLOW_TRACKING_PASSWORD="5060c52e0077a940410147fccd4b7e04c7363288"
'''

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


d729dcf9c5c5c8838b54da2c717430e8358d51f8

5060c52e0077a940410147fccd4b7e04c7363288


mlflow '' http://localhost:5000/#/experiments/0?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All%20Runs&selectedColumns=attributes.%60Source%60,attributes.%60Models%60&isComparingRuns=false&compareRunCharts=dW5kZWZpbmVk ''


# 🍷 Wine Quality Prediction – Red Wine Dataset

The **Wine Quality – Red** dataset is a popular dataset used for **Supervised Learning** tasks in Machine Learning. It contains **numerical features** like acidity, sugar, alcohol, and more – with a known **target label**: `quality` (wine rating score from 0 to 10).

---

## 🎯 Problem Type: Supervised Learning

Because:
- ✅ Has **input features** (e.g., acidity, residual sugar, alcohol, etc.)
- ✅ Has a **known output label**: `quality`

---

## 📈 Two Possible Problem Approaches

### 🔢 Regression
> Predict the **exact wine quality score**  
📊 Example: `6.0`, `7.0`, etc.

### 🧠 Classification
> Categorize wine into groups:
- 🍷 **Low**: `3–4`
- 🍷 **Medium**: `5–6`
- 🍷 **High**: `7–8`

---

## 🤖 Algorithms & Notes

| 🔍 Algorithm                          | 📝 Notes                                      |
|--------------------------------------|-----------------------------------------------|
| 💡 Logistic Regression               | Simple & interpretable                        |
| 🌳 Decision Tree Classifier          | Easy to visualize and explainable             |
| 🌲 Random Forest Classifier          | Great performance, handles overfitting well   |
| 🚀 Gradient Boosting (XGBoost, LGBM) | Often achieves **state-of-the-art** results   |
| 👥 KNN (K-Nearest Neighbors)         | Easy to implement, slower on large datasets   |
| 💠 SVM (Support Vector Machine)      | Effective in high-dimensional feature spaces  |

---

## 🧪 Dataset Link
- 📦 Source: [UCI Machine Learning Repository – Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality)

---

## 📌 Target Variable
- `quality`: Wine rating score ranging from `0` to `10`

---

## ✨ Want to try it?
Train your own model and predict the quality of red wine using this amazing dataset! 🍇🍷

---

_🔥 Feel free to fork this repo and play around!_
