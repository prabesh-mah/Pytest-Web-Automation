<img src="https://miro.medium.com/v2/resize:fit:786/format:webp/1*B-994Z0iTjHzgMCu5YhnOg.png" alt="Selenium Logo" style="max-width:100%;">


# Web Automation 

This project is about web automation on [Nepse Alpha](https://www.nepsealpha.com/) using `Python Selenium Webdriver` with `POM` design pattern and `Pytest` Framework with `HTML` reporting. 

## Requirements

- [git](https://git-scm.com/downloads)
- [python, pip](https://www.python.org/downloads/)
- [virtualenv](https://pypi.org/project/virtualenv/)
- [selenium](https://pypi.org/project/selenium/)
- [undetected-chromedriver](https://pypi.org/project/undetected-chromedriver/)
- [pytest](https://pypi.org/project/pytest/)
- [pytest-order](https://pypi.org/project/pytest-order/)
- [pytest-timeout](https://pypi.org/project/pytest-timeout/)

## Requirements Explaination in Brief: 
- `undetected-chromedriver` : This package is an optimized Selenium Chromedriver patch that does not trigger anti-bot services. It’s designed to not be detected by services like CloudFlare, Imperva, hCaptcha, and others.
- `pytest-order` : It is a pytest plugin that allows you to customize the order in which your tests are run
- `pytest-timeout` : It is a pytest plugin that interrupts and terminates tests that exceed a specified duration.
- `@pytest.mark.smoke` : It is a custom marker used in the pytest framework for Python. 

## What are tested in this project

- Toggle between dark and light theme
- About Nepse Alpha section
- Advertise with us section
- Search functionality 
- Facebook Embed
- Page Redirection
- Form fill up
- Tabs
- etc

## How To Setup This Project

To setup this project on your PC, download this project as a Zip file via. GitHub link or use `git clone`, below are the detailed steps:

**Step 1**: Use below command to ensure that all requirements have been installed.

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

**Step 5**: Run the following command in the terminal to install the virtual environment, allowing us to install the essential libraries on the virtual environment (Optional). 

```
pip install virtualenv
```

**Step 6**: Enter the command below to create a `Virtual Environment`. ** NOTE **: `venv` is the name of `virtual environment`, name can be anything.

```
virtualenv venv
```

**Step 7**: Below are the commands to activate & deactivate the `Virtual Environment`.

```
venv\Scripts\activate
``` 
```
deactivate
```

**Step 8**: After activating the virtual environment, install the necessary requirements for this project using.

```
pip install -r requirements.txt
```

## Usage

**# 1**: To run tests in pytest based on `custom markers`, you can use the `-m` option followed by the marker name. Here are examples for running tests with the `smoke` and `high_priority markers`:
```
pytest -m smoke 
```
```
pytest -m high_priority 
```
## Screenshot of HTML report
<img src="screenshot\Smoke-Test-Report.png" alt="HTML report" style="max-width:100%">

## Video of Smoke Test
[Watch the video](https://drive.proton.me/urls/03A3XZSAA4#XQIZbfINk3Pd)

**# 2**: To run all test methods and generate an `HTML report` simultaneously, you can use the following command:

```
pytest -vs --html='report.html' 
```

where, 
- `-v` : verbose, provide more detailed output.
- `-s`: stdout, allow print statement to be displayed.
- `--html='report.html'`: This option generate an HTML report with file name report.html.

## Screenshot of HTML report
<img src="screenshot\HTML-Report.png" alt="HTML report" style="max-width:100%">

## Video of all test
[Watch the video](https://drive.proton.me/urls/7HRV0R3X6W#1qGjl68TqliG)

