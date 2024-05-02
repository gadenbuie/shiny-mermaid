from shiny import App, ui
from mermaid_module import mermaid_diagram_ui, mermaid_diagram_server


app_ui = ui.page_fixed(  
    mermaid_diagram_ui("diagramA"),  
    mermaid_diagram_ui("diagramB"),
    mermaid_diagram_ui("diagramC"),
    title="Mermaid Test App"
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
