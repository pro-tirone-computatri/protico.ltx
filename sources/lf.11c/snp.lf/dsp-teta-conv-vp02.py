# (C) 2026 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]
# for converting a csv file of planking data into a json file: VP-0.2 

# intermediate representation and hard-coded test data set of planking data
td_hard_coded=[ 
  { "set": 1, "day": "2026-01-01", 
    "shall1": 30, "is1": 32, "shall2": 20, "is2": 18, "shall3": 15, "is3": 15}, 
  { "set": 2, "day": "2026-01-02", 
    "shall1": 30, "is1": 35, "shall2": 25, "is2": 22, "shall3": 20, "is3": 18} ]

# adapters to read planking-data from a file: 
def fill_from_csv(filename) :
  print(f"reading from csv file <{filename}>")
  planking_data=[]
  inf=open(filename,"r")
  # keep it simple: let the program crash if filename does not exist
  for line in inf:
    csv_str=line.strip()
    (id,dy,s1,i1,s2,i2,s3,i3)=csv_str.split(',')
    planking_data.append({ "set": id, "day":dy,
      "shall1":s1,"is1":i1,"shall2":s2,"is2":i2,"shall3":s3,"is3":i3,})
  return planking_data

# adapters to write planking-data into a file
def write_as_csv(filename,planking_data):
  print(f"writing into csv file <{filename}>")
  ouf=open(filename,"w")
  # keep it simple: let the program crash if filename does not exist
  for ds in planking_data:
    ouf.write(f"{ds["set"]},{ds["day"]},{ds["shall1"]},{ds["is1"]},"
      f"{ds["shall2"]},{ds["is2"]},{ds["shall3"]},{ds["is3"]}\n")
  return ouf.close()

# main
planking_data_file="dsp.lf/dsp.teta-c.csv"; # cleared data set
planking_data_test_file="dsp.lf/dsp.teta-t.csv"; # test data set
planking_data_as_csv="res.lf/planking_data.csv"
planking_data_as_json="res.lf/planking_data.json"

planking_data=fill_from_csv(planking_data_file)
#planking_data=td_hard_coded
if (planking_data):
  write_as_csv(planking_data_as_csv,planking_data)

