# Graduation Project – AI Model (Flask API)

This repository contains the AI model deployment part of a TÜBİTAK-supported Graduation Project focused on image-based waste classification.

The model is deployed as a Flask REST API and uses a YOLO-based deep learning model to detect recyclable materials from uploaded images.

---


## About the Project

Graduation Project AI Model is responsible for:
<ul>
<li>Receiving images from the backend</li>

<li>Running object detection using a trained YOLO model</li>

<li>Returning structured prediction results (labels, confidence, bounding boxes)</li>

</ul>


This service is designed to work independently and communicate with the backend over HTTP.


### Model Responsibilities

<ul>
  <li>Image preprocessing</li>
  <li>YOLO-based object detection</li>
  <li>Returning detection results as JSON</li>
  <li>Providing a scalable and containerized AI service</li>
</ul>


---


## Features

<ul>
  <li>YOLO-based waste classification</li>
  <li>RESTful Flask API</li>
  <li>JSON-based prediction responses</li>
  <li>Dockerized model deployment</li>
  <li>Backend integration ready</li>
</ul>


---


## Technologies Used

<ul> 
  <li>Python</li>
  <li>Flask</li>
  <li>Ultralytics YOLO</li>
  <li>Docker</li>
</ul>


## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/safaygt/GraduationProjectDeployModel.git

cd GraduationProjectDeployModel
```


### 2. Run Locally

Make sure the required Python packages are already installed in your environment.

Run the Flask application using:
```bash
python app.py
```

The API will be available at:

```text
http://localhost:5000
```

### 3. Run with Docker (Recommended)

```bash
docker-compose up --build -d
```



Related Repositories
<ul> 
  <li>Backend (Spring Boot)</li>
  <p><a href="https://github.com/safaygt/graduation-project.git">
      Graduation Project Backend → GitHub
    </a></p>
  
  <li>Frontend (React)</li>
  <p><a href="https://github.com/safaygt/GraduationProjectFrontEnd.git">
      Graduation Project Frontend → GitHub
    </a></p> 

    
  <li>Model Codes</li>
     <p><a href="https://colab.research.google.com/drive/1cXxeEJbGrX1H93ppr1vmGhJWHi5AY8j1">
      Model → Google Colab
  </a></p>
    
</ul>







<h1>Developer</h1>

Safa Yiğit
GitHub: [@safaygt](https://github.com/safaygt)  


