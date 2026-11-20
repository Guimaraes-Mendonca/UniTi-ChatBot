# Declaração de uso de Inteligência Artificial generativa

> O uso de IA generativa é permitido e incentivado no projeto, mas todo uso deve ser declarado e detalhado no artigo e na apresentação.

## 1. Ferramentas usadas

| Ferramenta (nome e versão/modelo) | Como acessaram | Quem usou |
|---|---|---|
| ChatGPT (GPT-6) | Navegador, versão gratuita | Caio Magno |
| Gemini Notebook | Navegador, versão PLUS estudantil | Pedro Mendonça |


## 2. Usos, um por linha

| # | Etapa | O que a IA fez | Prompt (ou resumo + link para o registro) | O que o grupo fez com o resultado |
|---|---|---|---|---|
| 1 | Documentação | Auxiliou na orientação sobre a organização dos documentos e sua separação por categorias. | Conversas com o ChatGPT sobre a organização da base de conhecimento do UniTI. | Os documentos foram organizados e conferidos manualmente por Caio Magno. |
| 2 | Coleta de dados | Auxiliou na elaboração das perguntas do formulário para coleta de mensagens de estudantes. | Conversas com o ChatGPT sobre a elaboração do formulário de coleta. | As perguntas foram revisadas e utilizadas por Caio Magno na criação e divulgação do formulário. |
| 3 | Escrita | Auxiliou na elaboração de mensagens para divulgação do formulário. | Conversas com o ChatGPT para elaboração de textos de divulgação. | Os textos foram revisados e adaptados por Caio Magno. |
| 4 | Geração de Dados (Passo 6) | Gerou frases sintéticas (`origem=llm`) para expandir o treino (`treino.csv`), cobrindo variações de linguagem das intenções de TI e negativos difíceis para `fora_dominio`. | Prompts solicitando frases em múltiplos estilos (formal, informal, erros) para intenções de TI e assuntos universitários vizinhos. | O grupo revisou e filtrou manualmente todas as frases geradas, garantindo zero vazamento e mantendo o `teste.csv` 100% composto por dados reais (`origem=coletado`). |
| 5 | Programação e Machine Learning (Notebook) | Auxiliou na estruturação dos pipelines do scikit-learn, vetorização por TF-IDF de n-gramas de caracteres, configuração do GridSearchCV e geração de gráficos (matrizes de confusão e distribuição de probabilidades). | Conversas sobre sintaxe de código em Python, ajuste do GridSearchCV e plotagem de gráficos com matplotlib/seaborn. | O grupo adaptou os códigos, corrigiu o isolamento do pacote `chatbot`, executou localmente, validou os resultados via validação cruzada (CV 5-folds) e testou com `scripts/verificar_entrega.py`. |

## 3. O que NÃO foi feito com IA

Para garantir a transparência, a integridade científica e o cumprimento rigoroso das regras do trabalho, as seguintes atividades foram realizadas **100% de forma manual pelos integrantes do grupo**, sem qualquer auxílio de ferramentas de Inteligência Artificial generativa [1, 2]:

1. **Redação e Elaboração do Artigo Científico (SBC)**: A escrita de todas as seções do artigo no formato da SBC (`relatorio/relatorio.pdf`), a fundamentação teórica, a análise crítica das métricas dos classificadores, a interpretação das matrizes de confusão e a redação da conclusão foram feitas integralmente pelos alunos, garantindo autoria humana completa.
2. **Organização do Repositório, Git e Divulgação**: A estruturação física das pastas do projeto, o controle de versão, o envio de commits/ushes ao GitHub e a criação e divulgação do formulário online foram executados por Caio Magno. As respostas do formulário foram fornecidas diretamente pelos estudantes participantes.
3. **Elaboração e Validação do Conjunto de Teste (`teste.csv`)**: A seleção, triagem, filtragem e rotulagem de **100% das 141 frases** do arquivo de teste foram realizadas de forma manual a partir das mensagens reais dos alunos coletadas no arquivo `respostas_classificadas.csv`. Nenhuma frase gerada ou sintetizada por IA foi inserida no conjunto de teste.
4. **Verificação de Vazamento e Divisão dos Dados**: A checagem de ausência de frases repetidas entre os conjuntos de treino e teste (*vazamento zero*) e o ajuste fino da proporção das intenções foram executados diretamente pelos integrantes do grupo.
5. **Curadoria das Fontes e Base de Conhecimento**: A busca, verificação de atualidade e catalogação dos 17 documentos oficiais da UFMS (em PDF, Markdown e HTML) reunidos no diretório `documentos/`, bem como o preenchimento do arquivo `FONTES.md`, foram conduzidos manualmente pela equipe.
6. **Roteirização e Gravação do Vídeo Demonstrativo**: A elaboração do roteiro, a definição das falas, a condução dos testes interativos no terminal e a gravação do vídeo de demonstração (até 10 minutos) foram realizadas integralmente pelos membros do grupo.


## 4. Reflexão (2 a 4 frases)

O desenvolvimento do projeto UniTI utilizou ferramentas de IA generativa como apoio no desenvolvimento do código, na expansão sintética do conjunto de treinamento e na redação das respostas RAG do assistente. No ecossistema de dados, a IA foi empregada para gerar 394 frases sintéticas no treino.csv sob cinco variações estilísticas (formal, informal, erros ortográficos, ansioso e curto), viabilizando o balanceamento de 50 amostras por classe para as 8 intenções do domínio de TI. No pipeline do chatbot, a LLM atuou na síntese de respostas orientadas pela persona do sistema a partir dos trechos recuperados da base de conhecimento.
Como limitações, observou-se a geração de frases sintéticas com construções repetitivas ou vocabulário distante da realidade acadêmica da UFMS, além da tendência do modelo em sugerir códigos desalinhados com a estrutura de arquivos e contratos da aplicação. Para mitigar tais falhas, o grupo conduziu uma curadoria manual de 100% dos dados sintéticos, descartando amostras redundantes e ajustando rótulos. Adicionalmente, manteve-se o conjunto de teste (teste.csv, 141 amostras) de forma 100% independente e composto exclusivamente por dados reais de origem humana, assegurando vazamento zero e validade na avaliação final. Todo o código e os modelos finais foram validados por validação cruzada (CV 5 folds) e auditados com o verificador automático do projeto (verificar_entrega.py).
