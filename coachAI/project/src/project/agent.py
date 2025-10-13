from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, function_tool
from dotenv import load_dotenv
from mysecrets import Secrets
import chainlit as cl


load_dotenv()
secrets = Secrets()

# function tool 
@function_tool("aboutus")
@cl.step(name = "Fetching information about CoachAI...", type= "tool") #label
def aboutus() -> str:
    """Provides information about the CoachAI service."""
    return (
    """🧠 About CoachAI
    💪 Who We Are

    CoachAI is your personal AI-powered fitness trainer — designed to guide you toward a healthier, stronger, and more confident version of yourself.
    It combines expert gym knowledge, personalized diet planning, and fitness motivation — all in one intelligent assistant.

    🥗 What CoachAI Does

    CoachAI helps you with:

    Personalized diet plans based on your body goals

    Smart workout routines for home or gym

    Step-by-step fat loss and muscle gain guidance

    Cardio scheduling, rest days, and hydration tips

    Real-time motivation and progress advice

    Whether you want to lose fat, build muscle, or stay fit — CoachAI gives you the exact plan and encouragement you need.

    ⚙️ How It Works

    Just tell CoachAI a few details:

    Your age, gender, weight, height, and goal
    and it will instantly create a complete diet + workout plan tailored just for you.

    🚀 Our Mission

    To make fitness simple, accessible, and motivating for everyone — powered by AI that actually understands your journey.

    CoachAI isn’t just a chatbot — it’s your virtual fitness partner that keeps you on track, motivated, and informed.""")


# our main agent function
def main_agent():
    ecternal_client = AsyncOpenAI(
        api_key=secrets.gemini_api_key,
        base_url= secrets.base_url
    )
    set_default_openai_client(ecternal_client)
    set_tracing_disabled(True)

    model = OpenAIChatCompletionsModel(
        model = secrets.gemini_api_model,
        openai_client= ecternal_client
    )

    agent = Agent(
        name= "CoachAI",

        instructions= """You are a professional AI Gym Coach named "CoachAI" with 10+ years of experience.
        Your role:
        - Help users improve their health, fitness, and diet.
        - Recommend them diet plans, fitness tips based on their questions.
        - Provide custom diet plans based on user's body goals (e.g. weight loss, muscle gain, fat burning).
        - Give workout routines for beginners, intermediates, and advanced users.
        - Suggest gym exercises for specific body parts (chest, abs, legs, etc.).
        - Motivate users like a real coach, but in a friendly and encouraging way.

        Rules:
        1. Always use simple and motivational language.
        2. If a user gives their body stats (age, gender, weight, height, goal), create a **personalized diet + workout plan**.
        3. If information is missing, ask politely for the required details.
        4. Never recommend any unsafe or medical products.
        5. Focus on natural fitness, discipline, consistency, and healthy eating.
        6. Always explain the reason behind your recommendations (e.g., why certain foods or workouts help).
        7. Keep tone professional but friendly — like a real coach who cares.
        8. You can guide users on:
        - Meal timing
        - Gym schedule
        - Rest days
        - Cardio routines
        - Protein intake and hydration
        9. If user asks general health or motivation questions, respond supportively.

        Output style:
        - Use short paragraphs or bullet points.
        - Highlight important points with emojis (💪🔥🥗💧 etc.).
        - Be energetic and encouraging.

        Example:
        User: "I want to lose fat from belly and chest."
        You: 
        "🔥 Let’s do it! Here's your plan:
        - **Diet:** Eat more protein (eggs, chicken, lentils), avoid sugar & oily food.
        - **Workout:** Mix cardio + push exercises.
        - **Cardio:** 20 min treadmill after workout.
        Stay consistent — results will show in 3-4 weeks! 💪""",

        model=model,
        tools = [
            aboutus,
        ]
    ) 

    return agent