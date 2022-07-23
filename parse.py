"""
Parses through a job company text and adds that to master csv file.
"""
import csv

with open("The Really Big Hugely Ginormous Tech Company List - Sheet1.csv", "r", encoding = "UTF-8") as file:
    with open("Top Technology Company Internships - Sheet1.csv", "r+", encoding = "UTF-8", newline='') as file2:
        master_spreadsheet = []

        # lines = file.readlines()
        lines = csv.reader(file)

        lines2read = csv.reader(file2)
        lines2write = csv.writer(file2)
        for line in lines2read:
            master_spreadsheet.append(line)
        position1, position2 = 0,0
        for line in lines:
            # for count, character in enumerate(line):
            #     if character == "[":
            #         position1 = count
            #     elif character == "]":
            #         position2 = count
            #         break
            name_company = line[1]
            flag = 0
            for row in master_spreadsheet:
                if row[2] == name_company.lower():
                    value = int(row[1])
                    value += 1
                    row[1] = value
                    flag = 1
                    break
            if flag == 0:
                master_spreadsheet.append([name_company, 1, name_company.lower()])
            file2.seek(0)
        for row in master_spreadsheet:
            lines2write.writerow(row)
            