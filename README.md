# Project Setup

## Requirements

This project requires the following Python packages:

- `streamlit`

## Installation

To get started with the project, follow the steps below:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Yema7D/docs.git
cd docs
```

### 2. Create a Virtual Environment

It's a good practice to create a virtual environment for your project. This helps to manage dependencies and avoid conflicts with other projects.

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
```bash
.\venv\Scripts\activate
```

- On macOS and Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using pip and the requirements.txt file:

- On Develeppement Mode:
```bash
pip install -r requirements.txt
```

- On Production Mode:
```bash
pip install -r requirements.txt
```


## Running the Project

Once everything is set up, you can run your project using the following command:

```bash
streamlit run main.py
```


## Additional Information

### Selenium Setup

If you are using Selenium for browser automation, you might need to download a WebDriver (e.g., ChromeDriver, GeckoDriver) that matches your browser version.

- **ChromeDriver**: [Download here](https://developer.chrome.com/docs/chromedriver/downloads)
- **GeckoDriver**: [Download here](https://sourceforge.net/projects/geckodriver.mirror/)