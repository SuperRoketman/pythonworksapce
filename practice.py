# weather = input("how is the weather?")
# if weather == "rain" or weather == "snow":
#     print("bring a umbrella")
# elif weather == "dust":
#     print("bring a mask")
# else:
#     print("bring nothing")

temp = int(input("how is the tempertuer?"))
if 30 <= temp:
    print("it is too hot. stay in")
elif 10<= temp and temp<30:
    print("bring a coat")
else:
    print("it is too cold. stay in")