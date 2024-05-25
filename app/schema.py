from pydantic import BaseModel, PositiveInt
from typing import Optional

class ProdutosSchema(BaseModel):
    id: PositiveInt 
    nome: str 
    descricao: Optional[str] = None 
    preco: float