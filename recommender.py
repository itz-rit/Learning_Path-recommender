import pandas as pd

def get_recommendations(user_interest):
    data = pd.read_csv('skill_data.csv')
    user_interest = user_interest.lower()
    
    for i, row in data.iterrows():
        if user_interest in row['Career'].lower():
            return {
                'Career': row['Career'],
                'Skills': row['Recommended Skills'].split(';'),
                'Courses': row['Courses'].split(';')
            }
    return None
