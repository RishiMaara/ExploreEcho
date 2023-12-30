class ExploringEcho:
    def __init__(self):
        self.name = "Exploring Echo"
        self.features = [
            "Real-time speech translation",
            "Weather Forecast"
            "Explore Tourist Places",
            "Explore Resorts and Hotels based on Your location",
        ]

    def introduce(self):
        intro_msg = (
            f"Hello, I am {self.name}, your AI Travelling companion!\n"
            f"I specialize in the following features:\n"
        )
        features_msg = "\n".join([f"- {feature}" for feature in self.features])
        outro_msg = "\nHow can I assist you today?"
        full_intro = intro_msg + features_msg + outro_msg
        return full_intro

    def respond_to_user_input(self, user_input):
        if "translate" in user_input.lower():
            return "Sure, I can help with real-time speech translation. Please provide the text you'd like to translate."
        elif "explore places" in user_input.lower():
            return "Great! To explore places, please specify the location or ask for recommendations in a particular city."
        elif "explore resorts and hotels" in user_input.lower():
            return "Excellent choice! I can find resorts and hotels based on your location. Could you please share your current location or the destination you have in mind?"
        elif "weather" in user_input.lower():
            return "Yeah! Today's Weather is "
        else:
            return "I'm sorry, I didn't understand that. If you have a specific request, feel free to ask, and I'll do my best to assist you."

# Example usage:
if __name__ == "__main__":
    exploring_echo = ExploringEcho()
    print(exploring_echo.introduce())

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = exploring_echo.respond_to_user_input(user_input)
        print(f"{exploring_echo.name}: {response}")

