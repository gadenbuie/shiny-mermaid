import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

let config = { startOnLoad: true, flowchart: { useMaxWidth: false, htmlLabels: true } };
mermaid.initialize(config);

async function drawDiagram(mermaidText) {
  const {svg} = await mermaid.render('mermaidText', mermaidText.diagram);
  return svg
}

class MermaidOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-mermaid-output");
  }

  async renderValue(el, payload) {

    // the payload is mermaid text
    const warhead = payload;
  
    const svg = await drawDiagram(warhead);

    // Why doesn't this work??
    // el.innerHTML = svg;
    setTimeout(() => el.innerHTML = svg, 0)
  }
}

Shiny.outputBindings.register(
  new MermaidOutputBinding(),
  "shiny-mermaid-output"
)
