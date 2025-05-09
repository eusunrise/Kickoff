# Kickoff
Projeto análise e projeto de software

Plataforma de Doação de Roupas e Alimentos

Equipe:
Ederval Gomes de Novaes Neto - RA 850645
Ian de Sousa Pereira - RA 850687
Carlos Roberto - RA 853313
Kilber Fernando - RA 853134

trello:
https://trello.com/invite/b/681928d2ab3dcad6c32bb540/ATTI7029eddf7a120e5a90e9b2160fc945b77070940C/analise-e-projeto-de-software

Sobre o Produto
A Plataforma de Doação de Roupas e Alimentos é um site criado para aproximar quem quer doar roupas e alimentos de quem realmente precisa delas, seja uma pessoa ou uma instituição. Com ela, você pode:

Cadastrar doações, informando detalhes das peças/Alimentos como tipo, tamanho/quantidade e estado de uso/validade;
Mapear pontos de entrega e retirada, ajudando a organizar melhor a logística e facilitar a vida de todo mundo;
Navegar por uma interface simples e fácil de usar, tanto para quem está doando quanto para quem vai receber.
A ideia é incentivar a solidariedade, dar uma nova vida às roupas paradas no armário e fornecer alimentos para quem está passando por dificuldades.

Historias com as personas:

Primeira Historia, Autor: Carlos Roberto.

-Como um comerciante de bairro
Quero cadastrar alimentos excedentes que estão próximos da validade
Para que eles possam ser doados para instituições que atendem pessoas em situação de vulnerabilidade

Cenário: João, dono de uma mercearia, acessa o sistema de doações comunitárias. Ele percebe que tem 10 pacotes de arroz com validade próxima (5 dias restantes). Ele clica em "Nova Doação", preenche o formulário com as seguintes informações:

Tipo de item: Alimento não perecível

Quantidade: 10 pacotes

Validade: 5 dias

Descrição: "Arroz branco tipo 1, pacote de 1kg, lacrados"

Local da doação: Mercearia Esperança, Rua das Acácias, nº 45

Após confirmar o cadastro, ele recebe uma notificação no painel que informa que a doação foi publicada e está aguardando mapeamento de retirada.

Critérios de Aceitação:

A doação deve ser listada como "Disponível" no sistema

O sistema deve armazenar todas as informações inseridas

Segunda Historia, Autor: Ian de Sousa

- Solicitar Retirada de Doação
Como uma instituição cadastrada
Quero solicitar a retirada de uma doação disponível
Para que possamos coletar os alimentos e distribuí-los a quem precisa

Cenário:
A instituição “Casa Solidária” vê uma doação de frutas com validade próxima e decide solicitar a retirada. Ela clica no botão “Solicitar Retirada”, confirma o endereço de coleta e envia a solicitação.

Critérios de Aceitação:

O botão “Solicitar Retirada” deve estar visível apenas para instituições logadas

Após a solicitação, o status da doação muda para “Retirada Solicitada”

A instituição deve poder visualizar um resumo da solicitação enviada

A data e hora da solicitação devem ser armazenadas no banco.

Terceira Historia, Autor: Kilber Fernando.

-Como um administrador do sistema
Quero revisar e aprovar manualmente as doações cadastradas
Para que apenas itens adequados sejam disponibilizados para retirada

Cenário: Após um usuário cadastrar uma doação de roupas usadas, o sistema envia automaticamente a doação para o painel de "Doações Pendentes" da equipe administrativa.

Fernanda, administradora do sistema, acessa a lista de pendentes. Ela revisa a descrição da doação, a imagem enviada e os dados de validade e quantidade. Como está tudo de acordo com os critérios (roupas em bom estado, dentro das categorias aceitas), ela clica em "Aprovar Doação".

A doação então se torna visível para voluntários no mapa e na listagem geral. Caso houvesse algo errado (como item proibido ou descrição incompleta), ela poderia recusar a doação, justificando o motivo.

Critérios de Aceitação:

O sistema deve permitir aprovar ou recusar doações pendentes

Em caso de recusa, o motivo deve ser registrado e comunicado ao doador

A aprovação torna a doação pública e visível no mapa/listagem

Quarta Historia, Autor; Kilber Fernando.

-Como um voluntário de logística
Quero visualizar as doações disponíveis em um mapa interativo com localização geográfica
Para que eu possa planejar rotas eficientes de coleta

Cenário: Larissa, voluntária responsável por buscar doações, acessa a seção "Mapa de Doações". Ela vê no mapa um marcador indicando a localização da mercearia do João (história anterior). Ao clicar no marcador, uma janela pop-up exibe os detalhes da doação.

Ela seleciona a opção "Agendar Retirada", escolhe a data e horário para coleta, e adiciona observações como "Levarei veículo com capacidade para 100kg". O sistema registra a retirada e atualiza o status da doação para "Aguardando Entrega".

