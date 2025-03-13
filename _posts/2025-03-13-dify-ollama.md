---
layout: post
title:  run Dify with Ollama.
subtitle: Below is a step-by-step guide to set up and run Dify with Ollama. This assumes you want to deploy both locally and integrate them to run large language models (LLMs) on your machine. 
cover-img: https://images.unsplash.com/photo-1677442135703-1787eea5ce01
tags: [ollama, dify]
---

### Overview


Below is a step-by-step guide to set up and run Dify with Ollama. This assumes you want to deploy both locally and integrate them to run large language models (LLMs) on your machine. 


### Demo

<video width="500" controls>
  <source src="/assets/img/2025-03-13/final Screen Recording 2025-03-13 at 19.42.37.mov" type="video/mp4">
</video>


<video width="500" controls>
  <source src="/assets/img/2025-03-13/final Screen Recording 2025-03-13 at 19.53.30.mov" type="video/mp4">
</video>



### Setup 

#### Prerequisites

Before starting, ensure you have:
Docker: Installed and running (required for Dify).

Docker Compose: For managing Dify’s multi-container setup.

Hardware: A machine with at least 8GB RAM (more for larger models) and sufficient storage.

Operating System: macOS, Windows, or Linux (Ollama and Dify support all three).

####  Step 1: Install Ollama

Ollama lets you run LLMs locally with a simple setup.
Download Ollama:
Visit ollama.com/download and grab the installer for your OS.

For Linux, you can run:
bash

curl -fsSL https://ollama.com/install.sh | sh

Verify Installation:
Open a terminal and run:
bash

ollama

If installed correctly, you’ll see usage instructions.

Pull a Model:
Choose a model (e.g., Llama 3 or Mistral). For a lightweight option, try gemma:2b:
bash

ollama pull gemma:2b

This downloads the model to your machine.

Run Ollama:
Start the Ollama service:
bash

ollama serve

It will run an API server at http://localhost:11434. Keep this terminal open.

####  Step 2: Install Dify

Dify is an open-source platform for building AI applications, and we’ll deploy it using Docker.
Clone the Dify Repository:
In a new terminal, run:
bash

git clone https://github.com/langgenius/dify.git
cd dify/docker

Configure Environment:
Copy the example environment file:
bash

cp .env.example .env

No changes are needed yet for a basic setup.

Launch Dify:
Start the containers:
bash

docker compose up -d

Wait a few minutes for all services to initialize. Check status with:
bash

docker ps

Access Dify:
Open your browser to http://localhost (or http://your_server_ip if on a remote machine).

Follow the on-screen prompts to create an admin account.

####  Step 3: Integrate Ollama with Dify

Now, connect Dify to your local Ollama instance.
Navigate to Model Providers:
In Dify, go to Settings > Model Providers > Ollama.

Configure Ollama Settings:
Fill in the fields:
Model Name: The model you pulled (e.g., gemma:2b).

Base URL: http://host.docker.internal:11434 (for macOS/Windows with Docker Desktop) or http://localhost:11434 (if Dify and Ollama are on the same non-Docker network). If using Docker, you might need http://ollama:11434 (see troubleshooting below).

Support for Vision: Check if your model supports it (e.g., Llava does; Gemma doesn’t).

Click Save. Dify will test the connection.

Test the Model:
Go to Prompt Eng. in your Dify app.

Select the Ollama provider and your model (e.g., gemma:2b).

Enter a test prompt (e.g., “Hello, how are you?”) and verify the response.

#### Step 4: Troubleshooting

Connection Errors:
If Dify can’t reach Ollama at localhost:11434, it’s likely a Docker networking issue. Use http://host.docker.internal:11434 (macOS/Windows) or ensure both services share a Docker network:
bash

docker network create dify-network
docker network connect dify-network <ollama_container_id>

Update docker-compose.yml in Dify to join this network.

Model Not Responding:
Ensure ollama serve is running and the model is pulled (ollama list to check).

Performance:
Larger models (e.g., Llama 3 70B) need more RAM/GPU. Stick to smaller models like gemma:2b or mistral:7b for modest hardware.

####  Step 5: Running Your Setup

Keep Services Running:
Ollama: ollama serve in one terminal.

Dify: docker compose up -d in the dify/docker directory.

Use Dify:
Build workflows or chatbots in Dify using your local Ollama model. Explore features like RAG or agent capabilities.

Optional: Offline Setup
If you need to run this without internet:
Pre-download Docker images for Dify (docker pull each image listed in docker-compose.yml).

Pull Ollama models beforehand (ollama pull <model>).

Deploy on an air-gapped machine with all files transferred manually.


### Note 


Setting environment variables on Mac
If Ollama is run as a macOS application, environment variables should be set using launchctl:

For each environment variable, call launchctl setenv.

Copy
launchctl setenv OLLAMA_HOST "0.0.0.0"
Restart Ollama application.

If the above steps are ineffective, you can use the following method:

The issue lies within Docker itself, and to access the Docker host.
you should connect to host.docker.internal. Therefore, replacing localhost with host.docker.internal in the service will make it work effectively.

Copy
http://host.docker.internal:11434