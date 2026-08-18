# Scrappy · Knowledge Graph interactivo

Grafo interactivo del **knowledge graph** del código fuente de
[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify), mapeado
100% local (tree-sitter AST, 0 tokens de LLM).

## 🌐 Landing interactiva

👉 **[Abrir el grafo interactivo →](https://scrappy.vercel.app)**

Haz clic en los nodos, filtra y navega las comunidades (force-directed graph).

## 📊 El grafo

| Métrica | Valor |
|---|---|
| Nodos | **2.304** |
| Aristas | **5.435** |
| Comunidades | **99** |
| Conexiones EXTRACTED | **93%** |
| Costo LLM | **0 tokens** |

## 🚀 Cómo se hizo

```bash
uv tool install graphifyy
graphify install             # registrar skill en el asistente
graphify . --code-only       # grafo local, sin LLM
graphify cluster-only .      # + GRAPH_REPORT.md y graph.html navegable
```

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
