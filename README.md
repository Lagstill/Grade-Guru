### Student Performance Predictor

### Introduction
* This is a modular Flask web application that provides a prediction endpoint for an ensemble of machine learning models. It takes input data from a web form and returns the predicted result.

* The project also includes CI/CD using GitHub Actions for automated build, test, and deployment.

#### Preview
![image](https://user-images.githubusercontent.com/22552983/129447571-1b8b9b9a-4b0a-4b9a-8b9a-9b0b0b8b0b0b.png)

### Dataset
The dataset used for this project is the [Student Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) from Kaggle. Which indeed is the data generated from [Royce Kimmons: Understanding digital participation divides](http://roycekimmons.com/tools/generated_data/exams), though in the Kaggle a sample of 1000 rows is provided, here a 9000 rows dataset is used, by the data generator provided by Royce Kimmons, with duplicates removed. 

P.S. The data generator is fictional.

### Project Structure
```bash
├── .ebextensions           # Elastic Beanstalk configuration files
├── .github/workflows 
├── app.py
├── setup.py
├── requirements.txt
├── data
│   ├── data-s.csv
├── notebook
│   ├── EDA.ipynb
│   └── train.ipynb
├── src
│   ├── __init__.py
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│   ├── components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   ├── predit_pipeline.py
├── templates
│   ├── home.html
│   ├── index.html
├── logs
│   ├── daily-wise.log
├── test_app.py
├── .gitignore              # Git ignore file
├── README.md               # Readme file
```

### Getting Started

To get started with the Flask application, follow the steps below:

1. Clone the repository:
```bash
git clone <repository_url>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python app.py
```
4. Access the website through the browser:
```arduino
http://localhost:5000/
```

### CI/CD GitHub Actions 

This project utilizes **GitHub Actions for continuous integration and continuous deployment (CI/CD). The included workflows in the ".github/workflows" directory automate the build, test, and deployment processes.

The CI/CD workflow performs the following tasks:

* On each push or pull request to the main branch, it triggers the workflow.
* The workflow checks out the source code using the actions/checkout action.
* It sets up the Python environment using the actions/setup-python action and installs the required dependencies.
* The code is linted using flake8 and tested using pytest.
* If all the tests pass, the workflow proceeds to deploy the application.

The deployment workflow can be customized based on your deployment target. For example, it can be configured to deploy to AWS Elastic Beanstalk or any other platform. Update the workflow configuration file (deploy.yml) according to your deployment requirements.

### Usage

The Flask application provides the following endpoints:

* GET /: Renders the index page with a web form to input the data.
* POST /predict: Accepts the data from the web form, processes it, and returns the predicted result.

The application expects the following data fields in the web form:

* gender: The gender of the student.
* ethnicity: The race/ethnicity of the student.
parental_level_of_education: The parental level of education.
* lunch: The type of lunch the student has.
* test_preparation_course: Whether the student completed a test preparation course.
* reading_score: The score obtained in the reading test.
* writing_score: The score obtained in the writing test.
* math_score: The score obtained in the math test. (prediction target)

The response from the /predict endpoint will be displayed on the home page via PredictPipeline.









