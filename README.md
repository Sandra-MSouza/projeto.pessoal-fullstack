# projeto.pessoal-fullstack
Este é um projeto pessoal em desenvolvimento que tem como objetivo construir um assistente inteligente para automatizar e otimizar o processo de busca de emprego. 
O sistema permite que o usuário cadastre currículos, preferências de vagas, acompanhe candidaturas e receba sugestões otimizadas com base em análise de dados e Inteligência Artificial.

## 🚀 Objetivo do Projeto

Criar uma aplicação capaz de:

- Gerenciar múltiplos currículos por usuário
- Salvar buscas de emprego personalizadas (por área, tipo, local, palavras-chave)
- Armazenar e analisar vagas coletadas de sites como LinkedIn, Gupy, etc.
- Registrar candidaturas e gerar cartas de apresentação automaticamente
- Utilizar LLMs para extrair perfis profissionais e adaptar currículos às vagas

## 📦 Estrutura do Projeto


## 🛠️ Tecnologias Utilizadas

- **Node.js** – Backend da aplicação
- **Python** – Scripts para IA e automações
- **Prisma ORM** – Mapeamento objeto-relacional com PostgreSQL
- **PostgreSQL** – Banco de dados relacional
- **LLMs / IA** – Para análise de currículos e geração de conteúdo
- **JavaScript / TypeScript** – Linguagem do backend (confirmar se está usando TS)
- **Linux** – Configuração adaptada para servidores ARM64 com OpenSSL 3.0

## 📚 Modelagem de Dados (via Prisma)

- `User`: dados do usuário
- `Resume`: currículo, análise, palavras-chave
- `JobSearch`: critérios da busca de vagas
- `JobVacancy`: detalhes de cada vaga encontrada
- `JobApplication`: candidaturas realizadas, status, carta e currículo adaptado

## 📌 Status do Projeto

🔧 **Em desenvolvimento** – funcionalidades principais em construção.  
Ainda estou implementando o backend, testes e conectando com serviços externos.

## 🙋‍♀️ Autora

Sandra M. Souza  
📧 san.mssouza@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sandramssouza)  
🔗 [GitHub](https://github.com/Sandra-MSouza)

---

