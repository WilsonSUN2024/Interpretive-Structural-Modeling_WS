# ISM (Interpretive Structural Modeling) Implementation


import pandas as pd
import numpy as np


def load_relationship_matrix(file_path: str, sheet_name: str = "Sheet1") -> np.ndarray:
    """
    Load the relationship matrix from an Excel file.

    Parameters
    ----------
    file_path : str
        Path to the Excel file.
    sheet_name : str
        Name of the worksheet to load.

    Returns
    -------
    np.ndarray
        The relationship matrix as a NumPy array.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    return df.values


def compute_reachability_matrix(base_matrix: np.ndarray) -> np.ndarray:
    """
    Compute the reachability matrix using transitive closure (Warshall algorithm).

    Parameters
    ----------
    base_matrix : np.ndarray
        The initial adjacency/relationship matrix.

    Returns
    -------
    np.ndarray
        The final reachability matrix.
    """
    n = base_matrix.shape[0]
    reachability = base_matrix.copy()

    # Add identity matrix (self-reachability)
    reachability = np.where(reachability == 1, 1, 0)
    np.fill_diagonal(reachability, 1)

    # Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reachability[i, j] = reachability[i, j] or (reachability[i, k] and reachability[k, j])

    return reachability.astype(int)


def level_partitioning(reachability_matrix: np.ndarray) -> list:
    """
    Perform level partitioning to determine hierarchical structure levels.

    Parameters
    ----------
    reachability_matrix : np.ndarray
        The reachability matrix of the system.

    Returns
    -------
    list
        A list of levels, each containing the indices of nodes in that level.
    """
    n = reachability_matrix.shape[0]
    remaining_nodes = set(range(n))
    levels = []

    while remaining_nodes:
        current_level = []
        for node in list(remaining_nodes):
            reachable_set = {j for j in range(n) if reachability_matrix[node, j] == 1}
            antecedent_set = {i for i in range(n) if reachability_matrix[i, node] == 1}
            intersection_set = reachable_set.intersection(antecedent_set)

            # Condition for level partitioning: intersection equals reachable set
            if intersection_set == reachable_set:
                current_level.append(node)

        if not current_level:
            raise RuntimeError("Level partitioning failed: no nodes found at this stage.")

        levels.append(current_level)
        remaining_nodes -= set(current_level)

    return levels


def export_results(reachability_matrix: np.ndarray, levels: list,
                   reachability_path: str, level_path: str) -> None:
    """
    Export the computed results to CSV files.

    Parameters
    ----------
    reachability_matrix : np.ndarray
        The reachability matrix.
    levels : list
        The hierarchical structure levels.
    reachability_path : str
        Path to save the reachability matrix CSV.
    level_path : str
        Path to save the level list CSV.
    """
    pd.DataFrame(reachability_matrix).to_csv(reachability_path, index=False, encoding='utf_8_sig')

    level_df = pd.DataFrame({"Level": list(range(1, len(levels) + 1)),
                             "Nodes": [", ".join(str(x + 1) for x in lvl) for lvl in levels]})
    level_df.to_csv(level_path, index=False, encoding='utf_8_sig')


if __name__ == "__main__":
    print("=== ISM Model Computation ===")
    file_path = input("Enter the Excel file path: ").strip()

    try:
        base_matrix = load_relationship_matrix(file_path)
        print("Matrix loaded successfully.")

        reachability_matrix = compute_reachability_matrix(base_matrix)
        print("Reachability matrix computed.")

        levels = level_partitioning(reachability_matrix)
        print(f"Level partitioning completed. Total levels: {len(levels)}")

        export_results(reachability_matrix, levels,
                       "reachability_matrix.csv", "structure_levels.csv")

        print("Results exported to 'reachability_matrix.csv' and 'structure_levels.csv'")

    except Exception as e:
        print(f"Error: {e}")
