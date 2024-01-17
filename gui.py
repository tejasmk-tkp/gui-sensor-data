from nicegui import ui

def gui_view(sensor, sensor_values, step_values):
    with ui.card().tight():
        fig = go.Figure(go.Scatter(x=[step], y=[value]))
        fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
        ui.plotly(fig).classes('w-100 h-100')
        with ui.card_section():
            ui.label(f'{sensor}: {value}')

def update_gui(sensor, value):
    step = 0
    while True:
        sensor_values.append(value)
        step_values.append(step)

        gui_view(sensor, sensor_values, step_values)

        step += 1

        time.sleep(0.02)

