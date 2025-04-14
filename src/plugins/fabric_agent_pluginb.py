import asyncio
from azure.identity.aio import DefaultAzureCredential
from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings

import os
from typing import TypedDict, Annotated
from semantic_kernel.functions import kernel_function




import logging
from opentelemetry import trace



# logger = get_logger(__name__)
# enable_telemetry(True)
# tracer = trace.get_tracer(__name__)

import logging

logging.basicConfig(level=logging.INFO)

    


async def get_fabricsalesdata(query_str: Annotated[str, "Query about internet sales data along with product and customer information"]) -> Annotated[str, "Response for the query"]:  


    
    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(credential=creds, conn_str="eastus2.api.azureml.ms;713a6867-f4a6-47da-8425-c1ea4c0ff132;ariefml;foundryworkshop") as client,
    ):
        # 1. Retrieve the agent definition based on the `agent_id`
        # Replace the "your-agent-id" with the actual agent ID
        # you want to use.
        agent_definition = await client.agents.get_agent(
        agent_id="asst_8lI50aBivLP88gawvD9qJHxl",
        )

        # 2. Create a Semantic Kernel agent for the Azure AI agent
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
        )

        # 3. Create a thread for the agent
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread = None
        

        try:
            print(f"# User: '{query_str}'")
           
            response = await agent.get_response(messages=query_str, thread=thread)
            print(f"# {response.name}: {response}")
        finally:
            print(f"{response.thread.id}")
            # 5. Cleanup: Delete the thread and agent
            await thread.delete() if thread else None
            # Do not clean up the agent so it can be used again
        
        
    return response

if __name__ == "__main__":
    asyncio.run(get_fabricsalesdata(query_str="What are top 10 customers?"))
