import asyncio
import logging
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAITextToImage
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.openapi_plugin import OpenAPIFunctionExecutionParameters
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions import KernelArguments
from openai import AzureOpenAI
#arief
#from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase, PromptExecutionSettings

from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

from plugins.time_plugin import TimePlugin
from plugins.geo_plugin import GeoPlugin
from plugins.weather_plugin import WeatherPlugin
from plugins.ai_search_plugin import AiSearchPlugin
from plugins.image_plugin import ImagePlugin



#Add logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv(override=True)

# System message defining the behavior and persona of the chat bot.
system_message = """
You're a virtual assistant that helps people find information. 
Ask followup questions if something is unclear or more data is needed to complete a task
"""

chat_history = ChatHistory()
chat_history.add_system_message(system_message)
# Initialize the kernel and add the Azure AI Foundry Chat Completion service
#chat_completion_service : AzureChatCompletion = None
#client : ChatCompletionClientBase = None

def initialize_kernel():
    kernel = Kernel()

    # Add Azure AI Foundry Chat Completion
    # chat_completion_service = AzureChatCompletion(
    # deployment_name="my-deployment",  
    # api_key="my-api-key",
    # endpoint="my-api-endpoint", # Used to point to your service
    # service_id="my-service-id", # Optional; for targeting specific services within Semantic Kernel
    # )


    # You can do the following if you have set the necessary environment variables or created a .env file
    chat_completion_service = AzureChatCompletion(service_id="chat-completion")
    kernel.add_service(chat_completion_service)
    logger.info("Chat completion service added to the service")

    #client = ChatCompletionClientBase(ai_model_id="gpt-4o")


    return kernel



async def process_message(user_input):
    logger.info(f"Processing user message: {user_input}")
    kernel = initialize_kernel()
    #challenge 2
    execution_settings = kernel.get_prompt_execution_settings_from_service_id("chat-completion")
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
    arguments = KernelArguments(settings=execution_settings)

       # Challenge 03 - Add Time Plugin
    # Placeholder for Time plugin
    # Challenge 03 - Add Time Plugin/GeoPlugin
    kernel.add_plugin(GeoPlugin(), plugin_name="GeoCoding",)
    kernel.add_plugin(TimePlugin(), plugin_name="Time",)
    kernel.add_plugin(WeatherPlugin(),plugin_name="Weather",)
   
     


    chat_completion_service = kernel.get_service(service_id="chat-completion")
    
    chat_history.add_user_message(user_input)
    response = await chat_completion_service.get_chat_message_content(chat_history=chat_history,settings=execution_settings,kernel=kernel)
       

    # chat_function = kernel.add_function(
    #     prompt="{{$chat_history}}{{$user_input}}",
    #     plugin_name="ChatBot",
    
    #     function_name="Chat"
    # )
    
    


    #Challenge 03 and 04 - Services Required
    #Challenge 03 - Create Prompt Execution Settings
    #execution_settings = kernel.get_prompt_execution_settings_from_service_id("chat_completion")
    ### 
        #Auto: Allows the AI model to choose from zero or more function(s) from the provided function(s) for invocation.
        #Required: Forces the AI model to choose one or more function(s) from the provided function(s) for invocation.
        #NoneInvoke: Instructs the AI model not to choose any function(s).
    ###
  




 

    # Challenge 04 - Import OpenAPI Spec
    # Placeholder for OpenAPI plugin


    # Challenge 05 - Add Search Plugin


    # Challenge 06- Semantic kernel filters

    # Challenge 07 - Text To Image Plugin
    # Placeholder for Text To Image plugin

    # Start Challenge 02 - Sending a message to the chat completion service by invoking kernel
    """
     chat history:users, assistants, system messages and tools   
    """
    # arguments = {}
    # chat_history.add_user_message(user_input)
    # arguments["user_input"] = user_input
    # arguments["chat_history"] = chat_history
    # result = await kernel.invoke(chat_function, arguments=arguments)
    # chat_history.add_user_message(user_input)
    # chat_history.add_assistant_message(str(result))


    return response

def reset_chat_history():
    global chat_history
    chat_history = ChatHistory()


