# Scraping e Análise dos Trabalhos do SBSR

O objetivo desta atividade é construir uma base de dados consolidada contendo todos os artigos publicados no **Simpósio Brasileiro de Sensoriamento Remoto (SBSR)**, a partir da coleta automatizada das informações disponíveis nos anais do evento.

Além da obtenção dos dados, espera-se que o grupo realize o processo de preparação, padronização e análise da base, produzindo indicadores que permitam compreender a evolução da produção científica apresentada no SBSR ao longo dos anos.

## Conjunto de dados

Os grupos deverão construir uma base de dados contendo, sempre que possível, informações como:

- Título do artigo;
- Ano e edição do evento;
- Autores;
- Instituições dos autores;
- Palavras-chave;
- Resumo;
- Sessão temática;
- Demais metadados disponíveis nos anais, inclusive metadados sobre o evento.

A origem dos dados deverá ser documentada, assim como o processo utilizado para sua obtenção.

## O desafio

O principal desafio consiste em obter uma base de dados consistente a partir de informações provenientes de diferentes edições do evento, que podem apresentar variações no formato de publicação, na estrutura dos metadados e na forma de identificação dos autores e instituições.

Além da coleta dos dados (*web scraping* ou outro método automatizado), será necessário realizar um processo de limpeza e padronização da base, eliminando inconsistências e ambiguidades que possam comprometer as análises.

## Sugestões para a preparação dos dados

A qualidade da base de dados será parte importante da avaliação. Algumas etapas que podem ser realizadas incluem:

- Identificação e correção de erros de digitação (*typos*);
- Padronização dos nomes dos autores;
- Tratamento de diferentes formas de escrita para uma mesma instituição;
- Remoção de registros duplicados;
- Identificação e resolução de ambiguidades entre autores homônimos, quando possível;
- Tratamento de valores ausentes;
- Padronização de caracteres especiais e acentuação;
- Documentação das decisões adotadas durante a preparação da base.

Todo o processo deverá ser desenvolvido seguindo os princípios de reprodutibilidade, permitindo que outro pesquisador possa reconstruir a base de dados a partir dos procedimentos descritos.

## Análise exploratória

Após a construção da base de dados, cada grupo deverá realizar uma análise exploratória buscando responder, entre outras, questões como:

- Quais são os autores que mais publicaram no SBSR?
- Quais autores participaram do maior número de edições do evento?
- Como evoluiu o número de trabalhos publicados ao longo dos anos?
- Quais instituições possuem maior participação no evento?
- Como evoluiu a colaboração entre autores e instituições?
- Quais temas ou palavras-chave aparecem com maior frequência ao longo do tempo?
- Como a temática dos trabalhos variou ao longo dos anos?

Outras análises poderão ser realizadas conforme o interesse do grupo.

## Desenvolvimento

O grupo deverá:

1. Desenvolver o processo automatizado de obtenção dos dados;
2. Construir a base de dados consolidada;
3. Avaliar e melhorar a qualidade dos dados por meio de técnicas de limpeza e padronização;
4. Documentar todas as etapas da preparação da base, garantindo sua reprodutibilidade;
5. Realizar uma análise exploratória dos dados utilizando tabelas, estatísticas e visualizações;
6. Discutir os principais resultados obtidos e as limitações da base construída.
