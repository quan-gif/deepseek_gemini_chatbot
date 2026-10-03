import logging
from typing import Dict,Optional
from app.gateways.base import BaseGateway
from app.gateways.deepseek_gateway import DeepseekGateway
from app.gateways.gemini_gateway import GeminiGateway
logger = logging.getLogger(__name__)
class ChatService:
    def __init__(self,gateways:Optional[Dict[str,BaseGateway]] = None):
        self.gateways = gateways if gateways else {}
    def get_gateway(self,provider_key:str):
         lower_provider = provider_key.strip().lower()
         if lower_provider in self.gateways:
            return self.gateways[lower_provider]
         if 'deepseek' == lower_provider:
           self.gateways[lower_provider] = DeepseekGateway()
         elif 'gemini' == lower_provider:
           self.gateways[lower_provider] = GeminiGateway()
         else:
            raise ValueError(f"Không hỗ trợ {provider_key},chỉ hỗ trợ deepseek hoặc gemini.")
         return self.gateways[lower_provider]
    async def ask(self,question:str,provider:str,model:str|None = None)->str:
         logger.info(f"Đang xử lý provider = {provider},câu hỏi:{question[:50]}")
         gateway = self.get_gateway(provider)
         answer = await gateway.generate(question,model)
         return answer

         







