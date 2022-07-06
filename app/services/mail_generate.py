import plotly.express as px


def return_graph():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[
        df["pop"] < 2.0e6, "country"
    ] = "Other countries"  # Represent only large countries
    fig = px.pie(
        df, values="pop", names="country", title="Population of European continent"
    )

    fig.write_image("fig1.png")
