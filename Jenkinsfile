pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "sonarqube-demo"
        SONAR_PROJECT_KEY = "jaivivs_sonarqube-demo"
        SONAR_ORG = "jaivivs"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/JaivivS/sonarqube-demo.git'
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat """
                        sonar-scanner ^
                        -Dsonar.projectKey=%SONAR_PROJECT_KEY% ^
                        -Dsonar.organization=%SONAR_ORG% ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=https://sonarcloud.io
                    """
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% ."
                    echo "Docker image built successfully!"
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline succeeded! Docker image created.'
        }
        failure {
            echo 'Pipeline failed! Quality gate not passed.'
        }
    }
}
