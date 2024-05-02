import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';

class MermaidOutputBinding extends Shiny.OutputBinding {
  find(scope) {
    return scope.find(".shiny-mermaid-output");
  }

  async renderValue(el, payload) {

    // the payload is mermaid text
    const warhead = payload;

    mermaid.initialize({
      startOnLoad: false,
    })

    const drawDiagram = async function(mermaidText) {
      const {svg} = await mermaid.render('mermaidText', mermaidText.diagram);
      el.innerHTML = svg
    }

    await drawDiagram(warhead);
  }
}

Shiny.outputBindings.register(
  new MermaidOutputBinding(),
  "shiny-mermaid-output"
)
