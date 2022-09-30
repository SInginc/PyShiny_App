from shiny import ui

app_ui = ui.page_navbar(
    ui.nav(
        title="General"
    ),
    ui.nav(
        title="Read SDTMs"    
    ),
    ui.nav(
        title="Datasets"
    ),
    title="Example App",
    window_title="Test"
)