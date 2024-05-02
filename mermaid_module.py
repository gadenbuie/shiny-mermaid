from shiny import module, ui, Inputs, Outputs, Session, render
from shiny.module import resolve_id
from shiny.render.renderer import Jsonifiable, Renderer
from htmltools import HTMLDependency
from htmltools import Tag
from typing import Any

memaid_dep = HTMLDependency(
    "mermaid",
    "10.9.0",
    source={"subdir": "mermaid"},
    script={"src": "mermaidComponent.js", "type": "module"},
    all_files=True,
)


class render_mermaid(Renderer[str]):
    """
    Renders mermaid diagrams
    """

    def auto_output_ui(self) -> Any:
        return ui.output_mermaid

    async def transform(self, value: str) -> Jsonifiable:
        return {
            "diagram": value,
        }

@module.ui
def mermaid_diagram_ui(height="400px") -> Tag:
    """UI component for mermaid diagram"""

    def output_mermaid(id, height):
        return ui.div(
            memaid_dep,
            id=resolve_id(id),
            class_="shiny-mermaid-output",
            style=f"height: {height}",
        )

    return output_mermaid("mermaid_diagram", height=height)


@module.server
def mermaid_diagram_server(
    input: Inputs,
    output: Outputs,
    session: Session,
    diagram_text: str
) -> Any:
    """Server component for mermaid diagram"""

    @render_mermaid
    def mermaid_diagram():
        return diagram_text
