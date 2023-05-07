from optibiz import schedule, add_shift, remove_shift, update_shift

def test_add_shift():
    add_shift(1, 'Monday 9am-5pm')
    assert schedule == {1: 'Monday 9am-5pm'}

def test_remove_shift():
    add_shift(1, 'Monday 9am-5pm')
    remove_shift(1)
    assert schedule == {}

def test_update_shift():
    add_shift(1, 'Monday 9am-5pm')
    update_shift(1, 'Monday 10am-6pm')
    assert schedule == {1: 'Monday 10am-6pm'}