from nicegui import ui
import plotly.graph_objects as go
from random import random

ui.label('Sensor Data')
ui.dark_mode().enable()

value = [random(), random(), random(), random(), random(), random()]

with ui.splitter() as splitter:
    with splitter.before:
        with ui.card().tight():
            fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4]))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
            ui.plotly(fig).classes('w-100 h-100')
            with ui.card_section():
                ui.label(f'MQ136: {value[0]}')
            '''def add_trace():
            fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[random(), random(), random(), random()]))
            plot.update()'''
    with splitter.after:
        with ui.card().tight():
            fig = go.Figure(go.Scatter(x = [1, 2, 3, 4], y = [1, 2, 3, 2.5]))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
            ui.plotly(fig).classes('w-100 h-100')
            with ui.card_section():
                ui.label(f'MQ2: {value[1]}')
    with splitter.separator:
        ui.icon('line').classes('w-100')

with ui.splitter() as splitter:
    with splitter.before:
        with ui.card().tight():
            fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4]))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
            ui.plotly(fig).classes('w-100 h-100')
            with ui.card_section():
                ui.label(f'DHT11 (temperature): {value[2]}')
            '''def add_trace():
            fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[random(), random(), random(), random()]))
            plot.update()'''
    with splitter.after:
        with ui.card().tight():
            fig = go.Figure(go.Scatter(x = [1, 2, 3, 4], y = [1, 2, 3, 2.5]))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
            ui.plotly(fig).classes('w-100 h-100')
            with ui.card_section():
                ui.label(f'DHT11 (humidity): {value[3]}')
    with splitter.separator:
        ui.icon('line').classes('w-100')

with ui.splitter() as splitter:
    with splitter.before:
        with ui.card().tight():
            fig = go.Figure(go.Scatter(x=[1, 2, 3, 4], y=[1, 2, 3, 4]))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
            ui.plotly(fig).classes('w-100 h-100')
            with ui.card_section():
                ui.label(f'MQ137: {value[4]}')
            '''def add_trace():
            fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[random(), random(), random(), random()]))
            plot.update()'''
    with splitter.after:
        with ui.card().tight():
            fig = go.Figure(go.Scatter(x = [1, 2, 3, 4], y = [1, 2, 3, 2.5]))
            fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
            ui.plotly(fig).classes('w-100 h-100')
            with ui.card_section():
                ui.label(f'MQ7: {value[5]}')
    with splitter.separator:
        ui.icon('line').classes('w-100')

ui.run()
