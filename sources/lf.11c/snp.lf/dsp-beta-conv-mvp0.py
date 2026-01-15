# (C) 2026 K.Reincke: proTironeComputatri snippet [CC-BY-4.0]

# converts a csv file of day data into the respective ini file
# minimal viable product 0: empty logical structure

# structure of the intermediate representation
# a list () of dictionaries {}, each filled with four key-value-pairs

dd_hard_coded=(
{ "day":"2026-01-01", "sunrise": "08:29","sunset": "16:31","durance": "08:02"},
{ "day":"2026-01-02", "sunrise": "08:29","sunset": "16:32","durance": "08:03"}
)

# adapters to read daydata from a file
def fill_from_csv(filename) :
  print(f"reading from csv file <{filename}>")
  daydata=()
  return daydata

# adapters to write daydata into a file
def write_as_csv(filename,daydata):
  print(f"writing into csv file <{filename}>")

# main

# the clarified version of dsp.beta.xyz:
# data-set-0 - data-set-3. accepted, data-set-4 rejected: inconsistent double
dd_file="dsp.lf/dsp.beta.csv";
dd_test_file="dsp.lf/dsp.beta-td.csv";
dd_csv_file="res.lf/daydata.csv";
dd_ini_file="res.lf/daydata.ini";

daydata=fill_from_csv(dd_test_file)

daydata=dd_hard_coded
if (daydata):
  write_as_csv(dd_csv_file,daydata)
