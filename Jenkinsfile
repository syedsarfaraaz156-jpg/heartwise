pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/syedsarfaraaz156-jpg/heartwise.git'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t heartwise:latest .'
            }
        }

        stage('Test Container') {
            steps {
                withCredentials([string(credentialsId: 'openrouter-api-key', variable: 'OPENROUTER_API_KEY')]) {
                    bat '''
                        docker rm -f heartwise-test 2>NUL || exit /B 0
                        docker run -d --name heartwise-test -p 5001:5000 -e OPENROUTER_API_KEY="%OPENROUTER_API_KEY%" heartwise:latest
                        powershell -Command "Start-Sleep -Seconds 5"
                        docker ps -a
                        docker logs heartwise-test
                        curl http://localhost:5001
                    '''
                }
            }
        }

        stage('Cleanup') {
            steps {
                bat 'docker rm -f heartwise-test'
            }
        }
    }
}
