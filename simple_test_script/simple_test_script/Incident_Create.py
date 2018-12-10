from random import randint

iterations = 2 # Number of time application loops
Resource1ToDispatch = "42"
Resource2ToDispatch = "M1"
Resource3ToDispatch = "C1"

addressList = ["5125 Harvard Blvd", 
"945 Saint Johns Rd",
"250 MONROE RD",
"3715 Bald Knob Rd",
"875 Bark Branch Rd",
"3464 Saint Johns RD",
"70 Royal Pkwy",
"9680 Old Owenton RD",
"2800 Harvieland RD",
"144 Wright RD",
"2225 PETTY RD",
"2350 STONE HOLLOW RD",
"5233 HUNTINGTON WOODS RD"]

numberOfAddresses = len(addressList) - 1

for i in range(iterations):
    randnum = randint(0,numberOfAddresses)
    randomAddress = addressList[randnum]
