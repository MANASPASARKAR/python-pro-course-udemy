import justpy as jp

def home():
    wp = jp.WebPage() # new webpage
    jp.Div(a=wp, text="Hello world!") # create div, add to webpage, and add text
    jp.Div(a=wp, text="Hello again")
    return wp

jp.Route("/", home) # route and the function/class for that route to render page
jp.justpy()