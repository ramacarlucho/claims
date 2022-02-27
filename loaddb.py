import db
import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) < 2:
        file = "claim.csv"
    else:
        file = sys.argv[1]

    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        total = 0
        errored = 0
        for row in spamreader:
            valid = False
            if len(row) < 2:
                errored += 1
                continue
            try:
                balance = str(row[1])
                valid = True
            except:
                print ("cant convert", row)
                errored += 1
                continue
        
            db.set_claimable(row[0], row[1])
            total += 1
        
        print("Finished loading db with ", total, " values")
        print(errored, " values failed to store")

        

