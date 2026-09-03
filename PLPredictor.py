from flask import Flask, request
import pandas as pd
import numpy as np
import math
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

def output_prediction(HomeTeam, AwayTeam, HomeTeamScore, AwayTeamScore):
    return f"""
        <!DOCTYPE html>
        <head>
        </head>
        <body style="background-color: #0e0e3f;">
        <p style="color: white; font-family: Arial, Helvetica, sans-serif; text-align: center; font-size: 40px;">{HomeTeam} {HomeTeamScore} - {AwayTeamScore} {AwayTeam}</p>
        </body>
        </html>
    """

@app.route('/')
def html():
    return """
        <!DOCTYPE html>
        <html>
        <head>
            <h1 style="color: white; text-align: center; font-size: 30px; font: Lucida Console; font-weight: bold;">Premier League Predictor</h1>
        </head>
        <body style="background-color: #0e0e3f;">
        <p style="color: white">This website predicts the results of upcoming Premier League games. Select the game you want to find predictions of.</p>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Chelsea&AwayTeam=Everton'">Chelsea vs Everton</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Liverpool&AwayTeam=Brighton'">Liverpool vs Brighton</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Burnley&AwayTeam=Fulham'">Burnley vs Fulham</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Arsenal&AwayTeam=Wolves'">Arsenal vs Wolves</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Crystal%20Palace&AwayTeam=Man%20City'">Crystal Palace vs Man City</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Sunderland&AwayTeam=Newcastle'">Sunderland vs Newcastle</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Nott%27m%20Forest&AwayTeam=Tottenham'">Nott'm Forest vs Tottenham</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=West%20Ham&AwayTeam=Aston%20Villa'">West Ham vs Aston Villa</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Brentford&AwayTeam=Leeds%20United'">Brentford vs Leeds United</button><br><br>
        <button style="background-color: #7FFF00; color: black; border-radius: 12px;" onclick="window.location.href='/prediction?HomeTeam=Man%20United&AwayTeam=Bournemouth'">Man United vs Bournemouth</button>

        </body>
        </html>
    """
@app.route('/prediction')
def prediction():
    HomeTeam = request.args.get('HomeTeam')
    AwayTeam = request.args.get('AwayTeam')
    data = pd.read_csv('results.csv', encoding="latin1")

    HomeGoalsScored = data[data['HomeTeam'] == HomeTeam]['FullTimeHomeGoals'].mean()
    HomeGoalsConceded = data[data['HomeTeam'] == HomeTeam]['FullTimeAwayGoals'].mean()
    AwayGoalsScored = data[data['AwayTeam'] == AwayTeam]['FullTimeAwayGoals'].mean()
    AwayGoalsConceded = data[data['AwayTeam'] == AwayTeam]['FullTimeHomeGoals'].mean()
    HomeAdvantage = np.log(HomeGoalsScored) - np.log(AwayGoalsScored)
    
    lambda_home = np.exp(np.log(HomeGoalsScored) + np.log(AwayGoalsConceded) + HomeAdvantage)
    lambda_away = np.exp(np.log(AwayGoalsScored) + np.log(HomeGoalsConceded))

    home_probability = []
    away_probability = []

    for i in range(0, 6):
        HomeProbability = (np.exp(-lambda_home) * (lambda_home**i))/math.factorial(i)
        home_probability.append(HomeProbability)

        AwayProbability = (np.exp(-lambda_away) * (lambda_away**i))/math.factorial(i)
        away_probability.append(AwayProbability)
        

    home_score = home_probability.index(max(home_probability))
    away_score = away_probability.index(max(away_probability))

    return output_prediction(HomeTeam, AwayTeam, home_score, away_score)


if __name__ == '__main__':
    app.run()
