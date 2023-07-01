# lotofacilRNA
Esse código foi criado para gerar uma sequência de SUGESTÕES de números da loteria LotoFacil.

#Funcionamento
O código está em execução via CRONTAB todos os dias em um servidor na nuvem (Oracle Cloud)

Esse código foi adaptado do artigo: https://medium.com/@polanitzer/how-to-guess-accurately-3-lottery-numbers-out-of-6-using-lstm-model-e148d1c632d6

Utiliza-se como entrada todos os resultados passados da Lotofacil, analisa esses dados utilizando rede neural e tenta predizer o próximo sorteio da LotoFacil.
O código possui 6 etapas:
   -(geraDados.py) Extraí da internet o último resultado da Lotofacil;

   -(geraNum1.py) Gera os 5 números mais frequentes dos ultimas 100 concursos e salva a informação em um arquivo;

   -(lstmCode1.py) Análise e predição dos números;
   
   -(validaLSTM.py) Validação se os números gerados estão OK dos padrões estatísticos dos últimos sorteios;

   -(normalizaLSTM.py) Extrai os dados da saída da RNA, abre os números mais sorteados dos últimos 100 concursos. Retira os números zeros e números repetidos encontrados no arquivo de saída da RNA. Substitui por números obtidos
do arquivo de mais sorteados

   -(formataLSTM.py) Formata o arquivo 'outputRNA_Modificado.csv' obtido na normalização e aplica a validação de SOMA. Se a somatória dos números estiver entre 170 e 220, é sugerido que se trata de um palpite válido. Se não estiver nesse range, não é válido.

   -(gitUpload.py) Envia o resultado obtido automaticamente para essa página GIT.
   


