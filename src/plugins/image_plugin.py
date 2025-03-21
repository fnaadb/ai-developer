from typing import List, Optional, Annotated
import os
from semantic_kernel.functions import kernel_function
from semantic_kernel import Kernel
from urllib.request import urlopen

class ImagePlugin:
    
    def __init__(self, kernel: Kernel):
        if not kernel.get_service("text-to-image"):
            raise Exception("Missing text-to-image service")
        self.dalle3 = kernel.get_service("text-to-image")

    @kernel_function(description="Draws image/picture out of text.")
    async def generate_image_from_prompt(self, user_message: Annotated[str,"Descriptive prompt optimized for DALL-E"]):
        """
        Generate an image from a text prompt using DALL-E.

        Args:
            prompt (str): The text prompt for the image.
            kernel (Kernel): The Semantic Kernel instance.

        Returns:
            str: The URL of the generated image.
        """
        print("image")
        image = await self.dalle3.generate_image(
            description=str(user_message), width=1024, height=1024
        )
        return image
