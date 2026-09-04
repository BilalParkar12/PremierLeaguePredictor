# Premier League Predictor

This Premier League Predictor collects historical match results to predict the scores of upcoming Premier League matches.

### Tech Stack
- Python
- HTML
- CSS
- Flask
- Pandas
- NumPy

Follow these steps to set up a virtual environment and run the application

### 1. Clone the repository
```
git clone https://github.com/BilalParkar12/PremierLeaguePredictor.git
cd PremierLeaguePredictor
```

### 2. Set up the virtual environment
Windows
```
python -m venv virtual_env
virtual_env\Scripts\activate
```
macOS/Linux
```
python3 -m venv virtual_env
source virtual_env/bin/activate
```

### 3. Install modules
Windows
```
pip install flask
pip install numpy
pip install pandas
```
macOS/Linux
```
pip3 install flask
pip3 install numpy
pip3 install pandas
```

### 4. Usage
Windows
```
python PLPredictor.py
```
macOS/Linux
```
python3 PLPredictor.py
```
### 5. View in browser
Open Google Chrome and copy and paste the address shown.

### Features
- User Capabilities - users can select a game for the next set of upcoming matches, then see the predicted scoreline for the match selected
- Flask - uses Flask to return a HTML page
- Python - uses Python for the score prediction for each team
- Historical match data - stores historical scorelines in a CSV file
- Score Prediction - uses a Poisson model to predict the number of goals each team will score
