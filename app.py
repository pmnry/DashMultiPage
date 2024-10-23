from dash import Dash, html, dcc, Input, Output, State, no_update, page_container

# Initialize the Dash app
app = Dash(__name__, use_pages=True, routing_callback_inputs={'id_dropdown': Input('id_dropdown', 'value')})

# Main layout with a banner, dropdown, button, and page container
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=True),  # For handling URLs
        html.Div(
            [
                dcc.Dropdown(
                    id="id_dropdown",
                    options=[{"label": f"ID {i}", "value": f"id{i}"} for i in range(1, 4)],
                    value="id1",
                    clearable=False,
                    style={'width': '200px', 'display': 'inline-block', 'margin-right': '20px'}
                ),
                html.Button("Go", id="go-button", n_clicks=0, style={'display': 'inline-block'}),
            ],
            style={'marginBottom': '20px', 'marginTop': '20px'}
        ),
        page_container  # This will load dynamic content
    ],
    style={'padding': '20px'}
)

# Callback for redirecting based on dropdown value
@app.callback(
    Output('url', 'pathname'),
    Input('go-button', 'n_clicks'),
    State('id_dropdown', 'value'),
    prevent_initial_call=True
)
def update_url(n_clicks, selected_id):
    if n_clicks > 0:
        return f"/page/{selected_id}"
    else:
        return f"/"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8070)
