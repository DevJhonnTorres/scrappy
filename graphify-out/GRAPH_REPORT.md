# Graph Report - graphify-demo  (2026-08-18)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 35 nodes · 61 edges · 5 communities (2 shown, 3 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Api
- OrderService
- Product
- Inventory
- orders.py

## God Nodes (most connected - your core abstractions)
1. `Product` - 11 edges
2. `Api` - 9 edges
3. `OrderService` - 9 edges
4. `Inventory` - 9 edges
5. `User` - 8 edges
6. `Order` - 8 edges
7. `OrderItem` - 4 edges
8. `Coordinates inventory reservation and order fulfilment.` - 1 edges
9. `API layer that exposes the order domain over HTTP-style handlers.` - 1 edges
10. `A small REST API to demo Graphify's knowledge graph: orders, users and…` - 1 edges

## Surprising Connections (you probably didn't know these)
- `Api` --uses--> `Inventory`  [INFERRED]
  demo_app/src/api.py → demo_app/src/orders.py
- `Api` --uses--> `OrderService`  [INFERRED]
  demo_app/src/api.py → demo_app/src/orders.py
- `Api` --uses--> `Product`  [INFERRED]
  demo_app/src/api.py → demo_app/src/orders.py
- `Api` --uses--> `User`  [INFERRED]
  demo_app/src/api.py → demo_app/src/orders.py

## Import Cycles
- None detected.

## Communities (5 total, 3 thin omitted)

### Community 0 - "Api"
Cohesion: 0.33
Nodes (3): Any, Api, User

### Community 1 - "OrderService"
Cohesion: 0.29
Nodes (3): Order, OrderService, Coordinates inventory reservation and order fulfilment.

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Product` connect `Product` to `Api`, `OrderService`, `Inventory`, `orders.py`?**
  _High betweenness centrality (0.295) - this node is a cross-community bridge._
- **Why does `Api` connect `Api` to `OrderService`, `Product`, `Inventory`, `orders.py`?**
  _High betweenness centrality (0.197) - this node is a cross-community bridge._
- **Why does `OrderService` connect `OrderService` to `Api`, `Inventory`, `orders.py`?**
  _High betweenness centrality (0.181) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Api` (e.g. with `Inventory` and `OrderService`) actually correct?**
  _`Api` has 4 INFERRED edges - model-reasoned connections that need verification._