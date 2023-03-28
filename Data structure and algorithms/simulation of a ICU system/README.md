# Problema 2 - Regulação de Leitos de UTI

## Objetivos
* Analisar os requisitos de um problema real, propondo uma solução computacional;
* Construir um protótipo de teste baseado na solução proposta;
* Entender os processos de manipulação de arquivos em Python.
* Construir um simulador capaz de criar demandas e disponibilidade de leitos
* Criar uma interface, em que é possível verificar a situação do sistema a cada fração de tempo

## Resumo do problema
Uma empresa que desenvolveu um sistema de regulação de leitos durante a pandemia está com processo seletivo aberto. Eles requisitaram aos candidatos que elaborassem um protótipo/simulador que tivesse a capacidade de criar demandas e disponibilidades de leitos, além disso o núcleo deve ser genérico de versátil, dado o fato de que o sistema provavelmente será expandido no futuro. Outrossim, o uso de estruturas prontas do própria Python é proibido, todas as estruturas de dados utilizadas devem ser construídas pelo próprio candidato.

## Construção do Simulador
Para a construção do código, primeiro foi necessário pensar de que forma o simulador operaria. Minha tese foi a seguinte: os dados contendo a idade e o estado dos pacientes chegariam ao sistema ao mesmo tempo que os dados dos diferentes tipos de leitos também chegariam ao sistema, nesse momento seria gerado um relatório da quantidade de leitos disponibilizados e da quantidade de pacientes totais na fila. Após isso o sistema faria uma espécie de peneira, os pacientes que mais precisam dos leitos seriam designados para os leitos respectivos a sua idade, à medida que estes estivessem disponíveis, caso contrário, o paciente permaneceria na fila de alta prioridade. Depois de fazer essa "peneira", o sistema geraria mais um relatório contendo os pacientes restantes na fila de espera, os leitos restantes, o número de pacientes que morreram enquanto esperavam por vagas de UTI e também o número de pacientes que melhoraram e não precisariam mais de vagas de UTI, note que nesses dois casos o paciente seria removido da fila de espera.

Assim, comecei meu código a partir da classe paciente, o paciente tem 3 atributos: ID, idade e estado. O número de ID de cada paciente é único e requisito para a construção de um objeto da classe paciente. Por outro lado, a idade e os estados eram dados de forma aleatória. Note que, a classe foi construída de modo que há mais chances do paciente ser um adulto ou criança do que um da categoria neonatal, e também, as chances de atribuição a um estado do paciente são diferentes. Além disso, foi necessário criar um método dentro da classe que seria responsável por dizer se um paciente melhorou, piorou ou morreu.

O primeiro passo pra criar o simulador já estava completo, no entanto havia a necessidade de usar TADs que tivessem a capacidade de armazenar e contabilizar a quantidade de pacientes e de leitos. Visando armazenar os pacientes, o tipo de TAD escolhida foi a queue(fila), pois respeita a lógica de uma verdadeira fila de hospital, em que o primeiro a chegar é o primeiro a ser atendido. E para os leitos foi escolhido stack(pilha), que também respeitava os requisitos do problema, o qual dizia que o último leito a chegar era o primeiro a sair. Essas TADs foram implementadas utilizando o conhecimento já obtido em sala de aula sobre elas.

Por fim, a cereja do bolo, o simulador. Ele foi construído como uma classe, pois eu queria utiliza-lo novamente na construção de uma interface gráfica. Os únicos atributos do simulador são variáveis de contagem de dados e as respectivas filas e pilhas necessárias. Havia a possibilidade de utilizar a TAD filas de prioridade, no entanto fui desencorajado devido à grande dificuldade de implementar sem o uso de TADs do próprio Python e também, devido ao grande número de operações de busca, remoção e etc que teriam de ser feitas. Por isso, optei por criar 9 filas diferentes, elas são classificadas quanto a idade/estado, e criei 3 pilhas diferentes, que são classificadas apenas quanto a idade.

