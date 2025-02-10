import seaborn as sns
from faicons import icon_svg
import plotly.express as px

# Import data from shared.py
from shared import app_dir, df, weights

from shiny import App, reactive, render, ui

# Define UI elements of app
app_ui = ui.page_sidebar(
# toggle Sullivan, Haruki, or Both
    ui.sidebar(
        # delete slider input
        ui.input_checkbox_group(
# change "species" to better label, remmber to change in server
            "cat",
            "Choose cat",
            ["Haruki", "Sullivan"],
            selected=["Haruki", "Sullivan"],
        ),
        title="Cat selector controls",
    ),
    ui.layout_column_wrap(
        ui.value_box(
            "Sullivan's current age",
            ui.output_text("sullivan_age"),
            showcase=icon_svg("cat"),
        ),
        ui.value_box(
            "Haruki's current age",
            ui.output_text("haruki_age"),
            showcase=icon_svg("cat"),
        ),
        ui.value_box(
            "Average growth rate",
            ui.output_text("growth_rate"),
            showcase=icon_svg("percent"),
        ),
        fill=False,
    ),
    ui.layout_columns(
        ui.card(
            ui.card_header("Sullivan and Haruki's weight change"),
            ui.output_plot("weight_plot"),
            full_screen=True,
        ),
        ui.card(
            ui.card_header("Raw measurements"),
            ui.output_data_frame("summary_statistics"),
            full_screen=True,
        ),
    ),
    ui.include_css(app_dir / "styles.css"),
    title="Cat weight dashboard",
    fillable=True,
)


def server(input, output, session):
    @reactive.calc
    def filtered_df():
        filt_df = weights[weights["cat"].isin(input.cat())]
        return filt_df

    @render.text
    def sullivan_age():
        return filtered_df().shape[0]

    @render.text
    def haruki_age():
        return f"{filtered_df()['weight']} lbs"

    @render.text
    def growth_rate():
        return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

    @render.plot
    def weight_plot():
        return px.scatter(
            data=filtered_df(),
            x="date",
            y="weight",
            hue="cat",
        )

    @render.data_frame
    def summary_statistics():
        cols = [
            "cat",
            "date",
            "weight",
        ]
        return render.DataGrid(filtered_df()[cols], filters=True)


app = App(app_ui, server)
