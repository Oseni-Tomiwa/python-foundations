
study_session = {
  "name": "Mavery",
  "topic": "Dictionaries",
  "hours": 2,
  "completed": True,
}


study_session["hours"] = 3
study_session["next_topic"] = "Functions"

print(f"Student: {study_session["name"]}")
print(f"Completed topic: {study_session["topic"]}")
print(f"Next topic: {study_session["next_topic"]} ")