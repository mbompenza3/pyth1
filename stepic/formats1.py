import csv,re
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
            if re.search(r'/2015',row[2]):
                if k > 0:
                    if row[5] not in dd:
                        dd[row[5]] = 1
                    else:
                        dd[row[5]] += 1
                k += 1


            # print(int(row[2]))
        print(k)
        print(dd.values())
        print(max(dd.values()))
        print(sorted(dd.items(), key=lambda x:x[1], reverse=True))
        print((dd))
# students = [
#     ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
#     ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
# ]
#
# with open("example.csv", "a") as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(students)
