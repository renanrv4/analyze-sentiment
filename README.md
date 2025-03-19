# Azure Language Studio

Projeto que recebe uma série de sentenças (MAX: 10) e faz a análise de sentimento usando o Azure Language Studio.

## Processo

1. **Configuração do Ambiente:**
    - Escolhi utilizar o python como linguagem para configurar o ambiente
    - A chave da API e o endpoint da Azure foram armazenadas em um `dotenv` que permite criar variáveis de ambiente.

2. **Leitura de Reviews:**
    - O projeto realiza a leitura de arquivos de texto contendo os reviews sobre algum tópico e/ou coisa.
    - Cada review é tratado de maneira individual para análise.

3. **Análise de Sentimentos:**
    - Cada review é enviado para o serviço da Azure que retorna o sentimento (positivo, negativo ou neutro) junto com uma pontuação de confiança.
    - As pontuações variam de 0 a 1 para as categorias positiva, negativa e neutra, e são usadas para determinar o sentimento geral da revisão.

4. **Exibição dos Resultados:**
    - Os resultados são exibidos com o sentimento e as pontuações associadas a cada review.

## Insights

- **Precisão da Análise:** 
    A análise de sentimentos da Azure é altamente eficaz para identificar padrões em grandes volumes de texto. Sentimentos negativos, neutros ou positivos podem ser facilmente categorizados, mas o contexto da frase é muito importante para uma avaliação mais precisa.
    
- **Aplicações Práticas:**
    A análise de sentimentos pode ser utilizada em diversas áreas:
    - **Análise de Mercado**
    - **Aprimoramento de Produtos**
    - **Monitoramento de Mídias Sociais:**
  
- **Limitação da API:**
    A Azure limita a quantidade de documentos enviados por vez. No caso da análise de sentimentos, um lote pode conter no máximo 10 documentos, o que pode exigir algum processamento extra caso você tenha mais reviews.

- **Diversidade de Sentimentos:**
    É importante ressaltar que a IA pode não ser 100% precisa em casos complexos. Como em sentenças sarcásticas, não é de se esperar que a IA consiga identificar corretamente o sentimento expressado nessas situações.

## Print de algumas análises;

```
Review 1:
Texto analisado: Este celular tem uma performance incrível, mas a bateria não dura muito.
Sentimento: negative
Pontuação positiva: 0.25
Pontuação negativa: 0.61
Pontuação neutra: 0.14
-------------------------
Review 2:
Texto analisado: O preço é muito alto para o que oferece. Não vale a pena.
Sentimento: negative
Pontuação positiva: 0.02
Pontuação negativa: 0.95
Pontuação neutra: 0.03
-------------------------
Review 3:
Texto analisado: O produto é bom, mas a entrega demorou demais.
Sentimento: negative
Pontuação positiva: 0.08
Pontuação negativa: 0.91
Pontuação neutra: 0.01
-------------------------
Review 4:
Texto analisado: Adorei o design e a qualidade do material, mas a tela podia ser melhor.
Sentimento: positive
Pontuação positiva: 0.99
Pontuação negativa: 0.01
Pontuação neutra: 0.0
-------------------------
Review 5:
Texto analisado: Simplesmente perfeito! Melhor aquisição que já fiz. Tudo veio bem embalado e a qualidade é top.
Sentimento: positive
Pontuação positiva: 1.0
Pontuação negativa: 0.0
Pontuação neutra: 0.0
-------------------------
Review 6:
Texto analisado: O serviço de atendimento foi excelente, me ajudaram com todas as dúvidas.
Sentimento: positive
Pontuação positiva: 1.0
Pontuação negativa: 0.0
Pontuação neutra: 0.0
-------------------------
Review 7:
Texto analisado: Produto razoável, mas tive problemas na instalação. O manual poderia ser mais claro.
Sentimento: negative
Pontuação positiva: 0.02
Pontuação negativa: 0.98
Pontuação neutra: 0.0
-------------------------
Review 8:
Texto analisado: Adorei! Muito bonito e funciona como esperado.
Sentimento: positive
Pontuação positiva: 1.0
Pontuação negativa: 0.0
Pontuação neutra: 0.0
-------------------------
Review 9:
Texto analisado: Horrível! Péssima experiência, demorou muito para chegar e veio errado. Nunca mais compro aqui.
Sentimento: negative
Pontuação positiva: 0.02
Pontuação negativa: 0.97
Pontuação neutra: 0.02
-------------------------
Review 10:
Texto analisado: Produto mediano, cumpre o que promete, mas sem grandes destaques.
Sentimento: positive
Pontuação positiva: 0.47
Pontuação negativa: 0.35
Pontuação neutra: 0.18
-------------------------
```