O primeiro método criado foi o de preencher as filas, esse método começa gerando um número k aleatório correspondente a quantidade de pacientes que serão criados, o paciente criado recebe sua ID única e a partir de seu estado/idade é direcionado para sua respectiva fila.

O segundo método foi o gerador de leitos, ele também começa gerando um número k aleatório correspondendo a quantas vezes o gerador de leitos vai atuar. Essa parte foi alterada no final do trabalho, portanto vou rapidamente explicar como ficou o resultado final. Uma TAD de leitos foi criada, com 3 atributos: id, idade e hospital, também foram criados 2 métodos responsáveis por randomizar os dois últimos atributos, os métodos são chamados assim que um objeto da classe é criado, enquanto a id é um parâmetro pra se criar o objeto, assim como ocorre com a TAD paciente. Voltando ao gerador de leitos do simulador, dependendo do atributo idade do leito criado, ele designa esse leito para uma das pilhas que lhe é correspondente.

O terceiro método foi o de alocar os pacientes, ele simplesmente verifica o estado das pilhas de leitos e das filas de pacientes, caso haja um paciente X esperando por um leito e haja um leito disponível, o método vai atribuir o leito ao paciente e irá remover ambos de suas respectivas pilhas e filas, caso o paciente X esteja esperando pelo leito e não haja leito, o método não vai fazer nada e caso não haja paciente na fila e haja leitos disponíveis, nada será feito.

O quarto método é responsável pela gerencia das filas, é nele que também ocorre a randomização do estado do paciente. Para se tornar mais claro e visualizar e operar, foram criadas 9 filas auxiliares. Então, o método percorre cada umas das filas originais, retira o primeiro paciente e o guardar em uma variável auxiliar, o método da classe paciente de randomizar o estado é utilizado e após a atualização do estado do paciente podem acontecer 3 coisas, o paciente é alocado em uma das filas auxiliares compatíveis com seu novo estado, o paciente pode morrer e assim é retirado da fila, ou o paciente melhora a ponto de não precisar mais de um leito de UTI, assim ele também é retirado da fila. É importante dizer que, no final do método, todas as filas auxiliares são esvaziadas e os pacientes que elas guardavam são passados para as filas originais, de modo que suas propriedades compatíveis com idade/estado são mantidas.

O quinto e último método é simplesmente o método responsável por atualizar os valores das variáveis de contagem após a utilização de cada um dos métodos do simulador.

Bom, todos esses métodos poderiam ser colocados na ordem desejada como atributos da própria classe, no entanto, como eu queria criar a interface gráfica e não havendo paralelização do código, isto não poderia ser feito dessa forma.

## Considerações acerca da construção da interface gráfica
O módulo utilizado foi o tkinter, ele já vem contido no próprio Python a partir da versão 3.7. Caso a versão do Python seja inferior a 3.7, é recomendado a atualização do Python. No entanto, caso não seja possível, o mapa da situação do simulador também poderá ser visto ao executar o módulo "main1.py" ao invés do “main.py”. Inclusive, recomendo fortemente que o módulo "main1.py" seja executado, já que nele as informações são mostradas a medida que os métodos são executados, enquanto na interface gráfica utilizando o tkinter eu não consegui fazer isso.

Acerca da construção da interface, achei conveniente criar uma classe para tal, já que o código fica mais limpo e muitas vezes é muito mais simples de fazer algumas ações.

A classe foi criada no módulo "CGraphicInt.py", e ela contém alguns atributos básicos necessários para a aplicação rodar, como o delay(referente ao tempo necessário para as informações serem atualizadas na tela), o running(é necessário pra poder pausar a simulação, e posteriormente começar ela novamente), e o simulador que é basicamente um objeto da classe simulador, a qual já foi criada e explicada anteriormente.

