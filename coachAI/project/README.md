🏋️‍♂️ CoachAI — Your Personal AI Fitness Trainer

CoachAI is an intelligent chatbot that acts as your virtual gym coach, helping users with custom diet plans, workout routines, and fitness guidance — all powered by AI.

🚀 Features

✅ Personalized Diet Plans — Tailored meal suggestions based on age, weight, and fitness goals
✅ Workout Routines — Smart gym and home workout guidance
✅ Real-Time Chat — Talk to your coach live using Chainlit’s chat UI
✅ Progress Motivation — Encouraging and friendly responses like a real trainer
✅ Safe & Natural Advice — No supplements or unsafe shortcuts

🧠 How It Works

User opens the chatbot (built using Chainlit).

CoachAI asks basic info — age, gender, weight, height, and fitness goal.

Based on inputs, it generates:

🥗 A personalized diet plan

💪 A workout routine

💧 Tips for recovery, cardio, and consistency

Users can continue chatting for motivation, tips, or updates on progress.

⚙️ Tech Stack

Python 3.11+

Chainlit (for chat UI)

OpenAI Agents SDK (for AI logic)

Async event streaming for real-time responses

🧩 Project Structure
coachAI/
├── chainlit.toml
├── chainlit.md
├── README.md
├── public/
│   └── logo.png
├── src/
│   └── project/
│       ├── main.py
│       ├── agent.py
│       ├── mysecrets.py
│       └── history.json


💡 Example Interaction

User: I want to lose fat from belly and chest.
CoachAI:
🔥 Let’s do it!

Diet: High protein (eggs, chicken, lentils), avoid sugar & fried foods.
Workout: Mix cardio (20 mins treadmill) + chest workouts (push-ups, incline press).
Tip: Stay consistent — you’ll see results in 3–4 weeks 💪

⚙️ Screenshot Sample
<img src="public/chat.png" alt="Chat Sample"/>

🧑‍💻 Developer Info

Project Name: CoachAI
Creator: [Your Name or Organization]
Built With: Python + Chainlit + OpenAI + Gemini API

🔥 Steps to set up and run my project
Clone my repo
Create Virtual Enviroment
Install dependencies
Run command: chainlit run main.py
