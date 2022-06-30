from fastapi import FastAPI
from enum import Enum


# Game teams Enum Model 
class Team(str, Enum):
    team_1 = "home"
    team_2 = "away"

# creat refference to fastapi 
app=FastAPI()

# initial score data store
score = {Team.team_1: 0 ,Team.team_2: 0}


# set the goals for team, at one can set for 1 team from enum teams
#curl -X 'POST' \
#  'http://127.0.0.1:8000/goal?team=away' \
#  -H 'accept: application/json' \
#  -d ''
#
@app.post('/goal')
def set_goal(team:Team): 
    if team==Team.team_1:
        score[Team.team_1]=score[Team.team_1]+1
        return score
    elif team==Team.team_2:
        score[Team.team_2]=score[Team.team_2]+1
        return score
    else:
        return 'Invalid team'
     

# Get current score of the Game
#curl -X 'GET' \
#  'http://127.0.0.1:8000/score' \
#  -H 'accept: application/json'
@app.get('/score')
def get_score():
    return score


    

