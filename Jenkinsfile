pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s devops-demo/app/tests'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    sh 'docker build -t devops-demo:${BUILD_NUMBER} ./devops-demo'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed during execution.'
        }
    }
}