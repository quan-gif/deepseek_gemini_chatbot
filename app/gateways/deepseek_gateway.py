import logging 
import os
from openai import AsyncOpenAI
from app.gateways.base import BaseGateway
from app.core.config import settings

logger = logging.getLogger(__name__)
class DeepseekGateway(BaseGateway):
        def __init__(self):
           self.api_key = settings.deepseek_api_key
           if not self.api_key or not self.api_key.strip():
             raise ValueError("API key không được phép rỗng")
           self.base_url = settings.deepseek_base_url
           self.model_name = settings.model_name
           self.client = AsyncOpenAI(api_key = self.api_key,base_url = self.base_url)
           self.max_output_tokens = settings.max_tokens
           logger.info(f"Đã khởi tạo thành công {self.model_name}")
        async def generate(self,prompt:str,model:str|None = None) -> str:
           model = model if model is not None else self.model_name
           user_message = [{"role":"user","content":prompt}]
           response = await self.client.chat.completions.create(
              model = model,
              messages = user_message,
              max_tokens = self.max_output_tokens,
              temperature = 0.7
        )
           content = response.choices[0].message.content
           return content







