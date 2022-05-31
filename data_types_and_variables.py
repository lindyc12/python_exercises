
from operator import truediv


the_little_mermaid = 3 * 3
brother_bear = 5 * 3
hercules = 3 * 1
print("The total price will be $" + str(the_little_mermaid + brother_bear + hercules))


google = 400 * 8
amazon = 380 * 6
facebook = 350 * 3
print("my total this week will be $" + str(google + amazon + facebook))


is_not_full = True
does_not_conflict = True
if (is_not_full and does_not_conflict) == True:
    print("can be enrolled")


more_than_two = True
not_expired = True
is_premium = True
if ((more_than_two and not_expired) or is_premium) == True:
    print ("offer can be applied")




username = 'codeup'
password = 'notstrongpassword'


at_least_five_characters = len(password) > 5
at_least_five_characters

username_20_characters_or_less =len(username) <= 20
username_20_characters_or_less


username_no_whitespace = username == username.strip()
password_no_whitespace = password == password.strip()

