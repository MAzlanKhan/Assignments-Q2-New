from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_default_openai_client, set_tracing_disabled
from dotenv import load_dotenv
from mysecrets import Secrets


load_dotenv()

def run():
    secrets = Secrets()

    external_client = AsyncOpenAI(
        api_key= secrets.gemini_api_key,
        base_url= secrets.base_url
    )

    set_default_openai_client(external_client)
    set_tracing_disabled(True)

    model = OpenAIChatCompletionsModel(
        model = secrets.gemini_api_model,
        openai_client= external_client
    )

    agent = Agent(
        name = "Nalza",
        instructions= "You are a concise assistant that greets the user in a single short sentence.",
        model = model
    )

    result = Runner.run_sync(agent, "Say hello in one short sentence.")
    print(result.final_output)

if __name__ == "__main__":
    run()