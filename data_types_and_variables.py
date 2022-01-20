#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

littleMermaid = 3
brotherBear = 5
hercules = 1 
rentalLst = [littleMermaid, brotherBear, hercules]

price = sum(rentalLst) * 3

print (price)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

googlePay = 400
amazonPay = 380
facebookPay = 350 

googleHrs = 6
amazonHrs = 4
facebookHrs = 10

payment = (googlePay * googleHrs) + (amazonPay * amazonHrs) + (facebookPay * facebookHrs)

print (payment)

#A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

classFull = False
scheduleConflict = False

enrolled = not (classFull or scheduleConflict)

print (enrolled)

#A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.

premiumMem = True
currentOffer = False 
noItems = 2

offer = currentOffer and (noItems > 2 or premiumMem)

print(offer) 

#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace 

username = 'codeup'
password = 'notastrongpassword'

userChar = len(username) < 20
passChar = len(password) >= 5

passUserSame = username == password

validRegistration = userChar and passChar and not passUserSame

print (validRegistration)

#bonus
userSpace = username[0] == ' ' or username[-1] == ' '
passSpace = password[0] == ' ' or password[-1] == ' '

validRegistration = userChar and passChar and not passUserSame and not (userSpace or passSpace)

print (validRegistration)