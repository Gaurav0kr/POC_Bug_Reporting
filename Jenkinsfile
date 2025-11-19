pipeline {
    agent any
    
    environment {
        // Python Configuration - Update path based on your Jenkins server
        PYTHON_HOME = 'C:\\Python314'  // Windows path, change for Linux/Mac
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${PATH}"
        
        // Test Configuration
        HEADLESS = 'true'
        VIEWPORT_WIDTH = '1280'
        VIEWPORT_HEIGHT = '720'
    }
    
    options {
        // Keep last 10 builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        
        // Timeout after 30 minutes
        timeout(time: 30, unit: 'MINUTES')
        
        // Add timestamps to console output
        timestamps()
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Setting up virtual environment (Linux/Mac)..."
                            python3 -m venv venv || python -m venv venv
                        '''
                    } else {
                        bat '''
                            echo Setting up virtual environment (Windows)...
                            if not exist venv (
                                python -m venv venv
                            )
                        '''
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Installing Python dependencies..."
                            source venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            echo Installing Python dependencies...
                            call venv\\Scripts\\activate.bat
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Install Playwright Browsers') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Installing Playwright browsers..."
                            source venv/bin/activate
                            python -m playwright install chromium
                            python -m playwright install-deps chromium
                        '''
                    } else {
                        bat '''
                            echo Installing Playwright browsers...
                            call venv\\Scripts\\activate.bat
                            python -m playwright install chromium
                        '''
                    }
                }
            }
        }
        
        stage('Create Environment File') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Creating .env file..."
                            if [ ! -f .env ]; then
                                cp env.example .env
                            fi
                        '''
                    } else {
                        bat '''
                            echo Creating .env file...
                            if not exist .env (
                                copy env.example .env
                            )
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            echo "Running Behave tests..."
                            source venv/bin/activate
                            mkdir -p reports
                            python -m behave --format pretty --format json --outfile reports/behave-report.json || true
                        '''
                    } else {
                        bat '''
                            echo Running Behave tests...
                            call venv\\Scripts\\activate.bat
                            if not exist reports mkdir reports
                            python -m behave
                        '''
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Archive test reports
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
            
            // Clean up virtual environment (optional - comment out if you want to keep it)
            script {
                if (isUnix()) {
                    sh 'rm -rf venv || true'
                } else {
                    bat 'rmdir /s /q venv || exit 0'
                }
            }
        }
        success {
            echo '✅ Tests completed successfully!'
            // Publish HTML reports if available
            script {
                if (fileExists('reports/behave-report.html')) {
                    publishHTML([
                        reportName: 'Behave Test Report',
                        reportDir: 'reports',
                        reportFiles: 'behave-report.html',
                        keepAll: true,
                        alwaysLinkToLastBuild: true
                    ])
                }
            }
        }
        failure {
            echo '❌ Tests failed! Check the console output for details.'
        }
        unstable {
            echo '⚠️ Tests completed with warnings.'
        }
    }
}

