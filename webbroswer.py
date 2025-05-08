import webbrowser as wb
import sys

urls = ['https://www.reddit.com/search/?q=',
        'www.google.co.nz/search?q=',
        'https://www.youtube.com/results?search_query=']

# Allowing the system to take input for the python script
def question():
    if len(sys.argv) > 1:
        # Allowing the first parameter to search in other places.
        query = sys.argv[2:]
        return ' '.join(query)
    else:
        print("There is an error")

def otherSearch():
    if (sys.argv[1] == "-r"):
        query = urls[0]+question()
        wb.get('chromium-browser').open_new_tab(query)

    elif (sys.argv[1] == "-g"):
        query = urls[1]+question()
        wb.get('chromium-browser').open_new_tab(query)
    
    elif (sys.argv[1] == "-y"):
        query = urls[2]+question()
        wb.get('chromium-browser').open_new_tab(query)
    
    else:
        print('Err')

otherSearch()

