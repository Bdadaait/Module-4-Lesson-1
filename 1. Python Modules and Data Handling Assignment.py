
# 1. Python Modules and Data Handling Assignment

# mood_responses.py

def mood_response(mood):
    if mood.lower() == "happy":
        return "I'm glad that you are happy! enjoy your day!"
    elif mood.lower() == "Sad":
        return "Sorry to hear that you are feeling sad, Hope things get better soon."
    elif mood.lower() == "Excited":
        return "That is Awsome!"
    else:
        return "Thanks for sharing your mood today!"

# main.py
    import mood_responses
    mood = input("How are you feeling today?")    
    print(mood_responses.mood_response(mood))