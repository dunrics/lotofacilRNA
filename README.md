# lotofacilRNA
Esse código foi criado para gerar uma sequência de SUGESTÕES de números da loteria LotoFacil.

#Funcionamento

Esse código foi adaptado do artigo: https://medium.com/@polanitzer/how-to-guess-accurately-3-lottery-numbers-out-of-6-using-lstm-model-e148d1c632d6

Utiliza-se como entrada todos os resultados passados da Lotofacil, analisa esses dados utilizando rede neural e tenta predizer o próximo sorteio da LotoFacil.
O código possui 3 etapas:

   -(lstmCode1.py) Análise e predição dos números;
   
   -(validaLSTM.py) Validação se os números gerados estão OK dos padrões estatísticos dos últimos sorteios;
   
   -(gitUpload.py) Envia o resultado obtido automaticamente para essa página GIT.
   

O código está em execução via CRONTAB todos os dias em um servidor na nuvem (Oracle Cloud)
