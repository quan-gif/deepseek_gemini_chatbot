from abc import ABC,abstractmethod
class BaseGateway(ABC):
    @abstractmethod
    async def generate(self,prompt:str,model:str|None = None) -> str:
        pass
        
# bản thiết kế chung cho mọi gateway
# quy định mọi gateway phải có method generate
