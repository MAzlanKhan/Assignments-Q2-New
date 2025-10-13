from agent import main_agent
import chainlit as cl
from typing import cast
from agents import Agent, Runner
import json
from openai.types.responses import ResponseTextDeltaEvent


@cl.set_starters
async def custom_starter():
    return [
        cl.Starter(
            label = "About CoachAI",
            message = "Tell me about CoachAI",
            icon = "public/coachai.jpg"
        ),
        cl.Starter(
            label = "Fitness Plan",
            message = "I want a personalized fitness plan",
            icon = "public/fitnessplan.jpg"
        ),
    ]
  

@cl.on_chat_start
async def start():
    agent = main_agent()
    cl.user_session.set("agent", agent)
    cl.user_session.set("history", [])

@cl.on_message
async def on_msg(message: cl.Message):
    msg = cl.Message(content="Thinking...")
    await msg.send()

    try:
        agent = cast(Agent, cl.user_session.get("agent"))
        history = cl.user_session.get("history", [])
        history.append({"role": "user", "content": message.content})

        result = Runner.run_streamed(agent, history)

        async for event in result.stream_events():

            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):

                if msg.content == "Thinking...":
                    msg.content = ""

                await msg.stream_token(event.data.delta)

        # When streaming completes, ensure final_output (if provided) is shown and save history
        if result.final_output is not None:
            msg.content = result.final_output
            await msg.update()

        cl.user_session.set("message_history", result.to_input_list())
    
    except Exception as e:
        msg.content = f"There is an error while processing your request. Please review the following before trying again. \n\n Error: {e}"
        await msg.update()
        
@cl.on_chat_end
async def end():
    history = cl.user_session.get("history", [])
    with open("history.json", "w") as f:
        json.dump(history, f, indent=2)
