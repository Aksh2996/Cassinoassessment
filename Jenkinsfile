pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
        REPORT_DIR = "${WORKSPACE}\\reports"
        LOG_DIR = "${WORKSPACE}\\logs"
    }

    stages {
        stage('Setup Python Virtualenv') {
            steps {
                script {
                    if (!fileExists("${VENV_DIR}")) {
                        bat "python -m venv ${VENV_DIR}"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                ${VENV_DIR}\\Scripts\\pip install --upgrade pip
                ${VENV_DIR}\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                mkdir ${REPORT_DIR} 2>nul
                mkdir ${LOG_DIR} 2>nul
                ${VENV_DIR}\\Scripts\\pytest -n auto --html=${REPORT_DIR}\\report.html --self-contained-html
                """
            }
        }

        stage('Archive Reports and Logs') {
            steps {
                archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
                archiveArtifacts artifacts: 'logs/*.log', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
