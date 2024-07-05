from streamlit_card import card
import pandas as pd
import base64

df = pd.read_csv('conectemos_preguntas.csv')
pregunta = df['Preguntas'].sample(1).values[0]

filepath = "conectm.png"
with open(filepath, "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")

hasClicked = card(
  title=pregunta,
  text='',
  image=data,
  styles={
        "card": {
            "width": "300%",
            "height": "450px",
            "border-radius": "30px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
        },
        "text": {
            "font-family": "serif",
        }
    }
)
