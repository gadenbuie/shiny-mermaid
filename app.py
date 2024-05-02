from shiny import App, ui
from mermaid_module import mermaid_diagram_ui, mermaid_diagram_server


app_ui = ui.page_navbar(  
    ui.nav_panel("A", mermaid_diagram_ui("diagramA")),  
    ui.nav_panel("B", mermaid_diagram_ui("diagramB")),  
    ui.nav_panel("C", mermaid_diagram_ui("diagramC")),  
    title="Mermaid Test App",  
    id="page",  
)  


def server(input, output, session):
    diagramA = """
    flowchart LR
        id1[This is Diagram A]
    """

    diagramB = """
    flowchart LR
        id1[This is Diagram B]
    """

    diagramC = """
    flowchart LR
        id1[This is Diagram C]
    """


    mermaid_diagram_server("diagramA", diagramA)

    mermaid_diagram_server("diagramB", diagramB)

    mermaid_diagram_server("diagramC", diagramC)


app = App(app_ui, server)
