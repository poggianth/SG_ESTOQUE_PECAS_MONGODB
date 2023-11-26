# SG_ESTOQUE_PECAS_MONGODB

Este é um sistema de gerenciamento de estoque simples, que inclui três collections principais: `estoques`, `produtos` e `itens_estoque`. 
O sistema permite o rastreamento de produtos em diferentes tipos de estoque e suas localizações específicas em prateleiras e estantes.

## Requisitos

Para executar este projeto, você precisará de:

1. **Banco de Dados MongoDB**: Certifique-se de ter um banco de dados MongoDB configurado e acessível.

2. **Python**: Deve-se ter o Python instalado na máquina. 

3. **Configuração da Base de Dados**: 
    - Para apenas **criar o banco** e as suas collections, execute o arquivo: "src/scripts/create_DB.py".
    - Para **inserir registros** nas collections, execute o arquivo: "src/scripts/create_records.py".
    - Caso queira **criar o banco e inserir registros**, execute o arquivo: "src/scripts/create_all.py".

4. **Arquivo "principal.py"**: Para rodar o programa, execute o arquivo "principal.py".

## Uso

Você pode usar este sistema de gerenciamento de estoque para rastrear produtos em diferentes tipos de estoque, adicionar novos produtos, verificar a quantidade disponível e localizá-los nas prateleiras e estantes. Personalize o sistema de acordo com as necessidades do seu negócio.

## Contribuição

Sinta-se à vontade para contribuir para este projeto, reportar problemas ou propor melhorias. Basta criar um fork deste repositório, fazer as alterações desejadas e enviar um pull request.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE). Sinta-se à vontade para usá-lo conforme necessário.

