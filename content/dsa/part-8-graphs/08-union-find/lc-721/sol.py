# LC 721. Accounts Merge
# String-keyed Union-Find: parent map is dict[str, str]. Each email is a
# node; for each account, union all of its emails into one set; finally
# group emails by their find-root and re-attach the owner name.
from typing import List
from collections import defaultdict


class DSU:
    def __init__(self) -> None:
        self.parent: dict = {}
        self.rank: dict = {}

    def make(self, x: str) -> None:
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x: str) -> str:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """LC 721: merge accounts that share at least one email; return the
    merged accounts with each email list sorted, owner name first."""
    dsu = DSU()
    email_to_name: dict = {}

    for account in accounts:
        name = account[0]
        first = account[1]
        dsu.make(first)
        email_to_name[first] = name
        for email in account[2:]:
            dsu.make(email)
            email_to_name[email] = name
            dsu.union(first, email)

    groups: dict = defaultdict(list)
    for email in email_to_name:
        groups[dsu.find(email)].append(email)

    return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]
