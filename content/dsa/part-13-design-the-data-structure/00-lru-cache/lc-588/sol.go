// LC 588. Design In-Memory File System (LeetCode Premium)
// Generalizes the dual-structure pattern: tree of map[string]*node
// with sort.Strings to honor ls's alphabetical contract.
package main

import (
	"sort"
	"strings"
)

type fsNode struct {
	children map[string]*fsNode
	content  string
	isFile   bool
}

type FileSystem struct {
	root *fsNode
}

func ConstructorFileSystem() FileSystem {
	return FileSystem{root: &fsNode{children: make(map[string]*fsNode)}}
}

func (fs *FileSystem) walk(path string) *fsNode {
	node := fs.root
	if path == "/" {
		return node
	}
	for _, part := range strings.Split(path[1:], "/") {
		child, ok := node.children[part]
		if !ok {
			child = &fsNode{children: make(map[string]*fsNode)}
			node.children[part] = child
		}
		node = child
	}
	return node
}

func (fs *FileSystem) Ls(path string) []string {
	node := fs.walk(path)
	if node.isFile {
		i := strings.LastIndex(path, "/")
		return []string{path[i+1:]}
	}
	out := make([]string, 0, len(node.children))
	for name := range node.children {
		out = append(out, name)
	}
	sort.Strings(out)
	return out
}

func (fs *FileSystem) Mkdir(path string) {
	fs.walk(path)
}

func (fs *FileSystem) AddContentToFile(filePath, content string) {
	node := fs.walk(filePath)
	node.isFile = true
	node.content += content
}

func (fs *FileSystem) ReadContentFromFile(filePath string) string {
	return fs.walk(filePath).content
}
