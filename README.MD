# LVS Repair Express System

## Descrição

O **LVS Repair Express System** é um sistema de atendimento digital projetado para facilitar a interação do usuário com serviços de reparo automotivo. Ele oferece funcionalidades como agendamento de atendimentos, visualização de planos de seguro, e simulação de problemas automotivos com sugestões de possíveis causas.

## Funcionalidades

1.  **Solicitar Atendimento**: Permite que os usuários descrevam problemas com seus veículos e recebam possíveis causas para o problema. Oferece a opção de solicitar um guincho ou dirigir-se a uma oficina específica.
    
2.  **Atendimentos Agendados**: Os usuários podem visualizar, alterar a forma de pagamento ou cancelar seus agendamentos de atendimento.
    
3.  **Visualizar Planos de Seguro**: Exibe os planos de seguro disponíveis, detalhando os benefícios e permitindo que o usuário assine um plano diretamente.
    
4.  **Gerar Placa de Carro**: Função para gerar uma placa de carro aleatória, utilizada no contexto de envio de guincho.
    
5.  **Criação de Conta e Login**: Permite que novos usuários criem contas e usuários existentes façam login para acessar os serviços.
    

## Estrutura do Código

-   **Funções Principais**:
    
    -   `solicitarAtendimento(problema)`: Gerencia o processo de solicitação de atendimento, incluindo a geração de protocolos e cálculo de preços.
    -   `atendimentosAgendados()`: Exibe e gerencia agendamentos existentes.
    -   `visualizarPlanos()`: Apresenta os planos de seguro disponíveis e permite assinatura.
    -   `novaPlaca()`: Gera uma placa de carro aleatória.
    -   `criar_conta(database)`: Cria uma nova conta de usuário.
    -   `fazer_login(database)`: Realiza o login do usuário.
    -   `menu(database)`: Gerencia o menu principal de interação do usuário.
    -   `menu2()`: Exibe as opções do menu principal após o login.
-   **Estruturas de Dados**:
    
    -   `protocolosLista`: Lista de dicionários que armazena os protocolos de atendimento.
    -   `database`: Dicionário que simula um banco de dados de usuários.
    -   `marcas_carro`: Dicionário que categoriza carros por planos de seguro.
    -   `beneficios`: Dicionário que define os benefícios de cada plano de seguro.

## Requisitos

-   Python 3.x
-   Bibliotecas: `google.generativeai`, `random`, `string`, `colorama`, `time`, `sys`

## Como Executar

1.  Certifique-se de ter Python 3.x instalado.
2.  Instale as bibliotecas necessárias usando pip:
    
    ```bash
    pip install google-generativeai colorama
    
    ```
    
3.  Execute o script Python:
    
    ```bash
    python nome_do_arquivo.py
    
    ```
    

## Notas

-   O sistema utiliza a API do Google Generative AI para gerar conteúdo relacionado a problemas automotivos. Certifique-se de configurar a chave da API corretamente.
-   O sistema inclui um pseudo banco de dados para armazenar informações de usuários e protocolos de atendimento.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.