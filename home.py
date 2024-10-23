from dash import html, register_page

register_page(__name__, path='/', title='Home')

# Home page layout
def layout(**kwargs):
    return [
        html.H2("Welcome to the Home Page"),
        html.P("Select an ID from the dropdown and click 'Go' to view the data.")
    ]


