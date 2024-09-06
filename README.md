<img src="https://miro.medium.com/v2/resize:fit:786/format:webp/1*B-994Z0iTjHzgMCu5YhnOg.png" alt="Selenium Logo" style="max-width:100%;">


# Project Description 

Automated the [Nepse Alpha](https://www.nepsealpha.com/) website using `Python with Selenium WebDriver`, implementing the `Page Object Model (POM)` design pattern for enhanced maintainability and scalability. Utilized the `pytest framework` for testing, enabling efficient test execution and detailed `HTML report` generation. Incorporated various `pytest plugins`, including `pytest-order` for controlling test execution order and `pytest-timeout` for managing test execution time. Implemented `custom markers` such as `smoke`, `regression`, `high_priority`, `medium_priority`, and `low_priority` to effectively categorize and prioritize tests.

# Requirements

- [git](https://git-scm.com/downloads)
- [python, pip](https://www.python.org/downloads/)
- [virtualenv](https://pypi.org/project/virtualenv/)
- [selenium](https://pypi.org/project/selenium/)
- [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver/)
- [pytest](https://pypi.org/project/pytest/)
- [pytest-order](https://pypi.org/project/pytest-order/)
- [pytest-timeout](https://pypi.org/project/pytest-timeout/)
- [pytest-html](https://pypi.org/project/pytest-html/)
- [pandas](https://pypi.org/project/pandas/)

## Requirements Explaination in Brief: 
- `undetected-chromedriver` : This package is an optimized Selenium Chromedriver patch that does not trigger anti-bot services. It’s designed to not be detected by services like CloudFlare, Imperva, hCaptcha, and others.
- `pytest-order` : It is a pytest plugin that allows you to customize the order in which your tests are run
- `pytest-timeout` : It is a pytest plugin that interrupts and terminates tests that exceed a specified duration.
- `@pytest.mark.smoke` : It is a custom marker used in the pytest framework for Python. 
- `pandas`: It is used to efficiently scrape HTML tables from web pages and save the extracted data into Excel files using the to_excel() function. 

# What are tested in this project

- HTML Table Scraping
- File Download
- Handled Tabs 
- Search functionality with different combinations
- Facebook Embed
- Toggle between dark and light theme
- About Nepse Alpha section
- Advertise with us section
- Form fillup
- etc

# How To Setup This Project

**Step 1**: Use the command below to ensure that all softwares have been installed.

```
python --version
pip --version
git --version
```

**Step 2**: Then use the `cd` command to navigate to the directory where you wish to be download this project. 

```
cd folder-name
```

**Step 3**: Now, use the `git clone` command to clone this project into that folder.

```
git clone https://github.com/prabesh-mah/Pytest-Web-Automation
```

**Step 4**: Once the project has been cloned, open the project using `Visual Studio Code` or any other IDE.

**Step 5**: Run the following command in the terminal to install the virtual environment, to install the essential libraries in an isolated environment. 

```
pip install virtualenv
```

**Step 6**: Enter the command below to create a `Virtual Environment`. **NOTE**: `venv` is the name of `virtual environment`, name can be anything.

```
virtualenv venv
```

**Step 7**: Commands to activate and deactivate the `Virtual Environment`.

```
venv\Scripts\activate
```
```
deactivate
```

**Step 8**: After activating the virtual environment, install the necessary dependencies for this project.

```
pip install -r requirements.txt --upgrade
```

# Usage

**# 1**: To run tests in pytest based on `custom markers`, you can use the `-m` option followed by the marker name. Below are the commands and markers that were used in this project.
```
pytest -m smoke 
pytest -m regression
pytest -m low_priority 
pytest -m medium_priority 
pytest -m high_priority 
```

**# 2**: To run all test methods and generate an `HTML report` at the end. 

```
pytest -vs --html='report.html' --self-contained-html 
```

where, 
- `-v` : verbose, provide more detailed output.
- `-s`: stdout, allow print statement to be displayed.
- `--html='report.html'`: This option generate an HTML report with file name **report.html**.
- `--self-contained-html`: Generates a single HTML file instead of HTML and CSS file separately.

## Full Code Execution Video
Watch the full code execution video.
[Here](https://drive.proton.me/urls/82HTY4XF5R#vRnv8rS7NldW)

## Integration with Jenkins via. Declarative Pipeline

Wrote a `declarative Jenkins pipeline` that automates the process of cloning the `feature branch` from the `GitHub` repository `Pytest-Web-Automation`. The pipeline begins by creating a virtual environment named `venv` to isolate project dependencies, followed by activating the environment and installing the required Python packages from `requirements.txt`. It then confirms the installation of `Python, pip, git, and pytest` by checking their versions. After ensuring that all necessary tools are in place, the pipeline executes one of the `test` using `pytest` and generates an `HTML report` saved in `jenkins_reports/test_reports.html`. Finally, it copies the generated test report to the user's desktop and cleans up by deleting the original report folder from the Jenkins workspace.

### Jenkins Declarative Pipeline Code

```
pipeline {

    agent any

    stages {
        stage("Clone Repository") {
            steps {
                // Clone the GitHub repository where branch is 'feature'
                git branch: 'feature', changelog: false, poll: false, url: 'https://github.com/prabesh-mah/Pytest-Web-Automation'
            }
        } // end of stage 1

        stage("Setup Python Environment") {
            steps {
                // Create virtual envonment named 'venv'
                bat '''
                    python -m venv venv
                '''
            }
        } // end of stage 2

        stage("Install Dependencies") {
            steps {
                // Activate venv & Install required dependencies
                bat '''
                    call "venv\\Scripts\\activate.bat" ^
                    && pip install -r requirements.txt --upgrade
                '''
            }
        } // end of stage 3

        stage("Verify Dependencies") {
            steps {
                // Activate venv & Verify Install Dependencies
                bat '''
                    call "venv\\Scripts\\activate.bat" ^
                    && python --version && pip --version && git --version && python -m pytest --version
                '''
            }
        } // end of stage 4


        stage("Run Test and Generate Report") {
            steps {
                // Run the tests and generate HTML report
                bat '''
                    call "venv\\Scripts\\activate.bat" ^
                    && pytest -vs .\\tests\\HomePageTest\\playstore_redirection_test.py --html=jenkins_reports/test_reports.html
                '''
            }
        } // end of stage 5

        stage("Copy Test Report To Desktop") {
            steps {
                script {
                    // Construct the path to the desktop
                    def desktopPath = "C:\\Users\\Wicked Man\\Desktop\\"
                    def sourceReportPath = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\GitHub\\Pytest-GitHub\\jenkins_reports"
                    def destinationReportPath = "${desktopPath}jenkins_reports"

                    // Copy the report folder to the desktop
                    bat "xcopy \"${sourceReportPath}\" \"${destinationReportPath}\" /E /I /Y"

                    // Check if the copy was successful
                    if (fileExists(destinationReportPath)) {
                        echo "Reports copied successfully to ${destinationReportPath}"

                        // Delete the original reports from the source folder
                        bat "rd /S /Q \"${sourceReportPath}\""
                        echo "Original reports deleted from ${sourceReportPath}"
                    } else {
                        error "Failed to copy reports to the desktop."
                    }
                }
            }

        } // end of stage 6

    } // end of all stages

} // end of pipeline

```

## Integration with Jenkins Video
As for this Demo only one test case file is executed on this video i.e. `fb_embed_test.py`. [Here](https://drive.proton.me/urls/DCNSZJW420#jCU2TRaJqWMe)
