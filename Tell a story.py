import random
When = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 30th Sep']
Who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
Name = ['Ali', 'Mariam','Dip', 'Hasan', 'Shuvo']
Place = ['Spain','Antarctica', 'Germany', 'Venice', 'Mars']
Went = ['cinema hall', 'university','seminar', 'school', 'coffee shop']
Situation = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(random.choice(When) + ', ' + random.choice(Who) + ' that lived in ' + random.choice(Place) + ', went to the ' + random.choice(Went) + ' and ' + random.choice(Situation) + ' -This story is writen by: ' + random.choice(Name))