from taipy import Gui
import pandas as pd
data = {
    "Date": pd.date_range("2023-1-1", periods=4, freq="D"),
    "Min": [-222,-19.7,265.7,666.5],
    "Max": [-877.6,-82.2,120.7,913.5]
}


title = "Stock Simulator By Pranav"
title2 = "Simulation"
path = "logoo.png"
company_name = "Tata"
company_minp = 300
company_maxp = 1000

def press(state):
    print("hey hello pranav")
    print(state.path)
    print(state.company_minp)

    with open("data.txt" , "w") as f:
        f.write(f"{state.company_name},{state.company_minp},{state.company_maxp}")

page = """
<|text-center|
<|{path}|image|>

<|{title}|hover_text = Welcome to Stock Screener|>

Name of Stock: <|{company_name}|input|>

Min Price: <|{company_minp}|input|>
Max Price: <|{company_maxp}|input|>

<|Run Simulation|button|on_action=press|>

<|{title2}|hover_text = Your Simulation|> 

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|line[1]=dash|color[2]=blue|>


>
"""
if __name__ == "__main__":
    app = Gui(page)
    app.run(use_reloader=True)