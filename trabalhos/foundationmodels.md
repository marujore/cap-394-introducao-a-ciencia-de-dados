# Comparação de Foundation model com algoritmos estado da arte (RF, XGBoost, LightGBM, Catboost, tabpfn)

O objetivo desta atividade é realizar um estudo comparativo entre Foundation Models e algoritmos clássicos de aprendizado de máquina utilizados em classificação de uso e cobertura da terra, avaliando desempenho, custo computacional, capacidade de generalização e robustez em diferentes conjuntos de dados.

Espera-se que o grupo desenvolva um fluxo reproduzível de treinamento, inferência e avaliação, comparando diferentes abordagens e investigando estratégias de ensemble para melhorar o desempenho final.

## Conjunto de dados

Os grupos deverão utilizar conjuntos de dados de observação da Terra disponibilizados pelo INPE, pode-se utilizar o pacote sits, que fornece acesso direto a cubos de dados e ferramentas para classificação de séries temporais. Se possível adote o uso do SITS em Python.

Sugere-se utilizar uma ou mais das seguintes coleções:

Sentinel-2 (L2A);
Sentinel-1 (RTC);
CBERS-4 (L4 SR);
CBERS-4A (L4 SR);
Amazônia-1 (L4 SR).

Os dados poderão ser obtidos diretamente por meio da infraestrutura do INPE e do pacote sits, permitindo a construção de conjuntos de treinamento e teste reproduzíveis.

Os grupos poderão trabalhar com uma ou mais regiões de interesse e diferentes classes de uso e cobertura da terra.

Modelos a serem avaliados

O estudo deverá comparar, no mínimo, os seguintes algoritmos:

Random Forest;
XGBoost;
LightGBM;
CatBoost;
TabPFN.

Além dos algoritmos clássicos, o grupo deverá selecionar e avaliar os Foundation Model disponíveis no SITS

Caso o Foundation Model não permita treinamento completo (fine-tuning), poderá ser utilizado como extrator de características (feature extractor), sendo as representações utilizadas para treinamento dos classificadores.

## O desafio

O principal desafio consiste em comparar metodologias bastante distintas de forma justa e reproduzível.

Os grupos deverão investigar aspectos como:

desempenho preditivo;
tempo de treinamento;
tempo de inferência;
consumo de memória;
capacidade de generalização para diferentes regiões;
sensibilidade ao tamanho do conjunto de treinamento;
facilidade de utilização.

Também deverá ser discutido em quais cenários os Foundation Models apresentam vantagens em relação aos algoritmos tradicionais.

## Ensembles

Além da comparação individual dos modelos, os grupos deverão investigar estratégias de combinação (ensemble) entre classificadores.

## Desenvolvimento

O grupo deverá:

1. Selecionar uma ou mais regiões de estudo;
2. Obter os dados utilizando o pacote sits e a infraestrutura do INPE;
3. Preparar os conjuntos de treinamento e validação;
4. Treinar os algoritmos clássicos de aprendizado de máquina;
5. Avaliar pelo menos um Foundation Model para sensoriamento remoto;
6. Implementar e comparar diferentes estratégias de ensemble;
7. Comparar os modelos utilizando métricas quantitativas e mapas produzidos;
8. Discutir os resultados obtidos, destacando vantagens, limitações e cenários de aplicação de cada abordagem.