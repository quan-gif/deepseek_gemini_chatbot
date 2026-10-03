import logging
from google import genai
from app.core.config import settings
from app.gateways.base import BaseGateway
logger = logging.getLogger(__name__)
class GeminiGateway(BaseGateway):
    def __init__(self):
        self.api_key = settings.gemini_api_key
        if not self.api_key or not self.api_key.strip():
            raise ValueError("Api key không được rỗng")
        self.model_name = settings.gemini_model
        self.client = genai.Client(api_key = self.api_key)
        logger.info(f"Đã khởi tạo thành công {self.model_name}")
    async def generate(self,prompt:str,model:str|None = None)-> str:
        try:
            model = model if model is not None else self.model_name
            response = await self.client.aio.models.generate_content(
                model = model,
                contents = prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"API của model gemini lỗi khi xử lý prompt: {e}")
            return("Hệ thống đang bị lỗi vui lòng thử lại sau")



