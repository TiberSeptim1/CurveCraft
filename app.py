import numpy as np
import plotly.graph_objects as go
import streamlit as st

st.title('Curve Tracing')

def plot_rose(sc, n):
    theta = np.linspace(0, 2*np.pi, 360)
    if sc =="cos":
        sc = np.cos
    else:
        sc = np.sin
    r = sc(n*theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines',name='Rose Curve'))

    fig.add_shape(type='line',
              x0=min(x), x1=max(x),
              y0=0, y1=0,
              line=dict(color='lightgrey', width=2))


    fig.add_shape(type='line',
              x0=0, x1=0,
              y0=min(y), y1=max(y),
              line=dict(color='white', width=2))
    r1=1
    for angle in np.arange(0, np.pi*2, (np.pi/2)/n):
        fig.add_shape(type='line',
                    x0=0, y0=0,
                    x1=r1*np.cos(angle),
                    y1=r1*np.sin(angle),
                    line=dict(color='white',width=1 )
                        )
    
    fig.update_layout( template="seaborn", title='Rose Curve', xaxis=dict(scaleanchor='y'))
    return fig
col1, col2 = st.columns(2)
with col1:
    sc = st.selectbox("cos or sin",["cos","sin"])
with col2:
    n = st.number_input("n=", step=1, value=2)
 

st.latex(r"r = {} \,{} ({} \theta)".format("a",sc,n))

fig = plot_rose(sc, n)
st.plotly_chart(fig)

st.caption("Made by TiberSeptim1")