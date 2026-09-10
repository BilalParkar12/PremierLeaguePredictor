# Premier League Predictor

A Flask application that collects historical match results to predict the scores of upcoming Premier League matches.

### Tech Stack
- Frontend - HTML (displays web pages), CSS (styles the web pages with colours)
- Backend - Python (score prediction for each team), Flask (framework to combine HTML and Python into one Python file)
- Modules - Pandas (collect historical match results from a CSV file), NumPy (convert data collected from a CSV file into an array)

Follow these steps to set up a virtual environment and run the application:

### 1. Clone the repository
```
git clone https://github.com/BilalParkar12/PremierLeaguePredictor.git
```
### 2. Navigate to the folder
```
cd PremierLeaguePredictor
```

### 3. Set up the virtual environment
Windows (PowerShell)
```
py -m venv virtual_env
```
macOS
```
python3 -m venv virtual_env
```

### 4. Enable the Activate.ps1 script (Windows PowerShell)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 5. Activate the virtual environment
Windows (PowerShell)
```
virtual_env\Scripts\Activate.ps1
```
macOS
```
source virtual_env/bin/activate
```

### 6. Install modules
Windows (PowerShell)
```
pip install flask
pip install numpy
pip install pandas
```
macOS
```
pip3 install flask
pip3 install numpy
pip3 install pandas
```

### 7. Usage
Windows
```
python PLPredictor.py
```
macOS
```
python3 PLPredictor.py
```

### 8. View in browser
Open Google Chrome and copy and paste the address shown.

### Features
- User Capabilities - users can select a game for the next set of upcoming matches, then see the predicted scoreline for the match selected
- Score Prediction - uses a Poisson model to predict the number of goals each team will score
