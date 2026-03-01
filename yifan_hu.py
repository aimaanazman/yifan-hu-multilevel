import numpy as np
from quadtree import QuadTree

def random_layout(G):
    return {v: np.random.rand(2) for v in G.nodes()}

def cool(iteration, max_iter):
    return 1.0 - (iteration / max_iter)

def calculate_spring_attraction(G, pos, K):
    forces = {v: np.zeros(2) for v in G.nodes()}
    for u, v in G.edges():
        delta = pos[u] - pos[v]
        dist = np.linalg.norm(delta) + 1e-9
        force = (dist**2 / K) * (delta / dist)
        forces[u] -= force
        forces[v] += force
    return forces

def refine_step(G, pos, theta, K, iteration, max_iter):
    tree = QuadTree(pos)
    alpha = cool(iteration, max_iter)
    new_pos = {}

    spring_forces = calculate_spring_attraction(G, pos, K)

    for v in G.nodes():
        rep_force = tree.barnes_hut_force(v, pos[v], theta, K)
        total_force = rep_force + spring_forces[v]
        norm = np.linalg.norm(total_force) + 1e-9
        displacement = alpha * (total_force / norm)
        new_pos[v] = pos[v] + displacement

    return new_pos

def yifan_hu_layout(G, levels=3, theta=0.8, K=1.0, max_iter=50):
    G_coarse = [G]

    # --- Coarsening Phase (simplified placeholder) ---
    for i in range(1, levels):
        G_coarse.append(G_coarse[-1])  # Replace with real coarsening

    pos = random_layout(G_coarse[-1])

    for t in range(max_iter):
        pos = refine_step(G_coarse[-1], pos, theta, K, t, max_iter)

    return pos
