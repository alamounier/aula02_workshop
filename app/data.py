from typing import List, Dict

class Produtos:

    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um telefone inteligente",
            "preco": 1500,
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um computador móvel",
            "preco": 3500,
        },
        {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um computador portátil",
            "preco": 2500,
        }
    ]

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto 
        return {"Status": 404, "Mensagem": "Produto não encontrado"}
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto