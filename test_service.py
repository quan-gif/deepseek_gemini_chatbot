import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')
import asyncio
from app.services.chat_service import ChatService
async def test():
    service = ChatService()
    answer = await service.ask('Xin chào','Gemini')
    print(answer)
if __name__ == "__main__":
    asyncio.run(test())







