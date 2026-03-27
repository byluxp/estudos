# ✨ Conceitos básicos de banco de dados ✨

Aulas:  
[x] AULA 1  
[x] AULA 2  
[ ] AULA 3  
[ ] AULA 4

## 📚📚 Como eu entendi:

📊 Os dados são conjuntos de fatos que com um contexto viram **informações**. Uma data de nascimento é apenas um dado se não é dado o contexto adequado.  
Uma data sem contexto poderia ser:
  - Uma data de início de contrato.
  - Uma data de acontecimento de um fato.
  - Uma data futura, como projeção de algo.
*Por isso o contexto é tão importante.*

💭 O conceito de minimundo, nos permite observar, de forma abstrata, diferentes contextos de forma a tratar nossos dados. 
  - Uma data de início de contrato, pode ser usada para parabenizar o cliente daqui 1 ano, como forma de fidelização.
  - A mesma data, pode ser usada como base para o vencimento do contrato.
  - E também, como histórico de quantas vezes aquela atividade se iniciou.

🗺️ Quando vemos o minimundo e seus contextos, enxergamos como organizar nossas partes chaves e com isso iniciamos o *MODELO CONCEITUAL*.  
O modelo conceitual trabalhado vale-se do Diagrama Entidade-Relacionamento. Que, por sua vez, possui regras específicas para funcionamento.  
[ MODELO ENTIDADE RELACIONAMENTO - DER]:   
<br><br>
<img width="600" height="252" alt="image" src="https://github.com/user-attachments/assets/0405fa37-ee03-4088-8772-03b5ec79f94c" />
<br><br>
**NORMALIZAÇÃO**  

A estratégia de normalização segue o padrão FN: 1FN, 2FN, 3FN... Conforme modelo abaixo:  
<img width="350" height="322" alt="image" src="https://github.com/user-attachments/assets/fb838309-ed97-42cc-af40-539b5ece5793" />  
Seguindo as regras:  
**1FN = ATRIBUTOS SIMPLES E MONOVALORADOS:** Busca evitar redundância e anomalias (inclusão, exclusão e alteração).  
  Exemplo: Evitar que um certo dado seja alterado em lugar x e não seja alterado em lugar y. Ou que x sendo dependente influente y que é o padrão.   
  **2FN = TODOS OS ATRIBUTOS DEVEM DEPENDER DAS CHAVES PRIMÁRIAS:**  
    OBS: Se há apenas uma chave primária, já está na 2FN. Caso haja atributos que não se relacionam com a chave primária, criar outra tabela 1FN.  
    **3FN = NÃO POSSUIR DEPENDÊNCIA TRANSITIVA:** 
      Exemplo: relacionar com um atributo que depende da PK mas NÂO DEPENDER DELA DIRETAMENTE. Caso seja transitiva, criar uma tabela 1FN. 
      

**As informações aqui descritas podem ser alteradas a qualquer momento conforme novos exemplos - entendimentos vão surgindo.   
O aprendizado é flutuante, não o enxergue como um caminho finalizado. O conhecimento aqui descrito está em constante expansão.**
