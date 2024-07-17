class Node:
    def __init__(self, url):
        self.prev = None
        self.url = url
        self.next = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        newNode = Node(homepage)
        self.home = newNode
        self.curr = self.home

    def visit(self, url: str) -> None:
        newNode = Node(url)
        if self.curr:
            self.curr.next = newNode
            newNode.prev = self.curr
            self.curr = newNode
        return
    
    def back(self, steps: int) -> str:
        curr = self.curr
        while steps > 0 and curr.prev:
            curr = curr.prev
            steps -= 1
        
        self.curr = curr
        return curr.url
        

    def forward(self, steps: int) -> str:
        curr = self.curr
        while steps and curr.next:
            curr = curr.next
            steps -= 1
        self.curr = curr
        return curr.url
            
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)