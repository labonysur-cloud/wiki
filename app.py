import time
from core.brain import Brain
from core.stt import listen
from core.tts import speak
from core.wakeword import detect_wakeword  # Detects "Hey Wiki"

# ======== Initialize Wiki Brain ========
dataset_paths = [
    "datasets/commands.csv",
    "datasets/cooking.csv",
    "datasets/study.csv"
]

brain = Brain(dataset_paths)

# ======== Main Loop ========
print("Wiki is ready. Say 'Hey Wiki' to start talking...")

while True:
    try:
        # 1. Listen for wake word
        print("Listening for wake word...")
        if detect_wakeword():  # Returns True when "Hey Wiki" is detected
            speak("I am listening.")
            
            # 2. Capture user speech
            user_input = listen()  # Converts audio to text
            print("You:", user_input)
            
            if user_input.lower() in ["exit", "quit", "stop"]:
                speak("Goodbye.")
                break
            
            # 3. Process input through Brain
            response = brain.respond(user_input)
            print("Wiki:", response)
            
            # 4. Speak response
            speak(response)
        
        # Small delay to reduce CPU usage
        time.sleep(0.5)
    
    except KeyboardInterrupt:
        print("\nExiting Wiki...")
        speak("Goodbye.")
        break
    
    except Exception as e:
        print("Error:", e)
        speak("An error occurred.")
        time.sleep(1)


                        