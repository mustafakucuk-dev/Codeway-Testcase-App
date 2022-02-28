# General Architecture

I created an applicable CI & CD pipeline for an application that runs on Google Cloud Kubernetes cluster.

![CI:CD Pipeline](https://user-images.githubusercontent.com/44123646/155923131-2f1a50c5-d092-40ac-a197-17ae66b1492a.png)


# Application Details

I used an python app that counts the number of visitor and updates the "hits" value on Redis Database. It can be run as:

pip install flask,redis

python app.py

A redis server are configured as a default but you can modify app.py file to change DB. If you want to change database endpoint on run time:

<img width="1005" alt="changeDB_ss" src="https://user-images.githubusercontent.com/44123646/155925118-522372f3-58e1-4a2c-9ccd-e9b4933de027.png">

