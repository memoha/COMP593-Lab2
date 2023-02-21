def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Megha Mohan',
        'first_name' : 'Megha',
        'student_id' : 10285551,
        'pizza_toppings' : [
            'PEPPERONI',
            'CHEESE',
            'ONION'
        ],
        'movies' : [
            {
                'title' : 'manifest',
                'genre' : 'fiction'
            },
            {
                'title' : 'spider man',
                'genre' : 'fantasy'
            }
        ]
    }

    
    about_me['movies'].append({'title' : 'charming', 'genre' : 'fairy tale'})

    print_student_name_and_id(about_me)

    return
def add_pizza_toppings(about_me, toppings):
    

    return

    # TODO: Step 3 - Add another movie to the data structure
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):   
    about_me_first = about_me['first_name']
    about_me_name = about_me['full_name']
    about_me_id = about_me['student_id']
    print(f'My name is {about_me_name}, but you can call me Ms.{about_me_first}., My student ID is {about_me_id}.')
    for p in about_me['pizza_toppings']:
        print(f'- {p.capitalize()}')


    
   

    
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):

    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'].sort()

    for p in about_me['pizza_toppings']:
        print(f'- {p.capitalize()}')

    return
    
    add_pizza_toppings(about_me, ('bacon', 'cheese', 'pepperoni'))
  

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()