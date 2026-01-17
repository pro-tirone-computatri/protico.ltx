# (C) 2026 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]

# converts a csv file of day data into the respective ini file: MVP

# intermediate representation and hard-coded testdata
dd_hard_coded=(
{ "day":"2026-01-01", "sunrise": "08:29","sunset": "16:31","durance": "08:02"},
{ "day":"2026-01-02", "sunrise": "08:29","sunset": "16:32","durance": "08:03"}) 

# adapters to read daydata from a file: 
def fill_from_csv(filename) :
  print(f"reading from csv file <{filename}>")
  daydata=()
  return daydata

# adapters to write daydata into a file
def write_as_csv(filename,daydata):
  print(f"writing into csv file <{filename}>")

# main
dd_csv_file="res.lf/daydata.csv"

daydata=dd_hard_coded
if (daydata):
  write_as_csv(dd_csv_file,daydata)

