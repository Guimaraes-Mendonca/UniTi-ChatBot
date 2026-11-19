# Declaração de uso de Inteligência Artificial generativa

> O uso de IA generativa é permitido e incentivado no projeto, mas todo uso deve ser declarado e detalhado no artigo e na apresentação.

## 1. Ferramentas usadas

| Ferramenta (nome e versão/modelo) | Como acessaram | Quem usou |
|---|---|---|
| ChatGPT (GPT-6) | Navegador, versão gratuita | Caio Magno |

**Pendente:** os demais integrantes devem acrescentar as ferramentas de IA que utilizaram.

## 2. Usos, um por linha

| # | Etapa | O que a IA fez | Prompt (ou resumo + link para o registro) | O que o grupo fez com o resultado |
|---|---|---|---|---|
| 1 | Documentação | Auxiliou na orientação sobre a organização dos documentos e sua separação por categorias | Conversas com o ChatGPT sobre a organização da base de conhecimento do UniTI | Os documentos foram organizados e conferidos manualmente por Caio Magno |
| 2 | Coleta de dados | Auxiliou na elaboração das perguntas do formulário para coleta de mensagens de estudantes | Conversas com o ChatGPT sobre a elaboração do formulário de coleta | As perguntas foram revisadas e utilizadas por Caio Magno na criação e divulgação do formulário |
| 3 | Escrita | Auxiliou na elaboração de mensagens para divulgação do formulário | Conversas com o ChatGPT para elaboração de textos de divulgação | Os textos foram revisados e adaptados por Caio Magno |
| 4 | Geração de Dados (Passo 6) | Gerou frases sintéticas (`origem=llm`) para expandir o treino (`treino.csv`), cobrindo variações de linguagem das intenções de TI e negativos difíceis para `fora_dominio`. | Prompts solicitando frases em múltiplos estilos (formal, informal, erros) para intenções de TI e assuntos universitários vizinhos. | O grupo revisou e filtrou manualmente todas as frases geradas, garantindo zero vazamento e mantendo o `teste.csv` 100% composto por dados reais (`origem=coletado`). |

**Pendente:** os demais integrantes devem acrescentar suas próprias utilizações de IA, incluindo geração de dados, desenvolvimento do chatbot, programação e escrita, caso tenham utilizado.

## 3. O que NÃO foi feito com IA

A organização dos arquivos e pastas, o envio das alterações ao GitHub e a divulgação do formulário foram executados por Caio Magno. As respostas do formulário foram fornecidas pelos próprios participantes.

Elaboração e Validação do Conjunto de Teste (`teste.csv`): A seleção, triagem e rotulagem de 100% das frases do arquivo de teste foram feitas de forma manual a partir das mensagens reais coletadas dos alunos (`respostas_classificadas.csv`).
Verificação de Vazamento e Divisão dos Dados: A verificação da ausência de frases repetidas entre treino e teste e o ajuste da proporção das intenções foram feitos diretamente pelo grupo.

**Pendente:** o grupo deve complementar esta seção, informando quais outras atividades foram realizadas sem auxílio de IA.

## 4. Reflexão (2 a 4 frases)

**Pendente:** o grupo deverá elaborar uma reflexão conjunta sobre onde a IA ajudou, onde apresentou limitações ou erros e como os resultados gerados foram conferidos e validados pelos integrantes.
