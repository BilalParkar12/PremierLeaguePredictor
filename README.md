# Premier League Predictor

This Premier League Predictor collects historical match results to predict the scores of upcoming Premier League matches.

### Tech Stack
- Python
- HTML
- CSS
- Flask
- Pandas
- NumPy

### Installation
Windows
```
git clone https://github.com/BilalParkar12/PremierLeaguePredictor.git
cd PremierLeaguePredictor
python -m venv virtual_env
virtual_env\Scripts\activate
pip install flask
pip install numpy
pip install pandas
python PLPredictor.py
```
macOS/Linux
```
git clone https://github.com/BilalParkar12/PremierLeaguePredictor.git
cd PremierLeaguePredictor
python3 -m venv virtual_env
source virtual_env/bin/activate
pip install flask
pip install numpy
pip install pandas
python3 PLPredictor.py
```
### Usage
Windows
```
python PLPredictor.py
```
macOS/Linux
```
python3 PLPredictor.py
```
### Features
- User Capabilities - users can select a game for the next set of upcoming matches, then see the predicted scoreline for the match selected
- Flask - uses Flask to return a HTML page
- Python - uses Python for the score prediction for each team
- Historical match data - stores historical scorelines in a CSV file
- Score Prediction - uses a Poisson model to predict the number of goals each team will score
