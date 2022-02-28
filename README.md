# General Architecture

I created an applicable CI & CD pipeline for an application that runs on Google Cloud Kubernetes cluster.

![CI:CD Pipeline](https://user-images.githubusercontent.com/44123646/155923131-2f1a50c5-d092-40ac-a197-17ae66b1492a.png)

# File Structure

Codeway-Testcase-App:  

app.py - Our main application      
test_app.py - Unit Test file     
Dockerfile - Used for building app.py to create a Docker image.   
cloudbuild.yaml - Used by Google Cloud to configure CI/CD.   
kubernetes.yaml.tpl - Kubernetes basic configuration template.   

Codeway-Testcase-Env:  

cloudbuild.yaml - Used by Google Cloud to configure CD.          
kubernetes.yaml - Kubernetes configuration file based on the given template.  

# Application Details

I used an python app that counts the number of visitor and updates the "hits" value on Redis Database. It can be run as:  

pip install flask,redis

python app.py

A redis server is configured as a default but you can modify app.py file to change DB. If you want to change database endpoint on run time:  

<img width="1005" alt="changeDB_ss" src="https://user-images.githubusercontent.com/44123646/155925118-522372f3-58e1-4a2c-9ccd-e9b4933de027.png">

Making a POST request to /changeDatabase used for changing endpoint on run time without rebuilding the container image. I know it isn't a pretty way to do, even though other options are not implemented, i will mention it later.

# Pipeline Implementation

In Google Cloud console, we start with enabling services that we will use later for creating CI/CD pipeline.  

gcloud services enable container.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com

We should create an Artifact Repository and Kubernetes Cluster.  

gcloud artifacts repositories create flask-app-repository \
  --repository-format=docker \
  --location=europe-west3
  
gcloud container clusters create flask-cloudbuild \
  --num-nodes 1 --region europe-west3

---------------------------------------------------------

Following 2 branch should be added on Cloud Build Trigger: (assuming already connected to github repo)  

Codeway-Testcase-App - Master Branch  
Codeway-Testcase-Env - Candidate Branch   

Configuration file should be choose as "cloudbuild.yaml" for both of them.  

---------------------------------------------------------

We can clone both repositories to our cloud shell and submit the build to Artifact Repositories: (In Codeway-Testcase-App directory)   

COMMIT_ID="$(git rev-parse --short=7 HEAD)"

gcloud builds submit --tag="europe-west3-docker.pkg.dev/${PROJECT_ID}/flask-app-repository/my-app:${COMMIT_ID}" .

---------------------------------------------------------

Reference: https://cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build#shell    

# Not Implemented Ideas

Changing database endpoint on run time:

1- It can be managed by Dynamic DNS. Same domain can be redirected new database endpoint on deploy time.

2- It can be managed by a proxy. We can configure a proxy server to point different database endpoint on deploy time.

Using Helm Charts to deploy and communicate with redis server:

1- I used a Redis chart on https://charts.bitnami.com/bitnami. Redis pods are functional but i can not modify my app to connect Redis on same namespace. So, i configured external Redis server.

I have started to learn container orchestration last week. I tried to do my best but i can't implement everything in one week.

# Test Environment

Since everything is on cloud, i can add a project member to my project. I need your gmail address to give an access to my environment.    
You can email me : mustafakucuk.dev@gmail.com

