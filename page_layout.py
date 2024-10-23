from dash import html, dcc, callback, register_page, Output, Input, State

register_page(__name__, path_template='/page/<selected_id>', title='ID page')

# Function to dynamically generate page layout based on selected ID
def layout(selected_id='id1', **kwargs):
    return html.Div(
        [
            html.H3(f"Page for {selected_id}"),
            dcc.Dropdown(
                id="asset-dropdown",
                options=[{"label": f"Asset {j}", "value": f"asset{j}"} for j in range(1, 4)],
                value="asset1",
                clearable=False,
                style={'width': '200px', 'marginBottom': '20px'}
            ),
            html.Div(id="display-data"),
        ],
        style={'padding': '20px'}
    )

# Callback to dynamically display data based on selected asset
@callback(
    Output("display-data", "children"),
    Input("asset-dropdown", "value"),
    State('id_dropdown', 'value')
)
def update_data(selected_asset, selected_id):
    return f"Selected ID: {selected_id}, Selected Asset: {selected_asset}"
