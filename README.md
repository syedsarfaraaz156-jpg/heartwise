# ❤️ HeartWise — AI Relationship Advisor

HeartWise is a simple AI-powered relationship advisor built with Python and Flask.

Users can describe a relationship situation and receive thoughtful, practical and balanced guidance from an AI assistant.

## 🚀 Features

- 💬 Simple relationship advice chatbot
- 🤖 AI-powered responses using OpenRouter
- 🌐 Flask web application
- 🎨 Clean and responsive web interface
- 🐳 Docker-ready application
- 🔐 API key handled through environment variables

## 🛠️ Tech Stack

- Python
- Flask
- OpenRouter API
- HTML/CSS
- Docker
- Git & GitHub
- Jenkins CI/CD
- AWS EC2

## 🏗️ Project Architecture

Developer → GitHub → Jenkins → Docker Build → Docker Container → AWS EC2

## 📁 Project Structure

```text
heartwise/
├── app.py
├── Dockerfile
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── templates/
    └── index.html
```

## ⚙️ Run Locally

Clone the repository:

```bash
git clone https://github.com/syedsarfaraaz156-jpg/heartwise.git
cd heartwise
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the OpenRouter API key.

### Windows PowerShell

```powershell
$env:OPENROUTER_API_KEY="YOUR_API_KEY"
```

Run the application:

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## 🐳 Run with Docker

Build the image:

```bash
docker build -t heartwise .
```

Run the container:

```bash
docker run -d -p 5000:5000 -e OPENROUTER_API_KEY="YOUR_API_KEY" heartwise
```

Open:

```text
http://localhost:5000
```

## 🔐 Security

The OpenRouter API key is not stored in the source code.

It is supplied through the `OPENROUTER_API_KEY` environment variable.

Never commit API keys or other secrets to GitHub.

## 🔄 CI/CD

Jenkins will be used to automate the deployment pipeline:

Developer → Git Push → GitHub → Jenkins → Build → Test → Docker Image → Deploy

## ☁️ Future Improvements

- Jenkins automated CI/CD pipeline
- Docker image publishing
- AWS EC2 deployment
- Application monitoring
- Improved AI conversation experience

## ⚠️ Disclaimer

HeartWise provides general relationship guidance and is not a substitute for professional help.

---

Built as a hands-on DevOps portfolio project.
