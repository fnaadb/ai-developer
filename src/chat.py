import asyncio
import logging
from dotenv import load_dotenv
from semantic_kernel import kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAITextToImage
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.openapi_plugin import OpenAPIFunctionExecutionParameters
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions import KernelArguments


#Add logger
logger = logging.getLogger(__name__)
load_dotenv(override=True)

# System message defining the behavior and persona of the chat bot.
system_message = """
You're a virtual assistant that helps people find information. 
Ask followup questions if something is unclear or more data is needed to complete a task
"""

chat_history = ChatHistory()

def initialize_kernel():
    kernel = kernel()

    # Add Azure AI Foundry Chat Completion
    # chat_completion_service = AzureChatCompletion(
    # deployment_name="my-deployment",  
    # api_key="my-api-key",
    # endpoint="my-api-endpoint", # Used to point to your service
    # service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel
    # )


    # You can do the following if you have set the necessary environment variables or created a .env file
    chat_completion_service = AzureChatCompletion(service_id="chat_completion")
    kernel.add_service(chat_completion_service)
    logger.info("Chat completion service added to the service")



async def process_message(user_input):
    logger.info(f"Processing user message: {user_input}")
    kernel = initialize_kernel()


