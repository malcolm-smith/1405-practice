possibleMovies = ('John Wick',
                  'The Matrix',
                  'Bill and Ted\'s Excellent Adventure',
                  'Constantine')

print('The actor is Keanu Reeves.\nThe possible movies are: ')
for movie in possibleMovies:
    print('\t-' + movie)
if input('Does his character die during the movie? ').upper()[0] == 'Y':
    if input('Can his character dodge bullets? ').upper()[0] == 'Y':
        print('The Matrix')
    else:
        print('Constantine')
else:
    if input('Does his character go back in time? ').upper()[0] == 'Y':
        print('Bill and Ted\'s Excellent Adventure')
    else:
        print('John Wick')
