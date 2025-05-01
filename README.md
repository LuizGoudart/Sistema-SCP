# Sistema-SCP
Sistema de Controle de Presença - Projeto para a Faculdade

Manual de Uso - Sistema de Controle de Presença 
Visão Geral 
Este aplicativo foi desenvolvido para facilitar o registro de presenças de alunos de 
forma simples e prática. 
Início do Sistema Ao abrir o aplicativo 
O sistema verifica automaticamente se já existe um arquivo de registro chamado 
presenca.xlsx.  
• Se o arquivo existir, o aplicativo perguntará se você deseja utilizá-lo; 
• Se o arquivo não existir, o aplicativo perguntará se deseja criar um novo 
arquivo para armazenar os registros; 
• O arquivo de registro conterá as seguintes informações: Data, Turma, Aluno, 
Presença. 
Interface do Aplicativo 
A interface é simples e intuitiva, contendo os seguintes campos e botões: 
• Data (Opcional): Permite informar a data no formato dd/mm/aaaa. Se deixar em 
branco, será utilizada a data atual automaticamente; 
• Turma: Campo obrigatório para informar a turma do aluno (exemplo: 3A); 
• Nome do Aluno: Campo obrigatório para informar o nome completo do aluno; 
• Existem dois botões principais: 
o Presente: Registra o aluno como presente. 
o Ausente: Registra o aluno como ausente. 
Como Registrar uma Presença 
• Preencha os campos obrigatórios (Turma e Nome do Aluno); 
• (Opcional) Preencha o campo Data se quiser indicar uma data diferente da 
atual; 
• Clique no botão Presente para registrar a presença ou no botão Ausente para 
registrar a ausência; 
• Uma mensagem de confirmação aparecerá informando que o registro foi feito 
com sucesso; 
• O campo do nome do aluno será automaticamente limpo para facilitar o 
próximo registro. 
Estrutura do Registro 
Cada registro será adicionado como uma nova linha no arquivo presenca.xlsx, 
conforme o formato abaixo: 
Data 
Turma 
Aluno 
28/04/2025 
3A 
João Menezes 
Presença 
28/04/2025 
Presente 
3A 
Maria dos Santos 
28/04/2025 
Presente 
3A 
Annah Azevedo 
Ausente 
Recomendações de uso mantenha o arquivo presenca.xlsx na mesma pasta do 
aplicativo. 
Para começar um novo registro, você pode apagar o arquivo atual (presenca.xlsx) e 
abrir o aplicativo novamente, que oferecerá a criação de um novo arquivo.
