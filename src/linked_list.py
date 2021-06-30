from cell import Cell


class LinkedList:
    def __init__(self):
        self.top = None

    # データの挿入
    def insert(self, n, x):
        if n == 0 or not self.top:
            self.top = Cell(x, self.top)
        else:
            cp = self.top
            while cp.rest():
                n -= 1
                if n == 0:
                    break
                cp = cp.rest()
            # 新しく追加するセル。データはx,nextはcpのnext
            new_cp = Cell(x, cp.rest())
            # cpのnextはnew_cpになりnew_cpはもともとcpのnextだったものになるので間に追加されたことになる
            cp.set_rest(new_cp)

    # データの削除
    def delete(self, n):
        if n == 0:
            if self.top:
                self.top = self.top.rest()
                return True
        else:
            cp = self.top
            while cp.rest():
                n -= 1
                if n == 0:
                    cp.set_rest(cp.rest().rest())
                    return True
                cp = cp.rest()

        return False

    # データの探索
    def index(self, x):
        n = 0
        cp = self.top
        while cp:
            if cp.first() == x:
                return n
            n += 1
            cp = cp.rest()

        return -1
