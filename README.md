# 📅 FlowCal

**FlowCal** is a smart calendar assistant that helps you plan meaningful activities based on weather forecasts, calendar availability, and natural language input — all through a powerful command-line interface (CLI). It’s designed to enhance your personal scheduling by integrating intelligent logic, AI, and external data.

---

## 🚀 Features

- 🌤️ Weather-aware activity suggestions
- 📆 Integration with Google Calendar (and more to come)
- 🤖 Natural language planning using AI (LLM)
- ⏰ CLI interface for fast and efficient control
- 📱 Designed for CLI-first, mobile UI coming soon

---

## 🛠️ Project Structure

smart_calendar/
├── cli/                 # Command-line interface (Typer)
├── core/                # Logic: planner, calendar ops, weather analysis
├── integrations/        # External APIs: Weather, Calendar, OpenAI
├── tests/               # Unit tests
├── requirements.txt     # Python dependencies
└── README.md

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/HosseinShirazi91/FlowCal.git
   cd FlowCal

	2.	Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


	3.	Install dependencies:

pip install -r requirements.txt



⸻

⚙️ Usage

python cli/main.py --help

Example commands:

# Suggest activities for a given day and location
python cli/main.py suggest --day "Saturday" --location "Berlin"

# Add a manual event
python cli/main.py add-event --title "Gym" --datetime "2025-07-10T09:00"

# Show upcoming schedule
python cli/main.py show-schedule

# Plan with AI prompt
python cli/main.py plan-with-ai "Plan something fun if it's sunny this weekend"


⸻

🔐 Environment Variables

Create a .env file in the project root to store your secrets (e.g., API keys):

OPENWEATHER_API_KEY=your_api_key
GOOGLE_CALENDAR_CREDENTIALS=path/to/credentials.json
OPENAI_API_KEY=your_openai_key

Make sure .env is listed in .gitignore to avoid leaking secrets.

⸻

🧪 Testing

pytest


⸻

📍 Roadmap
	•	CLI commands for planning and viewing schedule
	•	Weather API integration
	•	Natural language to calendar integration (AI)
	•	Full Google Calendar sync
	•	Mobile app frontend (React Native / Flutter)
	•	Push notification & smart reminders

⸻

🤝 Contributing

Contributions, feedback, and feature requests are welcome!
Feel free to fork, open issues, or submit a pull request.

⸻

📄 License

This project is licensed under the MIT License. See LICENSE for details.

⸻

🧠 Author

Developed by Hossein Shirazi
