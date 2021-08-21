print("Reading Data...")
raw_data = open("C:/Users/bns36/Documents/Mail Client/Data/unsorted_mail.txt", "r", encoding="utf8")
raw = raw_data.read().splitlines()
raw_data.close()
list_length = len(raw)
print("Raw Data Total = " + str(list_length))

print("Splitting List and Eliminating Duds...")
Duds = 0
raw_list = []
for x in raw:
    seperate_data = x.split(":")
    email = seperate_data[0]
    try:
        domain = email.split("@")
        if (domain[1] == "gmail.com") or (domain[1] == "hotmail.com") or (domain[1] == "outlook.com"):
            raw_list.append(email)
    except:
        Duds = Duds + 1

print("Duds Found:" + str(Duds))


print("Reducing to 5000...")
count = 0
email_list = []
while count != 5000:
    pull = raw_list[count]
    email_list.append(pull)
    count = count + 1

print("Inserting Spam Checker")
spam_checker = "paperweightofficial@outlook.com"
intervals = [250, 500, 750, 1000,
             1250, 1500, 1750, 2000,
             2250, 2500, 2750, 3000,
             3250, 3500, 3750, 4000]

for data in intervals:
    email_list.insert(data, spam_checker)

print("Writing Data")
write_data = open("C:/Users/bns36/Documents/Mail Client/Data/sorted.txt", "w", encoding="utf8")
for item in email_list:
    write_data.write(item + "\n")

print("Task Complete!")