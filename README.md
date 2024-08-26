<img src="https://miro.medium.com/v2/resize:fit:786/format:webp/1*B-994Z0iTjHzgMCu5YhnOg.png" alt="Selenium Logo" style="max-width:100%;">


# Web Automation 

I automated the [Nepse Alpha](https://www.nepsealpha.com/) website using `Python with Selenium WebDriver`, employing the `Page Object Model (POM)` design pattern for better maintainability and scalability. I utilized the `pytest` framework for testing, which allowed me to efficiently run tests and generate detailed HTML reports. Additionally, I incorporated various `pytest plugins`, such as `pytest-order` for controlling test execution order and `pytest-timeout` to manage test execution time. I also implemented `custom markers`, including `smoke`, `regression`, `high_priority`, `medium_priority`, and `low_priority`, to categorize and prioritize tests effectively.

## Requirements

- [git](https://git-scm.com/downloads)
- [python, pip](https://www.python.org/downloads/)
- [virtualenv](https://pypi.org/project/virtualenv/)
- [selenium](https://pypi.org/project/selenium/)
- [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver/)
- [pytest](https://pypi.org/project/pytest/)
- [pytest-order](https://pypi.org/project/pytest-order/)
- [pytest-timeout](https://pypi.org/project/pytest-timeout/)
- [pandas](https://pypi.org/project/pandas/)

## Requirements Explaination in Brief: 
- `undetected-chromedriver` : This package is an optimized Selenium Chromedriver patch that does not trigger anti-bot services. It’s designed to not be detected by services like CloudFlare, Imperva, hCaptcha, and others.
- `pytest-order` : It is a pytest plugin that allows you to customize the order in which your tests are run
- `pytest-timeout` : It is a pytest plugin that interrupts and terminates tests that exceed a specified duration.
- `@pytest.mark.smoke` : It is a custom marker used in the pytest framework for Python. 

## What are tested in this project

- HTML Table Scraping
- File Download
- Tabs 
- Search functionality 
- Facebook Embed
- Toggle between dark and light theme
- About Nepse Alpha section
- Advertise with us section
- Form fillup
- etc

## How To Setup This Project

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

**Step 6**: Enter the command below to create a `Virtual Environment`. ** NOTE **: `venv` is the name of `virtual environment`, name can be anything.

```
virtualenv venv
```

**Step 7**: Commands to activate & deactivate the `Virtual Environment`.

```
venv\Scripts\activate
deactivate
```

**Step 8**: After activating the virtual environment, install the necessary requirements for this project using.

```
pip install -r requirements.txt
```

## Usage

**# 1**: To run tests in pytest based on `custom markers`, you can use the `-m` option followed by the marker name. Below are the commands and markers used for this project.
```
pytest -m smoke 
pytest -m regression
pytest -m low_priority 
pytest -m medium_priority 
pytest -m high_priority 
```

## Screenshot of Smoke Test HTML report
<img src="screenshot\HTML-Report.png" alt="HTML report" style="max-width:100%">


## Video of Smoke Test
[Watch the video](https://drive.proton.me/urls/03A3XZSAA4#XQIZbfINk3Pd)

**# 2**: To run all test methods and generate an `HTML report`.

```
pytest -vs --html='report.html' 
```

where, 
- `-v` : verbose, provide more detailed output.
- `-s`: stdout, allow print statement to be displayed.
- `--html='report.html'`: This option generate an HTML report with file name report.html.