from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, set_default_openai_client, set_tracing_disabled
from mysecrets import Secrets
from dotenv import load_dotenv

load_dotenv()
secrets = Secrets()

external_client = AsyncOpenAI(
    base_url= secrets.base_url,
    api_key= secrets.gemini_api_key
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model = secrets.gemini_api_model,
    openai_client= external_client
)

agent = Agent(
    name = "Jarvis",
    instructions="You are a concise assistant that greets the user in a single short sentence.",
    model = model
)

result = Runner.run_sync(agent, "Say hello in one short sentence.")
print(result.final_output)