# Trabalho bimestral

Integrantes: Lívia Faria (020451), Lucas Faria (019790) e Wesley Júnior (020321)

# Sistema de gestão para autoescolas

## Introdução

Este documento apresenta a modelagem e administração de um banco de dados para uma **Plataforma de Gerenciamento de Autoescolas**, com foco na preparação teórica dos alunos para o exame do **DETRAN**. O objetivo principal é a **gestão de simulados, armazenamento de questões, gerenciamento de aulas teóricas e monitoramento do desempenho dos alunos**.

O banco de dados será implementado no **SQL Server**, o controle de acesso será por meio de **roles e privilégios** diferenciados para administradores, instrutores, alunos, avaliadores e analistas de dados.

## Análise de mercado

A preparação teórica para o exame de habilitação é um grande desafio para muitos candidatos, sendo um mercado atendido por algumas plataformas educacionais, como:

- [**Drivin-in**](https://painel.teorico.com.br/) – disponibiliza simulados online para exames teóricos.
- [**Autoclique**](https://autoclique.com.br/) – oferece cursos teóricos e simulados para obtenção da CNH.

Contudo, grande parte das autoescolas ainda **não dispõe de um sistema robusto** que centralize a experiência de aprendizado teórico, permitindo que alunos realizem simulados baseados em **bancos de questões atualizados**, acompanhem seu progresso e tenham acesso a **materiais teóricos complementares**.

## **Requisitos do Sistema**

O banco de dados deverá atender os seguintes requisitos funcionais e não funcionais:

### **Requisitos Funcionais**

- Gerenciamento de **usuários** (alunos, instrutores, administradores, avaliadores e analistas de dados).
- Cadastro e gestão de **simulados** e suas respectivas **questões e respostas**.
- Registro e acompanhamento do **desempenho dos alunos nos simulados**.
- Disponibilização de **aulas teóricas ministradas por instrutores**.
- Controle de acesso baseado em **perfis de usuário**, garantindo segurança e integridade dos dados.

### **Requisitos Não Funcionais**

- **Integridade e consistência**: o banco de dados deve garantir a correta associação entre alunos, simulados, aulas e resultados.
- **Segurança**: controle de acesso via **roles no SQL Server**, impedindo acesso não autorizado a informações sensíveis.
- **Escalabilidade**: estrutura modular para permitir expansões futuras, como a inclusão de **novas categorias de exames**.
- **Eficiência**: utilização de consultas otimizadas, visões e procedimentos armazenados para melhorar a performance e a experiência do usuário.

## Modelagem do banco de dados

As entidades inicialmente identificadas são essas:

| Entidade | Atributos Principais |
| --- | --- |
| **Aluno** | `id`, `nome`, `email`, `senha`, `data_nascimento` |
| **Instrutor** | `id`, `nome`, `email`, `senha` |
| **Administrador** | `id`, `nome`, `email`, `senha` |
| **Avaliador** | `id`, `nome`, `email`, `senha` |
| **Analista de Dados** | `id`, `nome`, `email`, `senha` |
| **Simulado** | `id`, `aluno_id`, `data_realizacao`, `nota` |
| **Questão** | `id`, `enunciado`, `simulado_id` |
| **Resposta** | `id`, `questao_id`, `alternativa`, `correta` |
| **Aula** | `id`, `instrutor_id`, `titulo`, `conteudo` |
| **Histórico de Simulados** | `id`, `aluno_id`, `simulado_id`, `nota`, `data_realizacao` |

Os atributos e entidades podem ser alterados durante o projeto.

### Modelo entidade relacionamento

![image.png](attachment:6ca51444-5dd3-4015-9f8f-760169f6881d:image.png)

## Perfis de Usuário e Controle de Acesso

- **administrator**
    - Privilégios: `INSERT`, `UPDATE`, `DELETE`, `SELECT` em **todas** as tabelas e views do banco de dados (ex.: `dbo.students`, `dbo.exams`, `dbo.questions`, `dbo.lessons`, `dbo.exams_history`, etc.).
    - Justificativa: permite à equipe de administração gerenciar completamente o sistema—desde contas de usuários até simulados, questões, aulas e relatórios—sem qualquer restrição de acesso.
- **instructor**
    - Privilégios: `INSERT`, `UPDATE`, `DELETE` em `dbo.lessons`; `SELECT` em `dbo.exams` e `dbo.students`.
    - Justificativa: instrutores criam e editam aulas e acompanham o desempenho dos alunos, mas não alteram resultados de provas.
- **student**
    - Privilégios: `SELECT`, `INSERT` em `dbo.exams`; `SELECT` em `dbo.lessons`, `dbo.questions` e `dbo.student_results`.
    - Justificativa: alunos realizam simulados e consultam conteúdos de aula e questões.
- **reviewer**
    - Privilégios: `INSERT`, `UPDATE`, `DELETE`, `SELECT` em `dbo.questions`.
    - Justificativa: revisores gerenciam o banco de questões, sem acesso aos dados dos alunos.
- **data_analyst**
    - Privilégios: `SELECT` em `vw_student_performance`.
    - Justificativa: analistas de dados acessam apenas visões agregadas de desempenho, sem poder modificar qualquer tabela base.

### Testes de Implementação de Segurança

| Role | Ação Testada | Resultado Esperado | Resultado Obtido |
| --- | --- | --- | --- |
| administrator | `INSERT` em exams; `SELECT` em questions | Permitido | OK |
| administrator | `SELECT` em students | Negado | OK |
| instructor | `INSERT` em lessons; `SELECT` em exams | Permitido | OK |
| instructor | `DELETE` em exams | Negado | OK |
| student | `INSERT` em exams; `SELECT` em lessons | Permitido | OK |
| student | `UPDATE` em questions | Negado | OK |
| reviewer | `INSERT`, `UPDATE` em questions | Permitido | OK |
| reviewer | `SELECT` em students | Negado | OK |
| data_analyst | `SELECT` em vw_student_performance | Permitido | OK |
| data_analyst | `INSERT` em exams | Negado | OK |

## Consultas Avançadas

- **Listar todos os alunos**
- **Exames aprovados (nota ≥ 70)**
- **Total de aulas ministradas por instrutor**
- **Média de notas por aluno (histórico)**
- **Aulas mais assistidas**
- **Alunos sem nenhum simulado realizado**

## Visões

- **vw_average_scores_per_student**: média de notas por aluno.
- **vw_exams_count_per_student**: total de exames por aluno.
- **vw_overall_exam_performance**: estatísticas gerais (média, mínimo, máximo).
- **vw_most_watched_lessons**: ranking de aulas por visualização.
- **vw_questions_reviewed_per_reviewer**: contagem de questões atribuídas a cada revisor.
- **vw_student_performance**: visão consolidada de desempenho, incluindo última data de exame.

## Procedimentos Armazenados

- **_sp_register_student**: insere novo aluno, com tratamento de erros em `TRY/CATCH`.
- **_sp_register_exam**: registra exame com data atual automaticamente.
- **_sp_update_question**: atualiza enunciado de questão conforme parâmetro.
- **_sp_filter_students**: pesquisa dinâmica de alunos por nome, e-mail e data de nascimento, montando SQL dinâmico.
- **_sp_bulk_insert_students**: importa dados de alunos via arquivo CSV, útil para cargas em massa.

### Scripts

Abaixo está os scripts:

- [Criação de tabelas](./scripts/CREATE.sql)
- [Permissões](./scripts/PERMISSIONS.sql)
- [Consultas](./scripts/QUERIES.sql)
- [Procedures](./scripts/PROCEDURES.sql)
- [Popular o banco de dados](./scripts/SEED.sql)
- [Visões](./scripts/VIEWS.sql)