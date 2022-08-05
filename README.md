# Diabetes Prediction System

## Introduction
Diabetes is an illness caused because of high glucose level in a human body. Diabetes
should not be ignored if it is untreated then Diabetes may cause some major issues in a person like:
heart related problems, kidney problem, blood pressure, eye damage and it can also affects other
organs of human body. Diabetes can be controlled if it is predicted earlier.
To achieve this goal this project work we will do early prediction of Diabetes in a human
body or a patient for a higher accuracy through applying Machine Learning Techniques. Machine
learning techniques provide better result for prediction by constructing models from datasets
collected from patients.

In this work we will use Machine Learning Classification and ensemble techniques on a
dataset to predict diabetes. Which are Support Vector Machine (SVM) and Random Forest (RF).
The accuracy is different for every model when compared to other models.
The Project work gives the accurate or higher accuracy model shows that the model is
capable of predicting diabetes effectively. Our result shows that Support Vector Machine achieved
higher accuracy compared to Random Forest.

## Proposed System
The proposed system is classification of Indian PIMA dataset for diabetes as binary
classification and making a interactive user interface in the form of Web App. This is proposed to
achieve through two machine learning algorithms, Support Vector Machine and Random Forest
Classifier. The Web App is made with the help of streamlit. The proposed system improves
accuracy of prediction through machine learning techiques and the intera tive user interface lets
people check whether they have diabetes from anywhere. 

## How to deploy to Azure App Service?
There are multiple ways to be go about this but I will share the experience that I found to be the easiest. We will be deploying to Azure App Service using a Docker linux container and Azure Container Registry (ACR).

## Prerequisites
- AzureCLI
- Docker

## Step 1 - ACR
- Create a container on ACR via Azure portal.
- Sign in to Azure Portal.
- From Azure Marketplace select Containers > Container Registry.
- Enter the required information.
- Select “Review + Create”.
- Once created, you should be redirected to a landing page with information pertaining to your container
- On the “Overview” tab, there should be something called “Login Server” (e.g. specificregistryname.azurecr.io). Note down this value as you will need again when you push and pull images with Docker.
- Login to registry.
  - Sign in to Azure CLI by running the command `az login` in your terminal. Note that this command will not work if you do not have Azure CLI installed.
  - Log into Azure ACR by running `az acr login — name <registry-name>`. Note do not include azurecr.io for the registry name.
- If you get stuck at any of these steps – take a look at this [tutorial](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli).

## Step 2 - Create a Requirements.txt file
- Run the command `pip freeze > requirements.txt` in your application terminal to autogenerate the requirements.txt file.
- This file contains all of your application’s dependencies.

## Step 3 - Create a Docker file
- The Dockerfile contains the instructions to build the image. Here is my Dockerfile for reference:
``` 
FROM python:3.9.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit" , "run"]
CMD ["PredictDiabetes.py"]
```

- If you choose to use this file just remember to change the Python version and your application .py file (in my case I named it “PredictDiabetes.py”).

## Step 4 - Build Docker container locally

- To build Docker container:
```
docker build –t mystapp:latest .
```
- To view all your Docker images:
```
docker images
```
- To run locally:
```
docker run -p 8501:8501 mystapp:latest
```

## Step 5 - Push local image to ACR
- Type in the following command:
```
docker login diabetesproject.azurecr.io
```
It will ask for your username and password. You will get the username and password of your registry after enabling the *Admin user* option in the *Access Keys* section of your registry.
- Tag your image:
```
docker tag mystapp:latest diabetesproject.azurecr.io/myimage:v1
```
- Push your image:
```
docker push diabetesproject.azurecr.io/myimage:v1
```

## Step 6 - Create an Azure App Service Web App
- Go to Azure portal.
- Search for App Services (or it can appear as Web App).
- Click the “Add” button.
- Fill out all the necessary fields.
- For Publish -> select “Docker Container”.
- On the “Docker” tab -> under Image Source -> select “Azure Container Registry” -> select your registry (which should appear on the dropdown list).
- Select “Review + Create”.

Awesome! Now you can see your app running on Azure by browsing to * http://<app-name>.azurewebsites.net *.

## Demo Video

https://user-images.githubusercontent.com/91541977/183058170-4fad8d01-f3ab-4c51-ab63-8418c32c5d06.mp4



