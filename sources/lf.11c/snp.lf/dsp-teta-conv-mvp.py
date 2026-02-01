# (C) 2026 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]
# for converting a csv file of planking data into a json file: MVP 

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
  return planking_data

# adapters to write planking-data into a file
def write_as_csv(filename,planking_data):
  print(f"writing into csv file <{filename}>")

# main
planking_data_as_csv="res.lf/planking_data.csv"
planking_data=td_hard_coded
if (planking_data):
  write_as_csv(planking_data_as_csv,planking_data)

