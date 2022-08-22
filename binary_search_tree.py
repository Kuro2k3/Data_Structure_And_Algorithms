from platform import node


class Node:
	def __init__(self,value=None):
		self.value = value
		self.left_child = None
		self.right_child = None

class Binary_Search_Tree:
	# Initial
	def __init__(self):
		# Initial root
		self.root = None
	
	# Add value
	def insert(self,value):
		# Check tree == None
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value,self.root)
	
	def _insert(self,value,cur_node):
		if value < cur_node.value:
			if cur_node.left_child == None:
				cur_node.left_child = Node(value)
			else:
				self._insert(value,cur_node.left_child)
		elif value > cur_node.value:
			if cur_node.right_child == None:
				cur_node.right_child = Node(value)
			else:
				self._insert(value,cur_node.right_child)
	
	# Print Tree
	def print_tree(self):
		if self.root != None:
			self._print_tree(self.root)
		else:
			print("Tree is empty!!!")
	
	def _print_tree(self,cur_node):
		if cur_node != None:
			self._print_tree(cur_node.left_child)
			print(str(cur_node.value),end = ' ')
			self._print_tree(cur_node.right_child)

	# find height tree
	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self,cur_node,cur_height):
		if cur_node == None: 
			return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)

	# Find Value from user input
	def find(self,value):
		if self.root != None:
			return self._find(self.root,value)
		else:
			return False
	
	def _find(self,cur_node,value):
		if value == cur_node.value:
			return True
		elif value < cur_node.value and cur_node.left_child != None:
			return self._find(cur_node.left_child,value)
		elif value > cur_node.value and cur_node.right_child != None:
			return self._find(cur_node.right_child,value)
		return False
	
	# Find node 2 children
	def node_2_children(self):
		if self.root != None:
			self._node_two_children(self.root)
		else:
			print("Tree is empty!!!")
	
	def _node_two_children(self,cur_node):
		if cur_node != None:
			if cur_node.left_child != None and cur_node.right_child != None:
				print(cur_node.value,end= ' ')
			self._node_two_children(cur_node.left_child)
			self._node_two_children(cur_node.right_child)

	# Find node one children
	def node_one_children(self):
		if self.root != None:
			self._node_one_children(self.root)
		else:
			print("Tree is empty!!!")

	def _node_one_children(self,cur_node):
		if cur_node != None:
			if (cur_node.left_child != None and cur_node.right_child == None) or (cur_node.left_child == None and cur_node.right_child != None):
				print(cur_node.value,end = ' ')
			self._node_one_children(cur_node.left_child)
			self._node_one_children(cur_node.right_child)
	
	# Find node leaf
	def node_leaf(self):
		if self.root != None:
			self._node_leaf(self.root)
		else:
			print("Tree is empty!!!")
	
	def _node_leaf(self,cur_node):
		if cur_node != None:
			if (cur_node.left_child == None and cur_node.right_child == None):
				print(cur_node.value,end = ' ')
			self._node_leaf(cur_node.left_child)
			self._node_leaf(cur_node.right_child)
if __name__ == '__main__':
	tree = Binary_Search_Tree()
	tree.insert(5)
	tree.insert(1)
	tree.insert(-2)
	tree.insert(0)
	tree.insert(8)
	tree.insert(7)
	tree.insert(9)
	tree.print_tree()
	print("\nThe height is " + str(tree.height()))
	print(tree.find(3))
	print(tree.find(12))
	print("Node 2 children is: ",end='')
	tree.node_2_children()
	print("\nNode 1 children is: ",end='')
	tree.node_one_children()
	print("\nNode leaf is: ",end='')
	tree.node_leaf()