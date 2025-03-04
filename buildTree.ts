class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

export function buildTree(values: (number | null)[]): TreeNode | null {
    if (values.length === 0 || values[0] === null) return null;

    // Создаем корень дерева
    const root = new TreeNode(values[0]);
    const queue: (TreeNode | null)[] = [root];
    let index = 1;

    // Обрабатываем значения
    while (index < values.length) {
        const current = queue.shift();
        if (current) {
            // Левый узел
            if (values[index] !== null) {
                current.left = new TreeNode(values[index]!);
                queue.push(current.left);
            }
            index++;

            // Правый узел
            if (index < values.length && values[index] !== null) {
                current.right = new TreeNode(values[index]!);
                queue.push(current.right);
            }
            index++;
        }
    }

    return root;
}

export { }