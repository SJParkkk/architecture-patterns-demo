from datetime import date

from allocate_batch import OrderedLine, Batch


def test_allocating_to_a_batch_reduce_the_available_quantity():
    batch = Batch("batch_001", "SMALL-TABLE", capability=20, eta=date.today())
    line = OrderedLine("order-ref", "SMALL_TABLE", 2)
    batch.allocate(line)
    assert batch.capability == 18


def make_batch_and_line():
    batch = Batch("batch_001", "SMALL-TABLE", capability=20, eta=date.today())
    line = OrderedLine("order-ref", "SMALL_TABLE", 2)
    batch.allocate(line)
    unallocated_line = list()
    return batch, unallocated_line


def test_can_deallocate_allocated_line():
    batch, unallocated_line = make_batch_and_line("DECORATIVE-TRINKET", 20, 2)
    batch.deallocated(unallocated_line)

