apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-cloudbuild
  labels:
    app: flask-cloudbuild
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-cloudbuild
  template:
    metadata:
      labels:
        app: flask-cloudbuild
    spec:
      containers:
      - name: flask-cloudbuild
        image: europe-west3-docker.pkg.dev/GOOGLE_CLOUD_PROJECT/flask-app-repository/my-app:COMMIT_SHA
        ports:
        - containerPort: 8080
---
kind: Service
apiVersion: v1
metadata:
  name: flask-cloudbuild
spec:
  selector:
    app: flask-cloudbuild
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer