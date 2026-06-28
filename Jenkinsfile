pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('Dockerhub')
        IMAGE_NAME = 'rashidali007/flask-dockerapp'
        SONAR_PROJECT_KEY='flask-dockerapp'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'Github_account',
                    url: 'https://github.com/rashid-007/flask-dockerapp.git',
                    branch: 'main'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
			/opt/sonar-scanner/bin/sonar-scanner \
			-Dsonar.projectKey=${SONAR_PROJECT_KEY} \
			-Dsonar.sources=. \
			-Dsonar.host.url=http://sonarqube:9000
                 
                       '''
                }
            }
        }
	stage('Quality Gate') {
	    steps {
		timeout(time: 2, unit: 'MINUTES') {
		    waitForQualityGate abortPipeline: true
		}
            }
	}

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker stop flask-app || true'
                sh 'docker rm flask-app || true'
                sh 'docker run -d -p 4000:4000 --name flask-app ${IMAGE_NAME}:${BUILD_NUMBER}'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check the logs.'
        }
    }
}
