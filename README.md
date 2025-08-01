# AI Travel Itinerary Planner

An AI-powered Streamlit web app that generates personalized day trip itineraries based on your chosen city and interests. Built with LangChain, Groq LLM, and containerized for easy deployment on Kubernetes. Includes full ELK stack (Elasticsearch, Logstash, Kibana, Filebeat) integration for log monitoring.

---

## Features

- 🌍 Enter a city and your interests to get a custom day trip itinerary.
- 🤖 Uses LLM (Groq) via LangChain for itinerary generation.
- 🐳 Dockerized for portability.
- ☸️ Kubernetes deployment-ready.
- 📈 Centralized logging with ELK stack and Filebeat.

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/sunithalv/AI-TRAVEL-ITINERARY-PLANNER.git
```

### 2. Install Requirements (Locally)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the App Locally

```bash
streamlit run app.py
```

---

## Docker Usage

### Build the Docker Image

```bash
docker build -t streamlit-app:latest .
```

### Run the Container

```bash
docker run -p 8501:8501 --env-file .env streamlit-app:latest
```

---

## Kubernetes Deployment

1. **Build Docker image inside Minikube:**

    ```bash
    eval $(minikube docker-env)
    docker build -t streamlit-app:latest .
    ```

2. **Create Kubernetes secret for API key:**

    ```bash
    kubectl create secret generic llmops-secrets --from-literal=GROQ_API_KEY=your_groq_api_key_here
    ```

3. **Deploy the app:**

    ```bash
    kubectl apply -f k8s-deployment.yaml
    ```

4. **Access the app:**

    ```bash
    kubectl port-forward svc/streamlit-service 8501:80 --address 0.0.0.0
    ```

---

## ELK Stack for Logging

- Deploy Elasticsearch, Kibana, Logstash, and Filebeat using the provided YAML files:
    - [elasticsearch.yaml](elasticsearch.yaml)
    - [kibana.yaml](kibana.yaml)
    - [logstash.yaml](logstash.yaml)
    - [filebeat.yaml](filebeat.yaml)

- See [FULL DOCUMENTATION.md](FULL%20DOCUMENTATION.md) for detailed setup steps.

---

## Project Structure

```
.
├── app.py
├── Dockerfile
├── k8s-deployment.yaml
├── requirements.txt
├── setup.py
├── src/
│   ├── chains/
│   ├── config/
│   ├── core/
│   └── utils/
├── logs/
├── elasticsearch.yaml
├── kibana.yaml
├── logstash.yaml
├── filebeat.yaml
└── FULL DOCUMENTATION.md
```


