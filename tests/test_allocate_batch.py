from datetime import date

from allocate_batch import OrderedLine, Batch


def test_allocating_to_a_batch_reduce_the_available_quantity():
    batch = Batch("batch_001", "SMALL-TABLE", capability=20, eta=date.today())
    line = OrderedLine("order-ref", "SMALL_TABLE", 2)

    batch.allocate(line)
    assert batch.capability == 18
