#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
def is_two(x):
    return x == 2 or x == '2'


# In[ ]:


is_two(2)


# In[ ]:


#2
def is_vowel(char):
    return len(string) == 1 and string.lower() in 'aeiou'


# In[ ]:


#3
def is_consonant(string):
    return len(string) == 1 and not is_vowel(string) and string.isalpha()


# In[ ]:


is_consonant('t')


# In[ ]:


#4

def capitalize_starting_consonant(string):
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string


# In[ ]:





# In[ ]:


capitalize_starting_consonant('tree')


# In[ ]:


#5
def calculate_tip(tip_percentage, bill):
    amount_to_tip = bill * tip_percentage
    return amount_to_tip


# In[ ]:


#6
def apply_discount(price, discount):
    ds = price*(discount/100)
    sp = price-ds
    sp = round(sp, 2)
    return sp

ori_price = int(input("Enter Original Price : "))
dis_per = int(input("Enter Discount Percentage : "))
print(dis(ori_price, dis_per))


# In[ ]:


#7

handle_commas = "1,000,000"
final_string=handle_commas.replace(',',"")
print(final_string


# In[3]:


#8 

def get_letter_grade(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return "Input must be a number"


# In[ ]:


#9

def remove_vowels(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)
    
string = "This is Great"
remove_vowels(string)


# In[ ]:


#10

def remove_special_char(string):
    return ''.join([c for c in string if c.isalnum() or c == ' '])


# In[ ]:


remove_special_char('name % 2')


# In[ ]:


def normalize_name(string):
    special_char_removed = remove_special_char(string)
    return special_char_removed.lower().strip().replace(' ', '_')


# In[ ]:


normalize_name('Lindy castellaw')


# In[ ]:


#11

cumulative_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
output = []
s = 0

for i in cumulative_sum:
    s+= i
    output.append(s)
print(cl)


# In[ ]:



#bonus

def twelveto24(string):

      if string[-2:] == "AM" and string[:2] == "12":
         return "00" + string[2:-2]

      elif string[-2:] == "AM":
         return string[:-2]

      elif string[-2:] == "PM" and string[:2] == "12":
         return string[:-2]
        
      else:
          return str(int(string[:2]) + 12) + string[2:8]


time="03:25PM"
print("12-hour Format time:: ", time)
print("24-hour Format time ::",twelveto24(time))

