def localize_triangles(triangles:np.ndarray, global_vertices:np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """This function resets the triangles' indices to be relative to the selection on mesh

    Args:
        triangles (np.ndarray): array of triangles from 'np.array(mesh.selection.triangles)[stage]' 
        global_vertices (np.ndarray): all vertices of the mesh 'np.array(mesh.data.coordinate)[stage]'

    Returns:
        tuple[np.ndarray, np.ndarray]: localized triangles' array and indices, for remapping of global vertices, values, etc.

    Usage:
        >>> global_vertices = np.array(mesh.data.coordinate)
        >>> triangles = np.array(mesh.selection.triangle)
        >>> number_of_stages = len(global_vertices)
        >>> for stage in range(number_of_stages):
        ...     localized_triangles, indices = localize_triangles(triangles[stage], global_vertices[stage])
        ...     localized_vertices = global_vertices[stage][indices]
    """
    indices = np.nonzero(np.bincount(triangles.ravel(), minlength=len(global_vertices)))[0]
    remap = np.ndarray(len(global_vertices), dtype=np.int32)
    remap[indices] = np.arange(0, len(indices))
    triangles = remap[triangles.ravel()].reshape(triangles.shape)
    return triangles, indices
