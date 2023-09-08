# Clean Code - Código Limpo
### Anotações sobre o livro!

## Princípios do 5S para Desenvolvimento de Código

O método 5S é uma abordagem popular para melhorar a organização e eficiência no ambiente de trabalho. Esses princípios podem ser aplicados ao desenvolvimento de código para promover boas práticas e produzir um código mais limpo, legível e fácil de manter. Aqui estão os princípios do 5S adaptados para o contexto de desenvolvimento de software:

## 1. Organização

No desenvolvimento de código, a organização é crucial para manter um ambiente de trabalho produtivo e um código bem estruturado. Ao nomear variáveis, funções e outros elementos do código, evite nomes genéricos e opte por nomes descritivos que indiquem claramente a função e o propósito desses elementos. Por exemplo, em vez de usar `s = a + b`, use `sum = a + b` para tornar o propósito da variável claro.

## 2. Arrumação

A arrumação no desenvolvimento de código refere-se à localização apropriada das partes do código. Certifique-se de que cada parte do seu código esteja onde você espera encontrá-la. Isso torna a manutenção mais fácil e reduz a confusão ao revisitar o código mais tarde. Se uma parte do código não parecer estar no lugar certo, considere reorganizá-la.

## 3. Limpeza

Manter o código limpo é fundamental para a legibilidade e manutenção eficiente. Assim como você não deixaria fios pendurados em um espaço de trabalho organizado, evite deixar linhas de comentários soltas pelo código. Remova comentários obsoletos e garanta que o código seja autoexplicativo por si só, minimizando a necessidade de explicações excessivas por meio de comentários.

## 4. Padronização

Manter um padrão de escrita consistente é vital em projetos de desenvolvimento colaborativo. Siga as diretrizes de estilo de código estabelecidas pela equipe ou comunidade para garantir que o código tenha uma aparência uniforme. Isso melhora a legibilidade e torna mais fácil para outros desenvolvedores entenderem o seu código.

## 5. Disciplina

A disciplina é necessária para aderir consistentemente às boas práticas de desenvolvimento. Assim como você precisa de disciplina para manter um ambiente de trabalho organizado, você também deve adotar uma abordagem disciplinada ao escrever código. Isso inclui nomear variáveis cuidadosamente, manter a estrutura do código coerente e realizar revisões regulares para identificar áreas que precisam ser aprimoradas.

Lembre-se de que escolher um nome para uma variável deve ser tão cuidadoso quanto escolher o nome do seu primeiro filho. A identação adequada também é um indicador estatístico de redução de erros e deve ser praticada para melhorar a legibilidade do código.

# Capítulo 1: A Importância do Código de Qualidade

Um exemplo notável da década de 80 nos mostra como um aplicativo popular se deteriorou devido ao mau código. Inicialmente bem-sucedido, o aplicativo passou a ser instável devido a atualizações apressadas que resultaram em código ruim. À medida que novas funcionalidades foram incorporadas, a estrutura do código se degradou, levando à sua decadência. Escrever código de baixa qualidade tem efeitos devastadores a longo prazo, levando a problemas de estabilidade, necessidade de mais gerenciamento e eventual declínio da produtividade.

A deterioração do código gera uma reação em cadeia. O aumento da complexidade exige mais gerentes, que por sua vez introduzem mais código ruim para atender a prazos apertados. Isso gera frustração, menor produtividade e, em última instância, a ineficiência generalizada. A solução muitas vezes é uma remodelagem liderada por uma "elite", mas frequentemente formada por novos membros, enquanto a equipe original sofre as consequências.

Um código eficaz não contém duplicações e é uma medida de estabilidade e qualidade. A legibilidade é fundamental, pois a leitura do código é uma atividade constante. Simplificar o código para facilitar sua compreensão resulta em economia de tempo a longo prazo.

# Capítulo 2: Princípios para Nomenclatura de Qualidade

Criar nomes significativos é essencial para a clareza do código:

- **Intenção Reveladora**: Nomes de variáveis, funções e classes devem explicar por que existem, o que fazem e como são usados. Evite comentários explicativos desnecessários; um bom nome deve falar por si só. Use nomes claros e evite constantes numéricas. Opte por variáveis com nomes explícitos para melhor compreensão.

- **Evite Desinformação**: Evite nomes que escondam o propósito. Evite abreviações, termos confusos ou ambíguos. Evite usar "List" a menos que seja uma lista. Não use "L" ou "O" como nomes de variáveis, pois se confundem com "1" e "0".

- **Distinções Claras**: Evite nomes semelhantes para coisas diferentes. Nomes como `getActiveAccount()`, `getActiveAccounts()`, `getActiveAccountInfo()` confundem. Escolha nomes distintos e claros.

