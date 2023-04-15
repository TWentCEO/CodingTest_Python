class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.next = next
        self.val = val
        self.prev = prev
class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val = homepage)
    def visited(self, url):
        self.current.next = ListNode(val = url, prev=self.current)
        self.current = self.current.next
    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        return self.current.val
    def back(self, steps):
        while steps < 0 and self.current.prev is not None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val



