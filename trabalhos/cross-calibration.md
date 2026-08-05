# Regressão para Calibração Cruzada (*Cross-Calibration*)

O objetivo desta atividade é desenvolver um pacote em **Python** capaz de realizar a calibração cruzada (*cross-calibration*) entre imagens dos satélites **CBERS-4**, **CBERS-4A** e **AMAZÔNIA-1** utilizando como referência imagens dos satélites **Sentinel-2** e **Landsat**.

Ao final da atividade, espera-se que o grupo desenvolva uma ferramenta reproduzível que automatize todo o fluxo de seleção, preparação e comparação dos dados, permitindo estimar relações de calibração entre sensores por meio de modelos de regressão linear.

## Conjunto de dados

O pacote deverá ser capaz de obter imagens a partir de catálogos compatíveis com o padrão **STAC (SpatioTemporal Asset Catalog)**.

Os sensores considerados na atividade são:

- CBERS-4;
- CBERS-4A;
- AMAZÔNIA-1;
- Sentinel-2;
- Landsat.

As imagens selecionadas deverão corresponder, à mesma região geográfica e à mesma data (ou datas suficientemente próximas), de forma a minimizar diferenças decorrentes das condições de aquisição.

Para facilitar as comparações, restrinja o conjunto de dados para os dados de reflectancia de superfície.
- https://data.inpe.br/stac/browser/collections/CB4-MUX-L4-SR-1?.language=en
- https://data.inpe.br/stac/browser/collections/CB4-WFI-L4-SR-1?.language=en
- https://data.inpe.br/stac/browser/collections/CB4A-MUX-L4-SR-1?.language=en
- https://data.inpe.br/stac/browser/collections/CB4A-WFI-L4-SR-1?.language=en
- https://data.inpe.br/stac/browser/collections/AMZ1-WFI-L4-SR-1?.language=en
- https://data.inpe.br/stac/browser/collections/landsat-2?.language=en
- https://data.inpe.br/stac/browser/collections/S2_L2A-1?.language=en

Também restrinja as bandas presentes nos satélites brasileiros (R, G, B e NIR). Obs: Sentinel-2 apresenta mais de uma NIR, ambas devem ser consideradas.

## O desafio

O principal desafio consiste em automatizar todas as etapas necessárias para tornar comparáveis imagens provenientes de diferentes sensores, considerando suas diferenças de resolução espacial, projeção cartográfica, cobertura, nomenclatura das bandas e características radiométricas.

Além da implementação da regressão, o pacote deverá permitir que todo o fluxo seja reproduzido de maneira simples e documentada.

## Funcionalidades esperadas

O pacote deverá ser capaz de:

- Buscar imagens em um catálogo STAC utilizando critérios espaciais e temporais;
- Identificar pares de imagens correspondentes entre sensores distintos;
- Realizar o download dos dados necessários;
- Reprojetar todas as imagens para uma projeção cartográfica comum;
- reamostrar a resolução espacial, quando necessário;
- Identificar e recortar (*crop*) automaticamente a região de interseção entre as imagens;
- Selecionar pares de bandas equivalentes para comparação;
- Executar regressões lineares entre os valores observados pelos diferentes sensores;
- Gerar estatísticas e gráficos que permitam avaliar a qualidade da calibração;
- Exportar os resultados obtidos.

Outras funcionalidades poderão ser implementadas conforme o interesse do grupo.

## Sugestões para o desenvolvimento

A qualidade da implementação será parte importante da avaliação. Alguns aspectos que podem ser considerados incluem:

- Estruturação do código como um pacote Python reutilizável;
- Modularização das diferentes etapas do processamento;
- Utilização de bibliotecas consolidadas para acesso a catálogos STAC e processamento geoespacial;
- Tratamento de erros e validação das entradas;
- Documentação da API e exemplos de utilização;
- Implementação de testes automatizados para as principais funcionalidades;
- Garantia de reprodutibilidade do fluxo de processamento.

## Desenvolvimento

O grupo deverá:

1. Projetar a arquitetura do pacote Python;
2. Implementar a busca automática de imagens em catálogos STAC;
3. Implementar as etapas de preparação dos dados (download, reprojeção, reamostragem e recorte);
4. Implementar o processo de regressão linear entre sensores;
5. Avaliar os resultados obtidos utilizando métricas estatísticas e visualizações apropriadas;
6. Documentar a utilização do pacote e discutir suas limitações e possibilidades de evolução.
