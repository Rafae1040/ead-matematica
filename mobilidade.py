# A base de dado é uma copia do dado original esta presente no link abaixo.
!wget -q "https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/develop/dataset/traffic.csv" -O traffic.csv


import pandas as pd

df = pd.read_csv('traffic.csv', sep=';')

df.head()

# O código extrai a 13ª linha de um arquivo, que corresponde à 14ª meia hora do dia 14/12/09, contando a partir das 07:00h. Essa linha representa os incidentes ocorridos na cidade entre 13:30h e 14:00h desse dia.
df.iloc[[13]]