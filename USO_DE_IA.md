# Declaração de uso de Inteligência Artificial generativa

> O uso de IA generativa é permitido e incentivado no projeto, mas todo uso deve ser declarado e detalhado no artigo e na apresentação.

## 1. Ferramentas usadas

| Ferramenta (nome e versão/modelo) | Como acessaram | Quem usou |
|---|---|---|
| OpenRouter (`openai/gpt-6-luna`) | API (chave da disciplina) | Grupo (execução do bot e geração de dados) |
| ChatGPT (GPT-6) | Navegador, versão gratuita | Caio Magno |
| Gemini Notebook | Navegador, versão PLUS estudantil | Pedro Mendonça |
| Gemini Hydrogen (raciocínio baixo) | Navegador, versão gratuita | João Vitor Limonges Bedaque |

## 2. Usos, um por linha

| # | Etapa | O que a IA fez | Prompt (ou resumo + link para o registro) | O que o grupo fez com o resultado |
|---|---|---|---|---|
| 1 | Documentação | Auxiliou na orientação sobre a organização dos documentos e sua separação por categorias. | Conversas com o ChatGPT sobre a organização da base de conhecimento do UniTI. | Os documentos foram organizados e conferidos manualmente por Caio Magno. |
| 2 | Coleta de dados | Auxiliou na elaboração das perguntas do formulário para coleta de mensagens de estudantes. | Conversas com o ChatGPT sobre a elaboração do formulário de coleta. | As perguntas foram revisadas e utilizadas por Caio Magno na criação e divulgação do formulário. |
| 3 | Escrita (Divulgação) | Auxiliou na elaboração de mensagens para divulgação do formulário. | Conversas com o ChatGPT para elaboração de textos de divulgação. | Os textos foram revisados e adaptados por Caio Magno. |
| 4 | Geração de Dados (Passo 6) | Gerou frases sintéticas (`origem=llm`) para expandir o treino (`treino.csv`), cobrindo variações de linguagem das intenções de TI e negativos difíceis para `fora_dominio`. | Prompts solicitando frases em múltiplos estilos (formal, informal, erros) para intenções de TI e assuntos universitários vizinhos (`dados/prompts_llm.md`). | O grupo revisou e filtrou manualmente todas as frases geradas, garantindo zero vazamento e mantendo o `teste.csv` 100% composto por dados reais (`origem=coletado`). |
| 5 | Programação e Machine Learning (Notebook) | Auxiliou na estruturação dos pipelines do scikit-learn, vetorização por TF-IDF de n-gramas de caracteres, configuração do GridSearchCV e geração de gráficos (matrizes de confusão e distribuição de probabilidades). | Conversas sobre sintaxe de código em Python, ajuste do GridSearchCV e plotagem de gráficos com matplotlib/seaborn. | O grupo adaptou os códigos, corrigiu o isolamento do pacote `chatbot`, executou localmente, validou os resultados via validação cruzada (CV 5-folds) e testou com `scripts/verificar_entrega.py`. |
| 6 | Operação do Chatbot (RAG) | Redige as respostas finais do UniTI ao estudante a partir dos trechos recuperados da base de conhecimento e da persona do `grupo.yaml`. | Prompts de sistema definidos em `chatbot/llm.py` e persona configurada em `grupo.yaml`. | O grupo ajustou a persona e validou o comportamento em testes reais no terminal (`conversar.py --depurar`), inclusive para perguntas sem resposta na base. |
| 7 | Roteiro de Apresentação e Ambiente | Auxiliou na estruturação e cronometragem do roteiro de fala para o bloco de demonstração, além de orientar na execução local do ambiente para Linux. | Solicitação de um roteiro objetivo e cronometrado com base no relatório de execução e nos requisitos do trabalho, visando respeitar o limite de tempo do grupo e evitar desvios (tangentes) durante a fala. | Os comandos e as perguntas da demonstração foram executados e validados localmente no terminal (`conversar.py --depurar`), e o roteiro foi adaptado antes da gravação. |
| 8 | Escrita e Estruturação do Artigo (SBC) | Auxiliou na estruturação das seções no padrão SBC, na organização das tabelas e no rascunho/revisão textual a partir dos dados reais do projeto. | Solicitação de organização das seções e redação preliminar com base nas saídas do `01_trabalho_grupo.ipynb`, `avaliacao.json`, `FONTES.md` e `USO_DE_IA.md`. | O texto foi revisado, adaptado e conferido contra as métricas reais, matrizes de confusão e formatação SBC no Google Docs por João Vitor Limonges Bedaque. |
| 9 | Complemento de Treino | Gerou 125 frases sintéticas (53 chitchat e 72 fora_dominio) para atingir o mínimo exigido no treino.csv. | Solicitação de frases extras de chitchat e fora_dominio sem vírgulas para o treino. | Frases revisadas e adicionadas manualmente ao treino.csv junto com 20 frases humanas. |

## 3. O que NÃO foi feito com IA

As seguintes atividades foram realizadas **100% de forma manual pelos integrantes do grupo**, sem auxílio de IA generativa:

1. **Organização do Repositório, Git e Divulgação**: A estruturação física das pastas do projeto, o controle de versão, o envio de commits/pushes ao GitHub e a criação e divulgação do formulário online foram executados por Caio Magno. As respostas do formulário foram fornecidas diretamente pelos estudantes participantes.
2. **Elaboração e Validação do Conjunto de Teste (`teste.csv`)**: A seleção, triagem, filtragem e rotulagem de **100% das 141 frases** do arquivo de teste foram realizadas manualmente a partir das mensagens reais dos alunos coletadas em `respostas_classificadas.csv`. Nenhuma frase gerada por IA foi inserida no teste.
3. **Verificação de Vazamento e Divisão dos Dados**: A checagem de ausência de frases repetidas entre treino e teste (*vazamento zero*) e o ajuste da proporção das intenções foram executados diretamente pelo grupo.
4. **Curadoria das Fontes e Base de Conhecimento**: A busca, verificação de atualidade e catalogação dos 21 documentos oficiais em PDF da UFMS reunidos em `documentos/`, bem como o preenchimento do arquivo `FONTES.md`, foram conduzidos manualmente pela equipe.
5. **Execução dos Testes Interativos e Gravação do Vídeo**: A condução dos testes ao vivo no terminal (`conversar.py --depurar`), a verificação das saídas reais do bot e a gravação/edição do vídeo demonstrativo foram feitas integralmente pelos integrantes.

## 4. Reflexão (2 a 4 frases)

O uso de IA generativa acelerou o desenvolvimento do projeto UniTI no apoio à programação, na expansão sintética do conjunto de treino (394 frases sob múltiplos estilos), na redação das respostas via RAG, na cronometragem do roteiro de vídeo e na organização do artigo. Como principais limitações, observaram-se frases sintéticas mais longas e estruturadas que as mensagens reais de estudantes (média de 14,3 contra 7,8 palavras), além de sugestões de código desalinhadas com o contrato do repositório. Para mitigar esses problemas, o grupo revisou manualmente todas as frases geradas, manteve o conjunto de teste (141 frases) 100% humano com vazamento zero e validou todos os códigos, métricas e demonstrações localmente via validação cruzada, terminal (`--depurar`) e `verificar_entrega.py`.
