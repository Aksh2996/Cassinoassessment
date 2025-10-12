pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        REPORT_DIR = "${WORKSPACE}/reports"
        LOG_DIR = "${WORKSPACE}/logs"
    }

    stages {
        stage('Setup Python Virtualenv') {
            steps {
                script {
                    // Create virtual environment if not exists
                    if (!fileExists("${VENV_DIR}")) {
                        sh "python -m venv ${VENV_DIR}"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    ${VENV_DIR}/Scripts/pip install --upgrade pip
                    ${VENV_DIR}/Scripts/pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh """
                    mkdir -p ${REPORT_DIR} ${LOG_DIR}
                    ${VENV_DIR}/Scripts/pytest -n auto --html=${REPORT_DIR}/report.html --self-contained-html
                    """
                }
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
            junit '**/reports/*.xml' // If you convert pytest output to JUnit XML
            echo 'Pipeline finished!'
        }
    }
}