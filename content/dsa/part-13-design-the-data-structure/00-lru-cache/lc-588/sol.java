// LC 588. Design In-Memory File System (LeetCode Premium)
// Generalizes the dual-structure pattern: a trie of TreeMap nodes
// (alphabetical order is part of the ls contract).
import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

class FileSystem {
    private static final class Node {
        final TreeMap<String, Node> children = new TreeMap<>();
        StringBuilder content = null; // null = directory; non-null = file
        boolean isFile() { return content != null; }
    }

    private final Node root = new Node();

    private Node walk(String path) {
        Node node = root;
        if (path.equals("/")) return node;
        for (String part : path.substring(1).split("/")) {
            node = node.children.computeIfAbsent(part, k -> new Node());
        }
        return node;
    }

    public List<String> ls(String path) {
        Node node = walk(path);
        if (node.isFile()) {
            String[] parts = path.split("/");
            List<String> out = new ArrayList<>();
            out.add(parts[parts.length - 1]);
            return out;
        }
        return new ArrayList<>(node.children.keySet());
    }

    public void mkdir(String path) {
        walk(path);
    }

    public void addContentToFile(String filePath, String content) {
        Node node = walk(filePath);
        if (node.content == null) node.content = new StringBuilder();
        node.content.append(content);
    }

    public String readContentFromFile(String filePath) {
        Node node = walk(filePath);
        return node.content == null ? "" : node.content.toString();
    }
}
