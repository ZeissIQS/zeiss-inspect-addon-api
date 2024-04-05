def localize_triangles(triangles: np.ndarray, global_vertices: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Helper function that converts global indices of triangles to local ones from selected mesh
    Args:
        triangles (np.ndarray): triangles acquired from selection
        global_vertices (np.ndarray): vertices of the whole element
    Returns:
        tuple[np.ndarray, np.ndarray]: array of local triangles, array of corresponding vertices
                                       
    """
    idx = np.nonzero(np.bincount(triangles.ravel(), minlength = len(global_vertices)))[0]
    remap = np.ndarray(len(global_vertices), dtype=np.int32)
    remap[idx] = np.arange(0, len(idx))
    new_triangles = remap[triangles.ravel()].reshape(triangles.shape)
    return new_triangles, global_vertices[idx]