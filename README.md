# Flask Application (Windows Setup)

## Prerequisites
- Windows 10 / 11
- Python 3.10+
- Command Prompt / PowerShell

## Step 1: Install Python
Download from:
https://www.python.org/downloads/

✅ Check installation:
python --version

## Step 2: Create Virtual Environment
python -m venv venv

Activate:
venv\Scripts\activate

## Step 3: Install Dependencies
pip install -r requirements.txt

## Step 4: Run the Application
python app.py

## Step 5: Access in Browser
http://127.0.0.1:5000/

Health API:
http://127.0.0.1:5000/api/health

## Stop Server
Press CTRL + C
