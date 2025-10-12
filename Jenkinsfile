pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest -n 4 --html=reports/report.html --self-contained-html'
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/report.html', fingerprint: true
            }
        }
    }
}
