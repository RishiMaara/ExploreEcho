class ExploringEcho:
    def __init__(self):
        self.name = "Exploring Echo"
        self.features = [
            "Real-time speech translation",
            "Weather Forecast",
            "Explore Tourist Places",
            "Explore Resorts and Hotels based on Your location",
        ]
        self.tourist_places_data = {
            "Taj Mahal": {
                "Availability": "Open all days",
                "specialization": "Historical Monument",
                "Special_food": "Mughlai Cuisine",
            },
            "Jaipur": {
                "Availability": "Open all days",
                "specialization": "Historical City",
                "Special_food": "Dal Baati Churma",
            },
            "Goa": {
                "Availability": "Open all year",
                "specialization": "Beaches",
                "Special_food": "Fish Curry and Rice",
            },
            "Golden Palace": {
                "Availability": "4 a.m. to 11 p.m (IST)",
                "specialization": "Golden Temple is considered to be the most important pilgrimage site amongst Sikhs",
                "Special_food": " delicious Guru ka Langar at the common Gurudwara kitchen.",
            },
            "Qutub Minar, Delhi": {
                "Availability": "Open all year",
                "specialization": "Beaches",
                "Special_food": "Fish Curry and Rice",
            },
            "Kerala Backwaters": {
                "Availability": "Year-round",
                "specialization": "Backwaters",
                "Special_food": "Kerala Sadya",
            },
            "Rann of Kutch": {
                "Availability": "October to March",
                "specialization": "Salt Desert",
                "Special_food": "Gujarati Thali",
            },
            "Mysore Palace": {
                "Availability": "Open all days",
                "specialization": "Historical Palace",
                "Special_food": "Mysore Pak",
            },
            "Hampi": {
                "Availability": "Open all days",
                "specialization": "Ancient Ruins",
                "Special_food": "Bisi Bele Bath",
            },
            "Khajuraho Temples": {
                "Availability": "Open all days",
                "specialization": "Historical Temples",
                "Special_food": "Chaat",
            },
            "Meenakshi Amman Temple": {
                "Availability": "The temple is open from 5:00 a.m. to 12:30 p.m. and 4:00 p.m. to 10:00 p.m.",
                "specialization": "Set on the banks of the Vaigai River, Meenakshi Temple is dedicated to Goddess Parvati and Lord Shiva. It is widely recognised for its architecture and 14-coloured multi-tiered gopuram",
                "Special_food": "Traditional Veg meals, Puttu",
            },
        }

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
        elif "explore tourist places" in user_input.lower():
            return "Sure! Here are some top tourist places in India: Pick one Out for Further Details\n" + ", ".join(self.tourist_places_data.keys())
        elif "explore resorts and hotels" in user_input.lower():
            return "Excellent choice! I can find resorts and hotels based on your location. Could you please share your current location or the destination you have in mind?"
        elif "weather" in user_input.lower():
            return "Yeah! Today's Weather is "
        elif user_input in self.tourist_places_data:
            place_info = self.tourist_places_data[user_input]
            return (
                f"{user_input}:\n"
                f"Availability: {place_info['Availability']}\n"
                f"Specialization: {place_info['specialization']}\n"
               )
        else:
            return "I'm sorry, I didn't understand that. If you have a specific request, feel free to ask, and I'll do my best to assist you. or else Ask me the above comments"

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
