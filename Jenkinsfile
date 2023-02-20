pipeline {
    agent { 
        node {
            label 'docker-agent-alpine'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Brad
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
        
        stage('Upload') {
            steps {
                // some instructions here
                office365ConnectorSend webhookUrl: 'https://conutigmbh.webhook.office.com/webhookb2/ec3ffa68-b88d-43ca-b3da-8e8b4da731b7@41e14d32-8bd5-48a3-b1f9-dfa440b0d9cf/IncomingWebhook/77a2460083cf45bcb06f0f2233801fe1/a0ef9e80-52f7-4579-8532-c5560ca33e6c',
                    message: 'Application has been [deployed]',
                    status: 'Success'
            }
        }
    }
}
