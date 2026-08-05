# Time Series Shift

O objetivo desta atividade é desenvolver um modelo de aprendizado de máquina capaz de estimar a **Concentração de Sedimentos Suspensos (CSS)** da estação fluviométrica de Aruanã (Rio Araguaia) a partir de informações de vazão e da data da observação.

Ao final da atividade, espera-se que o grupo seja capaz de gerar uma série temporal diária de CSS utilizando apenas variáveis derivadas da vazão e da data.

## Conjunto de dados

Foi disponibilizada uma planilha contendo as seguintes colunas:

- **Data** – data da observação;
- **Q_25200000** – vazão média diária (m³/s) da estação fluviométrica de Aruanã (Código ANA 25200000);
- **CSS** – concentração de sedimentos suspensos (mg/L);
- **Fonte** – origem do dado de CSS.

As observações de CSS foram obtidas de diferentes fontes:

- Agência Nacional de Águas e Saneamento Básico (ANA);
- Trabalhos acadêmicos (Aquino e Bayer);
- Estimativas obtidas por sensoriamento remoto.

Enquanto a série de vazão possui observações diárias, os dados de CSS estão disponíveis apenas para alguns dias ao longo do período de estudo.

## O desafio

O principal desafio consiste em construir um modelo capaz de aprender a relação entre vazão, sazonalidade e concentração de sedimentos, de forma a estimar os valores de CSS para todos os dias da série temporal.

Uma dificuldade importante é que a resposta da concentração de sedimentos nem sempre ocorre simultaneamente às variações da vazão. Em muitos casos, existe uma defasagem temporal (*lag*) entre essas variáveis, além de efeitos sazonais associados ao regime hidrológico anual.

Assim, uma etapa fundamental do trabalho será a construção de novas variáveis (*Feature Engineering*) que permitam representar essas relações.

## Sugestões para o *Feature Engineering*

A criatividade na construção das variáveis será parte importante da avaliação. Algumas possibilidades incluem:

- Extração de componentes da data:
  - Ano;
  - Mês;
  - Dia do ano;
  - Estação do ano;
  - Representações cíclicas da sazonalidade (por exemplo, seno e cosseno do dia do ano).

- Criação de variáveis derivadas da vazão:
  - Vazões defasadas (*lags*);
  - Vazões futuras (*leads*), quando justificadas para análise exploratória;
  - Médias móveis;
  - Diferenças entre dias consecutivos;
  - Taxa de variação da vazão;
  - Estatísticas calculadas em janelas temporais.

Não existe uma única solução correta. O objetivo é investigar quais atributos fornecem maior poder preditivo ao modelo.

## Desenvolvimento
O grupo deverá:
    1. realizar uma análise exploratória dos dados;
    2. tratar valores ausentes quando necessário;
    3. propor e justificar as variáveis criadas;
    4. treinar um ou mais modelos de regressão;
    5. avaliar o desempenho utilizando métricas apropriadas;
    6. discutir os resultados obtidos e as limitações da abordagem.
    7. fornecer uma planilha contendo os valores estimados de CSS para todos os dias da série.