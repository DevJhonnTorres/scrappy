# Graphify · Knowledge Graph interactivo

Demo en vivo del **knowledge graph** de Graphify: el grafo real del repositorio
[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify), mapeado
100% local (tree-sitter AST, 0 tokens de LLM).

## 🌐 Landing interactiva

👉 **[Abrir el grafo interactivo →](https://graphify-demo.vercel.app)**

Haz clic en los nodos, filtra y navega las comunidades (force-directed graph,
igual que el hero del README de Graphify).

## 📊 El grafo

| Métrica | Valor |
|---|---|
| Nodos | **11.057** |
| Aristas | **22.966** |
| Comunidades | **597** |
| Conexiones EXTRACTED | **93%** |
| Costo LLM | **0 tokens** |

## 🚀 Cómo se hizo

```bash
uv tool install graphifyy
cd graphify && git clone https://github.com/Graphify-Labs/graphify .
graphify . --code-only          # grafo local, sin LLM
graphify cluster-only .         # + GRAPH_REPORT.md y graph.html navegable
```

Nota: para `graph.html` de grafos >5.000 nodos se sube el límite con
`GRAPHIFY_VIZ_NODE_LIMIT=20000`.

## 💬 Consultas reales

```bash
graphify explain cli.py
# --> extract() [imports] [EXTRACTED] graphify/cli.py:L3319
# --> dispatch_command() [contains] [EXTRACTED] graphify/cli.py:L805

graphify path build_from_json validate_extraction --undirected
# build_from_json() --calls [EXTRACTED]--> validate_extraction()
```

## 🔗 Referencia

- [Graphify Labs / graphify](https://github.com/Graphify-Labs/graphify)
- Hecho con [Hermes Agent](https://hermes-agent.nousresearch.com)
