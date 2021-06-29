from cell import Cell


def test_nextがないcell():
    x = 1
    first_cell = Cell(x)
    assert first_cell.rest() == None
    assert first_cell.first() == x


def test_要素に破壊的な代入():
    x = 1
    cell = Cell(x)
    assert cell.first() == x
    y = 2
    cell.set_first(y)
    assert cell.first() == y


def test_nextを設定():
    x = 1
    top = Cell(x)
    cell = Cell(x, top)
    assert cell.rest() == top


def test_set_rest_set_first():
    x = 1
    top = Cell(x)
    y = 2
    cell = Cell(y, top)
    assert cell.rest() == top
    assert cell.first() == y

    cell.set_first(y)
    assert cell.first() == y

    z = 3
    another = Cell(z)
    cell.set_rest(another)
    assert cell.rest() == another
