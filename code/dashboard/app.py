# shiny app to display my cats' growth over time
# v0.0.1 - Andrew Richard
# project start: January 31, 2025
# to run, make sure venv is active with necessary libraries
# in terminal, run shiny run app.py when in directory 

# import libraries and functions
import seaborn as sns
import matplotlib.pyplot as plt
from faicons import icon_svg
import pandas as pd
from datetime import datetime as dt
from funcs import haruki_age, sullivan_age, age_in_weeks
from shared import app_dir, weights 
from shiny import App, reactive, render, ui

weights = age_in_weeks(weights)

# Define UI elements of app
app_ui = ui.page_sidebar(
    # toggle Sullivan, Haruki, or Both
    ui.sidebar(
        ui.input_checkbox_group(
            "cat",
            "Choose cat",
            ["haruki", "sullivan"],
            selected=["haruki", "sullivan"],
        ),
        ui.input_radio_buttons(
            "plot_toggle",
            "Toggle weight by age",
            choices = ["date", "weeks"],
            selected="date",
        ),
        ui.value_box(
            "Sullivan's current age",
                ui.tags.span(ui.output_text("sullivan_age_widget"), style="font-size: 11px"), 
            showcase=icon_svg("cat"),
        ),
        ui.value_box(
            "Haruki's current age",
            ui.tags.span(ui.output_text("haruki_age_widget"), style="font-size: 11px"), 
            showcase=icon_svg("cat"),
        ),
        ui.value_box(
            "haruki's growth rate",
            ui.tags.span(ui.output_text("haruki_growth_rate"), style="font-size: 11px"), 
            showcase=icon_svg("percent"),
        ),
        ui.value_box(
            "sullivan's growth rate",
            ui.tags.span(ui.output_text("sullivan_growth_rate"), style="font-size: 11px"), 
            showcase=icon_svg("percent"),
        ),
        title="Cat selector controls",
    ),
    ui.layout_column_wrap(
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
        col_widths=[9,3]
    ),
    ui.include_css(app_dir / "styles.css"),
    title="Cat weight dashboard",
    fillable=True,
)


def server(input, output, session):
    @reactive.calc
    def filtered_df():
        weights["date"] = pd.to_datetime(weights["date"], format="%Y-%m-%d").dt.date
        filt_df = weights[weights["cat"].isin(input.cat())]
        return filt_df

    @render.text
    def sullivan_age_widget():
        today_date_str = dt.today().strftime('%Y-%m-%d')
        age = sullivan_age(today_date_str)
        if "error" in age:
            return age["error"]
        return f"Sullivan's age: {age['years']} years, {age['months']} months, {age['weeks']} weeks, {age['days']} days"

    @render.text
    def haruki_age_widget():
        today_date_str = dt.today().strftime('%Y-%m-%d')
        age = haruki_age(today_date_str)
        if "error" in age:
            return age["error"]
        return f"Haruki's age: {age['years']} years, {age['months']} months, {age['weeks']} weeks, {age['days']} days"

    @render.text
    def haruki_growth_rate():
        haruki_growth_rate = weights[weights['cat'] == 'haruki']['weight'].max() / weights[weights['cat'] == 'haruki']['weeks'].max()
        return f"Haruki's growth rate:\n{round(haruki_growth_rate, 2)} lbs/wk"

    @render.text
    def sullivan_growth_rate():
        sullivan_growth_rate = weights[weights['cat'] == 'sullivan']['weight'].max() / weights[weights['cat'] == 'sullivan']['weeks'].max()
        return f"Sullivan's growth rate:\n{round(sullivan_growth_rate, 2)} lbs/wk"

    @render.plot
    def weight_plot():
        df = filtered_df()
        print(df)
        p = sns.lineplot(
            data=df,
            x=df[str(input.plot_toggle())],
            y="weight",
            hue="cat",
        )
        plt.xticks(rotation=45)
        return p 
    @render.data_frame
    def summary_statistics():
        cols = [
            "cat",
            "date",
            "weight",
        ]
        return render.DataGrid(filtered_df()[cols], filters=True)

app = App(app_ui, server)
