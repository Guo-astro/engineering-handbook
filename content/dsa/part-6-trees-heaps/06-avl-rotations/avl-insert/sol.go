// LC: none — chapter mechanic (AVL insert with rebalance)
package main

type Node struct {
	Key    int
	Left   *Node
	Right  *Node
	Height int
}

func Height(n *Node) int {
	if n == nil {
		return 0
	}
	return n.Height
}

func BalanceFactor(n *Node) int {
	return Height(n.Left) - Height(n.Right)
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func updateHeight(n *Node) {
	n.Height = 1 + maxInt(Height(n.Left), Height(n.Right))
}

func rotateRight(y *Node) *Node { // fixes LL
	x := y.Left
	t2 := x.Right
	x.Right = y
	y.Left = t2
	updateHeight(y)
	updateHeight(x)
	return x
}

func rotateLeft(x *Node) *Node { // fixes RR
	y := x.Right
	t2 := y.Left
	y.Left = x
	x.Right = t2
	updateHeight(x)
	updateHeight(y)
	return y
}

func Insert(root *Node, key int) *Node {
	if root == nil {
		return &Node{Key: key, Height: 1}
	}
	switch {
	case key < root.Key:
		root.Left = Insert(root.Left, key)
	case key > root.Key:
		root.Right = Insert(root.Right, key)
	default:
		return root
	}
	updateHeight(root)
	bf := BalanceFactor(root)

	if bf > 1 && root.Left != nil && key < root.Left.Key { // LL
		return rotateRight(root)
	}
	if bf < -1 && root.Right != nil && key > root.Right.Key { // RR
		return rotateLeft(root)
	}
	if bf > 1 && root.Left != nil && key > root.Left.Key { // LR
		root.Left = rotateLeft(root.Left)
		return rotateRight(root)
	}
	if bf < -1 && root.Right != nil && key < root.Right.Key { // RL
		root.Right = rotateRight(root.Right)
		return rotateLeft(root)
	}
	return root
}
