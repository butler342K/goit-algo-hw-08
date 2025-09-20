import avl_tree
from cables_heap import min_cost_cables

if __name__ == "__main__":
    # AVL Tree operations are demonstrated in avl-tree.py
    # Cable connection cost minimization is demonstrated in cables_heap.py

    root = None
    keys = [10, 20, 30, 25, 28, 27, -1, 5, 6,-3]

    for key in keys:
        root = avl_tree.insert(root, key)

    print("AVL-Дерево:")
    print(root)

    print("\nTask 1")

    min_value = avl_tree.min_value_node(root)
    print("Мінімальне значення в дереві:", min_value.key)

    print("\nTask 2")
    sum_values = sum(node.key for node in avl_tree.inorder_traversal(root))
    print("Сума всіх значень в дереві:", sum_values)

    print("\nTask 3. Мінімізація витрат на з’єднання кабелів")
    # Набір кабелів. Довжини
    cables = [4, 3, 2, 6, 8, 1, 12]
    cost, steps = min_cost_cables(cables)
    print("Мінімальні витрати:", cost)
    print("Порядок з’єднань:")
    for a, b, c in steps:
        print(f"Вибрані: {a} і {b} → новий кабель = {c}")