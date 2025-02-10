# cat_weight_tracker
a way to track the weights of my cats. may eventually be a webapp, for now just jupyter. 

## inputs
takes inputs of date (ISO 8601 standard) and weight (choose units, but currently need specification in plot labels)

## outputs
outputs three plots: one for each cat, and one combined with both cats plotted by the age they were in weeks, not by date.

## some shiny for python tips
To run a Shiny app from the command line, use the shiny run command. This command takes a single argument, the path to the app’s entry point. For example, if your app’s entry point is app.py in the directory ./app_dir, you can run it like this:

`shiny run --reload --launch-browser app_dir/app.py`

This should start your app and also automatically launch a web browser.

The --reload flag means that file changes in the current directory tree will cause the Python process to restart and the browser to reload. Update and save changes to app.py and then wait a moment for the changes to appear in the browser.

ctrl + c will interrupt and close your running app.
