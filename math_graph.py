import networkx as nx
import matplotlib.pyplot as plt

# 1. 그래프 객체 생성 (방향성이 있는 DiGraph)
G = nx.DiGraph()

# 2. 노드와 엣지 추가 (선행 개념 -> 후행 개념)
# 예: "Addition"을 알아야 "Multiplication"을 배울 수 있음
edges = [
    ("Numbers", "Addition"),         # 수의 체계 -> 덧셈
    ("Addition", "Subtraction"),    # 덧셈 -> 뺄셈
    ("Addition", "Multiplication"), # 덧셈 -> 곱셈
    ("Multiplication", "Division"), # 곱셈 -> 나눗셈
    ("Subtraction", "Division"),    # 뺄셈 -> 나눗셈
    ("Division", "Fractions"),      # 나눗셈 -> 분수
    ("Fractions", "Decimals"),      # 분수 -> 소수
    ("Multiplication", "Area"),     # 곱셈 -> 넓이 구하기
    ("Fractions", "Ratios")         # 분수 -> 비와 비율
]

G.add_edges_from(edges)

# 3. 시각화 설정
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G, seed=42)  # 노드들이 겹치지 않게 배치하는 알고리즘

# 노드 그리기
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color='lightgreen', alpha=0.9)

# 엣지(화살표) 그리기
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray', arrowstyle='-|>', arrowsize=20)

# 라벨(개념 이름) 적기
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Elementary Math Knowledge Graph", fontsize=15)
plt.axis('off')  # 축 숨기기

# 결과물 저장
plt.tight_layout()
plt.savefig('elementary_math_map.png')
