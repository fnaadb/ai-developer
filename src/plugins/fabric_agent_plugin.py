import asyncio
from azure.identity.aio import DefaultAzureCredential
#from azure.core.credentials import TokenRequestContext

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings

import os
from typing import TypedDict, Annotated
from semantic_kernel.functions import kernel_function

from semantic_kernel.agents import AzureAIAgentThread




import logging
from opentelemetry import trace


from app_insights_tracing import get_logger, enable_telemetry
import logging
from opentelemetry import trace

from semantic_kernel import Kernel

logger = get_logger(__name__)
enable_telemetry(True)
tracer = trace.get_tracer(__name__)

class FabricPlugin:
    

    @tracer.start_as_current_span(name="FabricAgentPlugin")
    @kernel_function(description="Adventureworks has information on internet sales data with customer, product information and is stored in fabric")
    async def get_fabricsalesdata(self, query_str: Annotated[str, "Query about internet sales data along with product and customer information"]) -> Annotated[str, "Response for the query"]:  
        
        
        try:
            credential = DefaultAzureCredential()
            print('{}.get_token succeeded'.format(await credential.get_token()))
            #print(f"Token: {token.token}")
        except Exception as ex:
            print(f"Authentication failed: {ex}")
        

        async with (
            DefaultAzureCredential() as creds,
            #AzureAIAgent.create_client(credential=creds,sconn_str=os.getenv("AIPROJECT_CONNECTION_STRING_KEY")) as client,
            AzureAIAgent.create_client(credential=creds,conn_str="eastus2.api.azureml.ms;713a6867-f4a6-47da-8425-c1ea4c0ff132;ariefml;foundryworkshop") as client,
        ):
        # 1. Retrieve the agent definition based on the `agent_id`
        # Replace the "your-agent-id" with the actual agent ID
        # you want to use.
            agent_definition = await client.agents.get_agent(
            #agent_id=os.getenv("FABRIC_AGENT_ID"),
            agent_id="asst_8lI50aBivLP88gawvD9qJHxl",
            )

        # 2. Create a Semantic Kernel agent for the Azure AI agent
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
        )
        print(f"agent {agent.id}")

        # 3. Create a thread for the agent
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        #thread: AzureAIAgentThread = await AzureAIAgentThread(client=client)
        

        try:
            print(f"# arief: '{query_str}, client{client}'")
            thread: AzureAIAgentThread = AzureAIAgentThread(client=client)
            response = await agent.get_response(messages=query_str, thread=thread)
            # async for content in agent.invoke(messages=query_str, thread=thread):
            #     print(content.content)
            
            #response =agent.invoke(messages=query_str)
            #print(f"# {response.name}: {response}")
        except Exception as e:
            print(f"# arief exception: '{e}'")
        finally:
            # 5. Cleanup: Delete the thread and agent
            await thread.delete() if thread else None
            # Do not clean up the agent so it can be used again
        
        print("just before return")
        return response

