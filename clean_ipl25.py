import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("matches.csv")


total_wins = df.groupby("match_winner")["match_id"].count().sort_values(ascending = False)
print(total_wins) 

team1_counts = df['team1'].value_counts()
team2_counts = df['team2'].value_counts()
total_played = (team1_counts + team2_counts).sort_values(ascending=False)
print(total_played)

per_wins = round((total_wins/total_played*100).sort_values(ascending=False),2)
print(per_wins)

total_toss_wins = df.groupby("toss_winner")["match_id"].count().sort_values(ascending=False)
print(total_toss_wins)

per_toss_win = round((total_toss_wins/total_played*100).sort_values(ascending=False),2)
print(per_toss_win)

toss_match_wins = df[df["toss_winner"] == df["match_winner"]].groupby("match_winner")["match_id"].count().sort_values(ascending = False)
print(toss_match_wins)

per_toss_match_win = round((toss_match_wins/total_wins*100).sort_values(ascending=False),2)
print(per_toss_match_win)

potm=df.groupby("player_of_the_match")["match_id"].count().sort_values(ascending=False)
print(potm)

best_bowler=df.groupby("best_bowling")["match_id"].count().sort_values(ascending=False)
print(best_bowler)

best_batsman=df.groupby("top_scorer")["match_id"].count().sort_values(ascending=False)
print(best_batsman)

teams=['PBKS','RCB','GT','DC','MI','SRH','LSG','KKR','CSK','RR']
j_colors=["#DD1F2D","#E63329","#1B2133","#004C97","#004B87","#EE7429","#EB261C","#3A225D","#F9CD05","#EA1A85"]

team_colors = {
    'PBKS': '#DD1F2D',
    'RCB': "#2B2A29",
    'GT': '#1B2133',
    'DC': '#004C97',
    'MI': '#004B87',
    'SRH': '#EE7429',
    'LSG': '#EB261C',
    'KKR': '#3A225D',
    'CSK': '#F9CD05',
    'RR': '#EA1A85'
}

plt.figure(figsize=(10,8))
bar_colors = [team_colors.get(team, 'gray') for team in per_toss_match_win.index]
plt.bar(per_toss_match_win.index,per_toss_match_win.values,color=bar_colors,edgecolor="black")
for i,v in enumerate(per_toss_match_win.values):
    plt.text(i,v+1,str(v)+"%",ha='center',fontweight='bold', fontsize=9)
plt.title('Win Percentage When Winning The Toss (By Team)- IPL 2025', fontsize=15, fontweight='bold')
plt.xlabel('Teams', fontsize=12)
plt.ylabel('Win Percentage (%)', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.xticks(rotation=45)
plt.ylim(0, 100) 
plt.tight_layout()
plt.show()


top_5_bowlers = best_bowler.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_5_bowlers.index[::-1], top_5_bowlers.values[::-1], color="#ab08dcbe", edgecolor='black')

plt.title('Top 5 Bowlers (Most "Best Bowling" Awards) - IPL 2025', fontsize=15, fontweight='bold')
plt.xlabel('Number of Awards', fontsize=12)
plt.ylabel('Bowler Name', fontsize=12)

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


top_5_potm = potm.head(5)
plt.figure(figsize=(10, 6))

plt.barh(top_5_potm.index[::-1], top_5_potm.values[::-1], color="#f1c100db", edgecolor='black')

plt.title('Top 5 Match Winners (Most POTM Awards) - IPL 2025', fontsize=15, fontweight='bold')
plt.xlabel('Number of Awards', fontsize=12)
plt.ylabel('Player Name', fontsize=12)

plt.grid(axis='x', linestyle='dotted', alpha=0.7)

plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))

plt.bar(per_wins.index, per_wins.values, color='team_colors', edgecolor='black')

# NEW LEARNING: Adding Data Labels on top of the bars 
# We loop through the values and place a text label at the top of each bar
for i, v in enumerate(per_wins.values):
    plt.text(i, v + 1, str(v) + '%', ha='center', fontweight='bold', fontsize=9)

plt.title('Win Percentage per Team - IPL 2025', fontsize=15, fontweight='bold')
plt.xlabel('Teams', fontsize=12)
plt.ylabel('Win Percentage (%)', fontsize=12)

plt.xticks(rotation=45)
plt.ylim(0, 75) 

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


bar_colors = [team_colors.get(team, 'gray') for team in per_wins.index]
plt.figure(figsize=(10, 6))
plt.bar(per_wins.index, per_wins.values, color=bar_colors, edgecolor='black')

for i, v in enumerate(per_wins.values):
    plt.text(i, v + 1, str(v) + '%', ha='center', fontweight='bold', fontsize=9)

plt.title('Win Percentage per Team - IPL 2025', fontsize=15, fontweight='bold')
plt.xlabel('Teams', fontsize=12)
plt.ylabel('Win Percentage (%)', fontsize=12)
plt.xticks(rotation=45)
plt.ylim(0, 75) 
plt.grid(axis='y', linestyle='-.', alpha=0.7)
plt.tight_layout()

plt.show()



avg_venue_score = df.groupby('venue')['first_ings_score'].mean().sort_values()
plt.figure(figsize=(10, 6))

plt.barh(avg_venue_score.index, avg_venue_score.values, color='skyblue', edgecolor='black')

plt.title('Average First Innings Score by Venue - IPL 2025', fontsize=14, fontweight='bold')
plt.xlabel('Average Score', fontsize=12)
plt.ylabel('Venue',labelpad=10,fontsize=12)

plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


defending_wins=df['wb_runs'].notna().sum()
chasing_wins=df['wb_wickets'].notna().sum()
my_list=[defending_wins,chasing_wins]
lbl=["Defending Wins","Chasing Wins"]
colors=["#1D96E7","#103EE4"]
plt.figure(figsize=(10,6))
plt.pie(my_list,labels=lbl,colors=colors,explode=[0,0.03],startangle=60,shadow=True,autopct="%1.2f%%")
plt.title("Defending Wins v/s Chasing Wins",fontsize=14,fontweight="extra bold",fontstyle="italic",family = "Arial")
plt.show()

top_5_batsmen = best_batsman.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_5_batsmen.index[::-1], top_5_batsmen.values[::-1], color="#ff8400", edgecolor='black')

plt.title('Top 5 Batsmen (Most "Best Batsmen" Awards) - IPL 2025', fontsize=15, fontweight='bold')
plt.xlabel('Number of Awards', fontsize=12)
plt.ylabel('Batsman Name', fontsize=12)

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
