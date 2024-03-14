def localize_triangles(local_triangles, local_vertices, global_vertices) -> np.ndarray:
    """Helper function that converts global indices of triangles to local ones from selected mesh

    Args:
        local_triangles (np.ndarray): triangles acquired from selection
        local_vertices (np.ndarray): vertices acquired from selection
        global_vertices (np.ndarray): vertices of the whole part

    Raises:
        RuntimeError: raised when there are point duplicates in global vertices

    Returns:
        np.ndarray: array of new reindexed triangles
    """
    new_triangles = np.zeros_like(local_triangles)
    used_vertices = np.zeros(len(global_vertices), dtype=bool)
    used_vertices[local_triangles[:, 0]] = True
    used_vertices[local_triangles[:, 1]] = True
    used_vertices[local_triangles[:, 2]] = True
    idx = np.where(used_vertices)[0]
    remap = np.ndarray(len(global_vertices), dtype=np.int32)
    remap[idx] = np.arange(0, len(idx))
    new_triangles[:, 0] = remap[local_triangles[:, 0]]
    new_triangles[:, 1] = remap[local_triangles[:, 1]]
    new_triangles[:, 2] = remap[local_triangles[:, 2]]
    return new_triangles