- **Pronunciabilidade**: Use nomes pronunciáveis e que façam sentido. Nomes como `genymdhms`, `modymdhs`, `pszqint` são ininteligíveis. Prefira `generationTimestamp`, `modificationTimestamp` e `recordId`.

- **Procurabilidade**: Nomes devem ser fáceis de pesquisar. Evite usar letras únicas como `i` e `j` sem um contexto claro.

- **Evite Codificação**: Evite inserir detalhes técnicos nos nomes, como Hungarian Notation.

- **Evite Nomes com uma Única Letra, Salve as Exceções i, j, k**: Evitar nomes de variáveis com uma única letra, a menos que sejam usados em contextos específicos como contadores em laços (`i`, `j`, `k`).

- **Nomes de Classes não Devem Ser Verbos**: Os nomes de classes devem indicar substantivos ou objetos, não ações ou verbos.

- **Use Nomes Técnicos e Específicos**: Quando apropriado, use nomes técnicos e específicos, como nomes de algoritmos ou termos matemáticos, para melhor representar o propósito da variável, função ou classe.



 **Quebre o Código em Pequenas Partes**: Evite definir todas as funcionalidades em uma única classe ou função. Divida o código em pequenas partes, tornando mais fácil para outros entenderem e manterem.

# Capítulo 3: Funções

Funções são componentes essenciais no desenvolvimento de código. Elas têm o propósito de adicionar funcionalidade ao programa. Algumas dicas para construir boas funções:

- **Pequenas e Concisas**: Procure construir funções pequenas, com até 20 linhas, sempre que possível. Isso torna as funções mais fáceis de entender e manter.

- **Identação Adequada**: Limitar funções a uma ou duas linhas de identação torna o código mais compreensível.

- **Blocos Simples**: Em estruturas condicionais como `if`, `else`, e laços como `while`, procure reduzir o bloco de código a uma única linha, preferencialmente chamando outra função.

- **Uma Única Responsabilidade**: Funções devem fazer uma única coisa e fazer bem essa coisa. Evite criar funções com várias funcionalidades.

- **Nomes Descritivos**: Use nomes descritivos para funções. Não tenha medo de usar nomes longos que especifiquem claramente o que a função faz.

- **Evite Codificação**: Evite incluir detalhes técnicos nos nomes das funções.
  
- **Argumentos**: O número ideal de argumentos em uma função é zero. Funções com até dois argumentos são toleráveis, mas evite funções com três ou mais argumentos, a menos que seja extremamente justificável.
- **Evite verificações duplicadas dentro de funções**.
- **Funções devem fazer ou algo ou responder algo, não ambos**.
- **Prefira levantar exceções a mensagens de erro, indicando que o erro deve ser tratado imediatamente**.
- **Djakstra:** Djakstra disse que uma das regras da programação estruturada que cada bloco com uma função deve ter uma entrada ou uma saída, o que quer dizer que uma função deve ter apenas um unico retorno, um laço de repetição não deve ter continue ou break e nunca deve ter um goto. Entretanto essas expressões são excelentes em casos de funções pequenas, salve a excessão do goto que deve ser usado somente em funções maiores.
  ### Conclusão:
 Portanto a partir de agora, quando for escrever funções coloque o seus pensamentos primeiro, isso vai gerar graneds funções, grandes blocos de identação varios laços de repetição, nomes sem sentido, mas a medida que você colocar a suas ideias, implemente todas as dicas vistas até agora e então terá uma função limpa.


## Capítulo 4: Comentários
Comentários são sempre vistos como um fracasso no código. Eles são usados quando não conseguimos expressar claramente o que queremos em nosso código, e seu uso nunca é uma celebração. Em vez de adicionar comentários para explicar códigos confusos, a melhor abordagem é limpar o código. <Br>
Às vezes, usamos comentários para explicar o que uma parte do código faz, como neste exemplo:
```markdown



```javascript
// Verifique se o funcionário tem direito a benefícios completos

if (employee.flags & hourly.flag) ...
```

Mas, na verdade, seria melhor usar uma função que explique o que está acontecendo:

```javascript
if (employee.isEligibleForFullBenefits())
```

Em casos que envolvem expressões regulares, comentários são úteis para explicar como a saída será formatada.

Comentários claros também são úteis ao explicar comparações. Se você sentir a necessidade de escrever um comentário, dedique o tempo necessário para escrevê-lo bem.

Evite comentários redundantes que explicam o que as linhas de código fazem quando as próprias linhas de código já são autoexplicativas.

Comentários que explicam o nome de variáveis ou funções muitas vezes são usados para obscurecer o código, criando uma ilusão de clareza. No geral, esses tipos de comentários estão sendo usados para ofuscar algo e devem ser evitados.



