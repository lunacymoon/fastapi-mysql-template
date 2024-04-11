# Introduction

We are building this template for all backend services later on. 
This is a Python template using FastAPI and SQLAlchemy ORM with mySQL DB, deploying through AWS ECS/EC2.

# Getting Started

1. Installation process:

   - Requirements:

     - Python 3.11
     - Docker
     - poetry
     - pyenv+virtualenv (or any env tool you like)
     - pre-commit

   - Here's an example for local virtual environment setup:
     ```
     pyenv install 3.11.0
     pyenv global 3.11.0
     pyenv virtualenv 3.11.0 backend-service-template
     pyenv activate backend-service-template
     ```
   - Install packages: `pip3 install -r requirements.txt`

2. API references
   - When running your application locally,
     - go to `localhost:5000/docs` for OpenAPI documentation
     - or `http://127.0.0.1:5000/docs` depends on your settings

# Build and Test

    - 'Run and Debug' tool in VSCode
        - When running debugger:
          - Remember to set your python interpreter
          - Add any configuration in launch.json if you need it

# Contribute

1. Please use Pre-commit
   - go `brew install pre-commit` or `pip install pre-commit`
   - like `pre-commit install` after its installation
2. We would love to user Trunk-based git model
3. For branch names and commits, please follow
   - branch name: `{feature/fix/hotfix}/{ticket_number}-{ticket_name}`
     - e.g. `feature/18989-new_repo` (this is a new feature to develop branch)
     - e.g. `fix/18989-model_name_typo` (this is a little bug fix to develop branch)
     - e.g. `hotfix/18989-get_enterprise_activity_error` (this is a bug hotfix to release or master branch)
   - commit name: `[{feature/fix/hotfix}][{ticket_number}] {ticket_name}
     - e.g. `[feature][18989] new repo coming!`
4. To Update Packages:
   - Add new packages:
     ```
     poetry self update
     poetry add {package_name}
     poetry export -f requirements.txt -o requirements.txt --without-hashes --dev
     ```
   - Update dependencies:
     ```
     poetry self update
     poetry lock
     poetry export -f requirements.txt -o requirements.txt --without-hashes --dev
     ```
