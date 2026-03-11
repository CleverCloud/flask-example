# Flask Example Application on Clever Cloud

[![Clever Cloud - PaaS](https://img.shields.io/badge/Clever%20Cloud-PaaS-orange)](https://clever-cloud.com)

This is a minimal Flask application ready to deploy on Clever Cloud.

## About the Application

This application provides simple HTTP endpoints:
- `/` - Returns "Hello world!"
- `/headers` - Returns the request headers
- `/pyver` - Returns the Python version

## Technology Stack

- [Flask](https://flask.palletsprojects.com/) 3.1 - A lightweight Python web framework
- [Gunicorn](https://gunicorn.org/) 23 - A Python WSGI HTTP server
- Python 3

## Prerequisites

- Python 3
- pip

## Running the Application Locally

```bash
pip install -r requirements.txt
flask run
```

The application will be accessible at http://localhost:5000.

## Deploying on Clever Cloud

You have two options to deploy your Flask application on Clever Cloud: using the Web Console or using the Clever Tools CLI.

### Option 1: Deploy using the Web Console

#### 1. Create an account on Clever Cloud

If you don't already have an account, go to the [Clever Cloud console](https://console.clever-cloud.com/) and follow the registration instructions.

#### 2. Set up your application on Clever Cloud

1. Log in to the [Clever Cloud console](https://console.clever-cloud.com/)
2. Click on "Create" and select "An application"
3. Choose "Python" as the runtime environment
4. Configure your application settings (name, region, etc.)

#### 3. Configure Environment Variables

Add the following environment variables in the Clever Cloud console:

| Variable | Value | Description |
|----------|-------|-------------|
| `CC_PYTHON_MODULE` | `app:app` | The WSGI module to run (`file:flask_app`) |
| `CC_PYTHON_BACKEND` | `gunicorn` | The WSGI HTTP server to use |

#### 4. Deploy Your Application

You can deploy your application using Git:

```bash
# Add Clever Cloud as a remote repository
git remote add clever git+ssh://git@push-par-clevercloud-customers.services.clever-cloud.com/app_<your-app-id>.git

# Push your code to deploy
git push clever master
```

### Option 2: Deploy using Clever Tools CLI

#### 1. Install Clever Tools

Install the Clever Tools CLI following the [official documentation](https://www.clever-cloud.com/doc/clever-tools/getting_started/):

```bash
# Using npm
npm install -g clever-tools

# Or using Homebrew (macOS)
brew install clever-tools
```

#### 2. Log in to your Clever Cloud account

```bash
clever login
```

#### 3. Create a new application

```bash
# Step 1: Initialize the current directory as a Clever Cloud application
clever create --type python <YOUR_APP_NAME>

# Step 2: Add your domain (optional but recommended)
clever domain add <YOUR_DOMAIN_NAME>

# Step 3: Set the required environment variables
clever env set CC_PYTHON_MODULE app:app
clever env set CC_PYTHON_BACKEND gunicorn
```

#### 4. Deploy your application

```bash
clever deploy
```

#### 5. Open your application in a browser

Once deployed, you can access your application at `https://<YOUR_DOMAIN_NAME>/`.

### Monitoring Your Application

Once deployed, you can monitor your application through:

- **Web Console**: The Clever Cloud console provides logs, metrics, and other tools to help you manage your application.
- **CLI**: Use `clever logs` to view application logs and `clever status` to check the status of your application.

## Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gunicorn Documentation](https://gunicorn.org/)
- [Clever Cloud Python Documentation](https://www.clever-cloud.com/developers/doc/applications/python/)
