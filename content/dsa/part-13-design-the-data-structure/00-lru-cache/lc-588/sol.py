# LC 588. Design In-Memory File System (LeetCode Premium)
# Generalizes the dual-structure design pattern: a tree of hash maps,
# where each Node holds a children dict (path -> Node) plus an optional
# file content string. ls/mkdir/addContentToFile/readContentFromFile.
class _Node:
    __slots__ = ("children", "content")

    def __init__(self) -> None:
        self.children: dict[str, "_Node"] = {}
        self.content: str | None = None  # None for directories; "" or non-empty for files

    @property
    def is_file(self) -> bool:
        return self.content is not None


class FileSystem:
    def __init__(self) -> None:
        self.root = _Node()

    def _walk(self, path: str) -> _Node:
        node = self.root
        if path == "/":
            return node
        for part in path.split("/")[1:]:
            node = node.children.setdefault(part, _Node())
        return node

    def ls(self, path: str) -> list[str]:
        node = self._walk(path)
        if node.is_file:
            # ls on a file path returns the file's basename
            return [path.rsplit("/", 1)[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._walk(path)  # setdefault chain is the make-dir

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._walk(filePath)
        node.content = (node.content or "") + content

    def readContentFromFile(self, filePath: str) -> str:
        return self._walk(filePath).content or ""
