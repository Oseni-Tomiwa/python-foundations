

study_sessions = [
    {
        "topic": "python",
        "hours": 3
    },
    {
        "topic": "Docker",
        "hours": 2
    }
]

# print(study_session[0]["topic"])
# print(study_session[1]["hours"])

# looping through every dictionary

for session in study_sessions:
    print(f"Topic: {session["topic"]}")
    print(f"Hours: {session["hours"]}")