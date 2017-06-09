from urllib.request import urlopen
def read(filename):
  file = open(filename, "w")
  data = urlopen("http://137.164.121.254:9001/static/"+filename)
  context = data.readlines()
  for line in data.readlines(): file.write(line.rstrip())
  file.close()
  return filename
def send(data):
  return urlopen("http://137.164.121.254:9001/data.txt/secuwrite/"+str(data)) == "True"
