# PAN Card Tampering Detection

A Flask web application that detects tampering in PAN (Permanent Account Number) cards using image similarity analysis.

## Features
- Upload PAN card images for tampering detection
- Structural Similarity (SSIM) analysis
- Real-time detection results
- Responsive UI with gradient design

---

## Local Setup (Windows)

### Prerequisites
- Windows 10 / 11
- Python 3.10+
- Command Prompt / PowerShell

### Installation

1. **Install Python**
   Download from: https://www.python.org/downloads/
   ```bash
   python --version
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Access in Browser**
   - Application: http://localhost:5000/
   - Upload a PAN card image to test

6. **Stop Server**
   Press CTRL + C

---

## Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Git initialized
- Heroku account

### Deployment Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

4. **View Logs**
   ```bash
   heroku logs --tail
   ```

5. **Access Your App**
   ```bash
   heroku open
   ```

### Important Files for Heroku
- `Procfile` - Specifies how Heroku runs the app (uses gunicorn)
- `runtime.txt` - Specifies Python version (3.10.13)
- `requirements.txt` - Lists all dependencies with pinned versions

### Troubleshooting Heroku Issues

**App crashes after deployment?**
- Check logs: `heroku logs --tail`
- Verify PORT environment variable is used (app.py handles this)
- Ensure `Procfile` uses `gunicorn app:app`

**Static files not loading?**
- Flask serves static files in `/static` folder
- Ensure CSS and JS are in the correct directory

**Reference image missing?**
- Original PAN image must be at: `model/original_pan.jpg`
- Verify during deployment: `git push heroku main --verbose`

# Folder Structure

pan_tampering_app/
│
├── app.py
├── model/
│   └── original_pan.jpg        # genuine PAN template
│
├── static/
│   ├── styles.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── requirements.txt
└── README.md

# How to Run (Windows)

```bash
cd pan_tampering_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```