import csv
#
# with open("example.tsv") as f:
#     reader = csv.reader(f, delimiter="\t")
#     for row in reader:
#         print(row)
#         print(int(row[2]))
dd={}
k=0
with open("Crimes.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if k>0:
                dd[row[6]]=+1
            k+=1
            if k>100:
                break
            # print(int(row[2]))

# students = [
#     ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]
#
# with open("example.csv", "a") as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(students)
