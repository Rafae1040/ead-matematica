# -- read

data = None

with open(file='traffic.csv', mode='r', encoding='utf8') as fp:
   
   fp.readline()
   data = fp.read()

# -- analytics 

import numpy as np

day = 14
incidents = 0
incident_by_day = dict()

for timebox in data.split(sep='\n'):

  timebox_data = timebox.split(sep=';')

  # --
  # -- inicio da computação vetorial
  # --
  
  
  incidents = incidents + np.sum(np.array(list(map(int, timebox_data[1: len(timebox_data)-1]))))

  # --
  # --  fim da computação vetorial
  # --

  try:

    half_hour = int(timebox_data[0])

    if half_hour == 27:
      incident_by_day[day] = incidents
      day = day + 1
      incidents = 0
  
  except ValueError:
    continue

  # -- results

for day in incident_by_day:

  print(f'{day}: {incident_by_day[day]}')