Critérios de Aceitação:

O mapa deve exibir doações geolocalizadas

A função "Agendar Retirada" deve registrar data, horário e observações

O status da doação deve mudar automaticamente

Quinta Historia, Autor: Ian de Sousa

-Confirmar Entrega da Doação
Como um comerciante doador
Quero confirmar que a instituição retirou a doação
Para que o sistema mantenha o histórico de entregas e atualize o status da doação

Cenário:
João, após entregar os pacotes de arroz à ONG “Casa Solidária”, acessa o painel e confirma a entrega.

Critérios de Aceitação:

O comerciante deve ter acesso à lista de doações com retirada solicitada

Ao clicar em “Confirmar Entrega”, o status da doação deve ser alterado para “Concluída”

A data/hora da confirmação deve ser registrada no banco

A instituição deve receber uma notificação (no painel) de que a entrega foi confirmada

Sexta Historia, Autor: Carlos Roberto

Como um entregador voluntário
Quero registrar que realizei a entrega da doação em uma instituição
Para que o sistema mantenha o histórico de doações concluídas e as instituições possam dar feedback

Cenário: Rafael, após coletar as doações, leva os pacotes até o abrigo “Casa Solidária”. Ao chegar, ele acessa o sistema pelo celular, vai até a aba "Minhas Entregas", seleciona a doação da mercearia João e clica em "Registrar Entrega".

Ele insere uma foto da entrega, o nome da pessoa que recebeu, e comentários como "Doação entregue sem avarias". O sistema registra essa entrega e envia uma notificação para o comerciante João com agradecimentos automáticos e a confirmação da entrega.

Critérios de Aceitação:

Deve ser possível registrar uma entrega com foto, nome do recebedor e comentário

O sistema deve notificar o doador automaticamente

A doação deve mudar de status para "Entregue com sucesso"

Sétima Historia, Autor: Ederval Gomes

Como uma instituição cadastrada quero poder cancelar uma solicitação de retirada feita anteriormente para que possamos liberar a doação para outras instituições em caso de imprevisto.

Cenário:
A ONG “Mãos Unidas” solicita a retirada de uma doação de pães, mas por falta de transporte, decide cancelar a solicitação no mesmo dia. Ela acessa o painel da plataforma e clica em “Cancelar Solicitação”.

Critérios de Aceitação:

O botão “Cancelar Solicitação” deve estar visível apenas enquanto o status for “Retirada Solicitada”

Após o cancelamento, o status da doação deve voltar para “Disponível”

A ação deve ser registrada com data e hora no banco de dados

Outras instituições devem poder visualizar a doação novamente após o cancelamento.

Oitava Historia, Autor: Ederval Gomes

Como uma instituição cadastrada quero avaliar a qualidade da doação recebida para que os doadores recebam feedback e o sistema mantenha um histórico de reputação

Cenário:
Após receber um lote de legumes, a instituição “Esperança Viva” avalia a doação com 4 estrelas e comenta sobre a boa qualidade dos produtos.

Critérios de Aceitação:

A avaliação deve estar disponível apenas após o status da doação ser “Concluída”

A nota e comentário devem ser armazenados no banco de dados

O doador deve poder visualizar as avaliações recebidas em seu painel

Cada doação pode ser avaliada uma única vez por instituição.

Nona Historia, Autor: Ederval Gomes

Como uma pessoa física, quero acessar um histórico das doações realizadas ou recebidas para que eu possa acompanhar o impacto das ações ao longo do tempo

Cenário:
João acessa seu painel e vê todas as doações que já fez, incluindo datas, status e instituições beneficiadas. Da mesma forma, a ONG “Casa Solidária” pode ver as doações que recebeu.

Critérios de Aceitação:

O histórico deve mostrar a lista de doações com status, datas e nomes das partes envolvidas

Deve ser possível filtrar por data, status e tipo de alimento

Os dados devem estar ordenados do mais recente para o mais antigo

A informação deve ser acessível apenas para usuários autenticados.

Decima Historia, Autor: Ederval Gomes

Como uma instituição cadastrada quero ser notificada quando uma nova doação for disponibilizada na minha região para que eu possa agir rapidamente e solicitar a retirada, se necessário

Cenário:
A ONG “Alimento para Todos” recebe uma notificação em seu painel informando que uma padaria próxima disponibilizou uma doação de pães frescos.

Critérios de Aceitação:

A notificação deve ser enviada automaticamente quando uma nova doação for cadastrada por um comerciante próximo

A notificação deve conter o tipo de alimento, quantidade e validade

A instituição deve poder acessar os detalhes da doação a partir da notificação

A notificação deve ser registrada no sistema e exibida no painel da instituição.
