from fastapi import HTTPException, APIRouter, status
from app.schemas.chat import AskRequest, AskResponse
from app.services.chat_service import ChatService
router = APIRouter(
    prefix = "/chatbot",
    tags = ["user"]
)
@router.post("/chat",response_model = AskResponse)
async def chat_endpoint(request:AskRequest)-> AskResponse:
    try:
       service = ChatService()
       answer = await service.ask(request.question,request.provider)
       return AskResponse(
        answer = answer,
        provider = request.provider,
        model = request.model
    )
    except ValueError:
        raise HTTPException(status_code = 400,detail = str(e))



        