import webbrowser as wb
import sys

urls = ['https://www.reddit.com/search/?q=',
        'www.google.co.nz/search?q=',
        'https://www.youtube.com/results?search_query=']

# TODO: to see if it is possible to change broswer - Currently getting an error
# browsers = ['firefox','chrome','chromium','safari','opera']

def question():

    if len(sys.argv) > 1:
        # Allowing the first parameter to search in other places.
        query = sys.argv[2:]
        return ' '.join(query)
    else:
        print("Please provide a logger query")

def otherSearch():
    if (sys.argv[1] == "-r"):
        # change the link after site:
        limitsearch = " site:stackoverflow.com OR site:reddit.com"
        query = urls[0]+question() + limitsearch
        wb.get('chromium').open_new_tab(query)

    elif (sys.argv[1] == "-g"):
        query = urls[1]+question()
        wb.get('chromium').open_new_tab(query) 
    
    elif (sys.argv[1] == "-y"):
        query = urls[2]+question()
        wb.get('chromium').open_new_tab(query)    

    else:
        print('Err')
otherSearch()