O primeiro método da classe é o "start", é ele quem dá início ao simulador tornando o running = True, é a partir dele também que a função "startSimula" é ativada, e é ela quem executa os métodos da classe simulador, no caso, a ordem escolhida pelos métodos é preencher filas, gerar leitos, alocar pacientes, retornar valores, randomizar estado dos pacientes e por fim retornar valores novamente. Como já dito ateriormente, não foi possível mostrar o mapa da situação a medida que o programa é exeutado, ele apenas atualizada os dados ao final da execuçã de todos os métodos pré-estabelecidos. De qualquer forma, no final da função chamamos o método after(), ele é responsável por mandar uma mensagem pro mainloop(), pra rodar novamente uma função(nesse caso, é a "startSimula" ), em n(nesse caso foram 1000) milisegundos, dessa forma o programa entra em recursão enquanto a variável runnning == True. O resto do código referente ao método start é apenas referente a textos, fontes, cores e informações que serão exibidas na janela da interface gráfica.

O segundo método é o "stop", ele simplesmente torna running=False, portanto, a função recursiva para e o simulador também para.

## O código rodando
No "main.py", o módulo CSimulador, CGraphicalInt e o tkinter foram importados. Aqui eu decidi criar outra interface gráfica do tkinter, essa interface gráfica é responsável por comandar a interface gráfica dentro da classe "gInterface". Essa interface gráfica contêm 3 botões, o "START", "STOP" e o "QUIT", o START executa a função "start" da classe gInterface, o STOP executa, a partir da função lambda, a função "stop" do gInterface, além de executar a função destroy() que é responsável por encerrar a interface gráfica em questão, e o QUIT executa a função "quitControl" que chama um destroy() para a interface gráfica criada dentro da classe "gInterface" e para interface gráfica criada no main.py ou somente para interface gráfica criada no "main.py".

Para o "main1.py" eu criei um outro módulo a fim de tornar o código mais limpo, nesse módilo (mapInterface), foram importados os módulos "time" e o "os" do Python com o objetivo de controlar o tempo que os dados aparecem na tela e apagar os dados já existentes para apresentar os novos, respectivamente. Como já foi dito anteriormente, as informações aqui são mostradas cada vez que algum método da classe simulador é executada. No mais, eu gostaria de causar a interrupção do programa com uma tecla do keyboard, no entanto haveria necessidade de instalar um módulo exterior, por isso a solução é usar o ctrl+C, essa combinação de teclas já serve pra interromper o programa.

## Explicando cada uma das informações mostradas na interface gráfica ou no terminal
* Pacientes totais - Referente ao número total de pessoas que o simulador recebeu dados(isso inclui as pessoas que logo foram retiradas da fila de espera por não apresentarem necessidade de leitos de UTI).
* Leitos disponibilizados - Quantidade total de leitos que o simulador recebeu dados.
* Fila de espera(Adulto) - Quantidade de adultos esperando por um leito.
* Fila de espera(Pediátrico) - Quantidade de crianças esperando por um leito.
* Fila de espera(Neonatal) - Quantidade de bebês esperando por um leito.
* Fila de espera - Quantidade total de pacientes esperando por um leito.
* Leitos disponíveis(Adulto) - Quantidade de leitos disponíveis para adultos.
* Leitos disponíveis(Pediátrico) - Quantidade de leitos disponíveis para crianças.
* Leitos disponíveis(Neonatal) - Quantidade de leitos disponíveis para bebês.
* Melhoraram - Quantidade de pacientes que melhoraram enquanto esperavam e, portanto, foram removidos da fila de espera.
* Morreram - Quantidade de pacientes que morreram enquanto esperavam e, portanto, foram removidos da fila de espera.


## Referências bibliográficas

Data Structures & Algorithms in Python - Michael T.Goodrich, Roberto Tamassia, Michael H. Goldwasser

Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática

https://www.markdownguide.org/basic-syntax/

https://federacaors.org.br/os-melhores-hospitais-do-mundo-2022/

https://www.pythontutorial.net/tkinter/

