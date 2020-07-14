import plotly
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

def vector_trace(vector, name = '', text = ''):
    x_coord = vector[0] 
    if len(vector) is 1:
        trace = {'x': [0, x_coord], 'y': [0, 0], 'mode': 'lines+markers', 'name': name, 'text': text}
        layout = {'xaxis': {'range': [0, 4]}, 'yaxis': dict(range=[-.5, .5],
        showgrid=False,
        zeroline=True,
        showline=False,
        ticks='',
        showticklabels=False)}
        return plot([trace], layout)
    else:
        y_coord = vector[1]
        return {'x': [0, x_coord], 'y': [0, y_coord], 'mode': 'lines+markers', 'name': name, 'text': text}
    
def plus_trace(first_array, second_array, name = ''):
    added = first_array + second_array
    first_added = added[0]
    second_added = added[1]
    second_vector_x = [first_array[0], first_added]
    second_vector_y = [first_array[1], second_added]
    return trace_values(second_vector_x, second_vector_y, mode = 'lines+markers', name = name)

def plot(traces, layout = {}):
    if not isinstance(traces, list): raise TypeError('first argument must be a list.  Instead is', traces)
    plotly.offline.iplot({'data': traces, 'layout': layout})

def build_layout(x_range = None, y_range = None, options = {}):
    layout = {}
    if isinstance(x_range, list): layout.update({'xaxis': {'range': x_range}})
    if isinstance(y_range, list): layout.update({'yaxis': {'range': y_range}})
    layout.update(options)
    return layout


def trace_values(x_values, y_values, mode = 'markers', name="data", text = []):
    return {'x': x_values, 'y': y_values, 'mode': mode, 'name': name, 'text': text}


def trace(data, mode = 'markers', name="data"):
    x_values = list(map(lambda point: point['x'],data))
    y_values = list(map(lambda point: point['y'],data))
    return {'x': x_values, 'y': y_values, 'mode': mode, 'name': name}

def plot(traces, layout = {}):
    if not isinstance(traces, list): raise TypeError('first argument must be a list.  Instead is', traces)
    plotly.offline.iplot({'data': traces, 'layout': layout})

def build_layout(x_range = None, y_range = None, options = {}):
    layout = {}
    if isinstance(x_range, list): layout.update({'xaxis': {'range': x_range}})
    if isinstance(y_range, list): layout.update({'yaxis': {'range': y_range}})
    layout.update(options)
    return layout

def unit_vector(a):
    return a/norm(a)

def cos_a_b(a, b):
    return unit_vector(a).dot(unit_vector(b))

def vector_projection_trace(a, b):
    projection_vec = unit_vector(b)*cos_a_b(a,b)*norm(a)
    vector_projection_trace = vector_trace(projection_vec, name = 'c')
    return vector_projection_trace