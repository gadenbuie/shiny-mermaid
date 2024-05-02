import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

let config = { 
  startOnLoad: true,
  flowchart: { 
    useMaxWidth: false,
    htmlLabels: true 
  } 
};

mermaid.initialize(config);

class MermaidOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-mermaid-output");
  }

  async renderValue(el, payload) {
    const { svg } = await mermaid.render(el.id + "_svg", payload.diagram)
    el.innerHTML = svg;
  }
}

Shiny.outputBindings.register(
  new MermaidOutputBinding(),
  "shiny-mermaid-output"
)
