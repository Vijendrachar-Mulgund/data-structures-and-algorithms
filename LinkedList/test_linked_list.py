import pytest
from linked_list import Node, LinkedList


# ──────────────────────────────────────────────
# Node — constructor
# ──────────────────────────────────────────────

class TestNode:
    # Node stores the value passed to its constructor
    def test_node_has_value(self):
        node = Node(10)
        assert node.value == 10

    # A newly created node should not point to any other node
    def test_node_next_is_none(self):
        node = Node(10)
        assert node.next is None

    # Node should accept any data type as its value
    def test_node_with_different_types(self):
        assert Node("hello").value == "hello"
        assert Node(3.14).value == 3.14
        assert Node(None).value is None


# ──────────────────────────────────────────────
# LinkedList — constructor
# ──────────────────────────────────────────────

class TestLinkedListConstructor:
    # Constructor creates a node and sets it as head
    def test_head_is_node_with_value(self):
        ll = LinkedList(4)
        assert ll.head.value == 4

    # Constructor creates a node and sets it as tail
    def test_tail_is_node_with_value(self):
        ll = LinkedList(4)
        assert ll.tail.value == 4

    # With one element, head and tail should reference the same node
    def test_head_and_tail_are_same_node(self):
        ll = LinkedList(4)
        assert ll.head is ll.tail

    # A new list with one node should have length 1
    def test_length_is_one(self):
        ll = LinkedList(4)
        assert ll.length == 1

    # The single node in a new list should not point to anything
    def test_head_next_is_none(self):
        ll = LinkedList(4)
        assert ll.head.next is None


# ──────────────────────────────────────────────
# print_list
# ──────────────────────────────────────────────

class TestPrintList:
    # Printing a one-element list outputs just that value
    def test_print_single_element(self, capsys):
        ll = LinkedList(1)
        ll.print_list()
        assert capsys.readouterr().out == "1\n"

    # Printing a multi-element list outputs each value on its own line
    def test_print_multiple_elements(self, capsys):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.print_list()
        assert capsys.readouterr().out == "1\n2\n3\n"


# ──────────────────────────────────────────────
# append
# ──────────────────────────────────────────────

class TestAppend:
    # Appended node becomes the new tail
    def test_append_adds_to_end(self):
        ll = LinkedList(1)
        ll.append(2)
        assert ll.tail.value == 2

    # Head stays the same while tail moves to the appended node
    def test_append_updates_tail(self):
        ll = LinkedList(1)
        ll.append(2)
        assert ll.head.value == 1
        assert ll.tail.value == 2
        assert ll.head is not ll.tail

    # The old tail's next pointer should link to the new tail
    def test_append_links_nodes(self):
        ll = LinkedList(1)
        ll.append(2)
        assert ll.head.next is ll.tail

    # Each append should increase length by 1
    def test_append_increments_length(self):
        ll = LinkedList(1)
        ll.append(2)
        assert ll.length == 2
        ll.append(3)
        assert ll.length == 3

    # Multiple appends should maintain insertion order
    def test_append_multiple_preserves_order(self, capsys):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        ll.append(40)
        ll.print_list()
        assert capsys.readouterr().out == "10\n20\n30\n40\n"

    # The last node in the list should always have next as None
    def test_append_tail_next_is_none(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        assert ll.tail.next is None


# ──────────────────────────────────────────────
# pop
# ──────────────────────────────────────────────

class TestPop:
    # Popping from an empty list should return None
    def test_pop_empty_list_returns_none(self):
        ll = LinkedList(1)
        ll.pop()
        assert ll.pop() is None

    # Pop should return the removed tail node
    def test_pop_returns_removed_node(self):
        ll = LinkedList(1)
        ll.append(2)
        removed = ll.pop()
        assert removed.value == 2

    # After pop, the second-to-last node becomes the new tail
    def test_pop_updates_tail(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.pop()
        assert ll.tail.value == 2

    # New tail's next should be None after pop
    def test_pop_new_tail_next_is_none(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.pop()
        assert ll.tail.next is None

    # Pop should decrease the length by 1
    def test_pop_decrements_length(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.pop()
        assert ll.length == 1

    # Popping the only element should set head and tail to None
    def test_pop_single_element_sets_head_and_tail_to_none(self):
        ll = LinkedList(1)
        removed = ll.pop()
        assert removed.value == 1
        assert ll.head is None
        assert ll.tail is None
        assert ll.length == 0

    # Popping all elements one by one should empty the list
    def test_pop_all_elements(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        assert ll.pop().value == 3
        assert ll.pop().value == 2
        assert ll.pop().value == 1
        assert ll.pop() is None
        assert ll.length == 0


# ──────────────────────────────────────────────
# prepend
# ──────────────────────────────────────────────

class TestPrepend:
    # Prepend should add a node at the beginning, making it the new head
    def test_prepend_updates_head(self):
        ll = LinkedList(2)
        ll.prepend(1)
        assert ll.head.value == 1

    # The new head's next should point to the old head
    def test_prepend_links_to_old_head(self):
        ll = LinkedList(2)
        ll.prepend(1)
        assert ll.head.next.value == 2

    # Tail should remain unchanged after prepend
    def test_prepend_tail_unchanged(self):
        ll = LinkedList(2)
        ll.prepend(1)
        assert ll.tail.value == 2

    # Prepend should increase length by 1
    def test_prepend_increments_length(self):
        ll = LinkedList(2)
        ll.prepend(1)
        assert ll.length == 2

    # Prepend should return True on success
    def test_prepend_returns_true(self):
        ll = LinkedList(2)
        assert ll.prepend(1) is True

    # Prepending to an empty list should set both head and tail to the new node
    def test_prepend_to_empty_list(self):
        ll = LinkedList(1)
        ll.pop()  # empty the list
        ll.prepend(10)
        assert ll.head.value == 10
        assert ll.tail.value == 10
        assert ll.head is ll.tail
        assert ll.length == 1

    # Multiple prepends should maintain reverse insertion order
    def test_prepend_multiple_preserves_order(self, capsys):
        ll = LinkedList(4)
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        ll.print_list()
        assert capsys.readouterr().out == "1\n2\n3\n4\n"


# ──────────────────────────────────────────────
# pop_first
# ──────────────────────────────────────────────

class TestPopFirst:
    # Pop first from an empty list should return None
    def test_pop_first_empty_list_returns_none(self):
        ll = LinkedList(1)
        ll.pop()
        assert ll.pop_first() is None

    # Pop first should return the removed head node
    def test_pop_first_returns_removed_node(self):
        ll = LinkedList(1)
        ll.append(2)
        removed = ll.pop_first()
        assert removed.value == 1

    # After pop first, the second node becomes the new head
    def test_pop_first_updates_head(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.pop_first()
        assert ll.head.value == 2

    # The removed node should be disconnected (next set to None)
    def test_pop_first_disconnects_removed_node(self):
        ll = LinkedList(1)
        ll.append(2)
        removed = ll.pop_first()
        assert removed.next is None

    # Pop first should decrease the length by 1
    def test_pop_first_decrements_length(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.pop_first()
        assert ll.length == 1

    # Popping the only element should set head and tail to None
    def test_pop_first_single_element_sets_head_and_tail_to_none(self):
        ll = LinkedList(1)
        removed = ll.pop_first()
        assert removed.value == 1
        assert ll.head is None
        assert ll.tail is None
        assert ll.length == 0

    # Popping all elements from the front one by one should empty the list
    def test_pop_first_all_elements(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        assert ll.pop_first().value == 1
        assert ll.pop_first().value == 2
        assert ll.pop_first().value == 3
        assert ll.pop_first() is None
        assert ll.length == 0


# ──────────────────────────────────────────────
# get
# ──────────────────────────────────────────────

class TestGet:
    # Get should return the node at the given index
    def test_get_first_node(self):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        assert ll.get(0).value == 10

    # Get should traverse to the correct middle node
    def test_get_middle_node(self):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        assert ll.get(1).value == 20

    # Get should return the last node at index length-1
    def test_get_last_node(self):
        ll = LinkedList(10)
        ll.append(20)
        ll.append(30)
        assert ll.get(2).value == 30

    # Negative index is out of bounds and should return None
    def test_get_negative_index_returns_none(self):
        ll = LinkedList(1)
        assert ll.get(-1) is None

    # Index equal to length is out of bounds and should return None
    def test_get_index_equal_to_length_returns_none(self):
        ll = LinkedList(1)
        assert ll.get(1) is None

    # Index greater than length is out of bounds and should return None
    def test_get_index_beyond_length_returns_none(self):
        ll = LinkedList(1)
        assert ll.get(5) is None

    # Get should return the actual node object, not just the value
    def test_get_returns_node_not_value(self):
        ll = LinkedList(10)
        node = ll.get(0)
        assert isinstance(node, Node)


# ──────────────────────────────────────────────
# set_value
# ──────────────────────────────────────────────

class TestSetValue:
    # set_value should update the value of the node at the given index
    def test_set_value_updates_node(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.set_value(1, 20)
        assert ll.get(1).value == 20

    # set_value should return True when the update is successful
    def test_set_value_returns_true(self):
        ll = LinkedList(1)
        assert ll.set_value(0, 10) is True

    # set_value should return False for a negative index
    def test_set_value_negative_index_returns_false(self):
        ll = LinkedList(1)
        assert ll.set_value(-1, 10) is False

    # set_value should return False for an index beyond the list
    def test_set_value_out_of_bounds_returns_false(self):
        ll = LinkedList(1)
        assert ll.set_value(5, 10) is False

    # set_value should not change other nodes in the list
    def test_set_value_does_not_affect_other_nodes(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.set_value(1, 99)
        assert ll.get(0).value == 1
        assert ll.get(2).value == 3

    # set_value should work on the head node
    def test_set_value_on_head(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.set_value(0, 100)
        assert ll.head.value == 100

    # set_value should work on the tail node
    def test_set_value_on_tail(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.set_value(1, 200)
        assert ll.tail.value == 200


# ──────────────────────────────────────────────
# insert
# ──────────────────────────────────────────────

class TestInsert:
    # Inserting at index 0 should prepend and update head
    def test_insert_at_beginning(self):
        ll = LinkedList(2)
        ll.append(3)
        ll.insert(0, 1)
        assert ll.head.value == 1
        assert ll.head.next.value == 2
        assert ll.length == 3

    # Inserting at index equal to length should append and update tail
    def test_insert_at_end(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.insert(2, 3)
        assert ll.tail.value == 3
        assert ll.length == 3

    # Inserting in the middle should place the node at the correct position
    def test_insert_in_middle(self):
        ll = LinkedList(1)
        ll.append(3)
        ll.insert(1, 2)
        assert ll.get(0).value == 1
        assert ll.get(1).value == 2
        assert ll.get(2).value == 3

    # The previous node's next should point to the newly inserted node
    def test_insert_links_previous_to_new_node(self):
        ll = LinkedList(1)
        ll.append(3)
        ll.insert(1, 2)
        assert ll.get(0).next.value == 2

    # The newly inserted node's next should point to the node that was at that index
    def test_insert_links_new_node_to_next(self):
        ll = LinkedList(1)
        ll.append(3)
        ll.insert(1, 2)
        assert ll.get(1).next.value == 3

    # Insert should increment the length by 1
    def test_insert_increments_length(self):
        ll = LinkedList(1)
        ll.append(3)
        ll.insert(1, 2)
        assert ll.length == 3

    # Insert should return True on successful insertion
    def test_insert_returns_true(self):
        ll = LinkedList(1)
        assert ll.insert(0, 0) is True
        assert ll.insert(2, 2) is True
        assert ll.insert(1, 99) is True

    # Negative index is out of bounds and should return False
    def test_insert_negative_index_returns_false(self):
        ll = LinkedList(1)
        assert ll.insert(-1, 10) is False

    # Index greater than length is out of bounds and should return False
    def test_insert_index_beyond_length_returns_false(self):
        ll = LinkedList(1)
        assert ll.insert(5, 10) is False

    # Inserting at index 0 on an empty list should set both head and tail
    def test_insert_into_empty_list(self):
        ll = LinkedList(1)
        ll.pop()  # empty the list
        ll.insert(0, 42)
        assert ll.head.value == 42
        assert ll.tail.value == 42
        assert ll.head is ll.tail
        assert ll.length == 1

    # Inserting at beginning should not change the tail
    def test_insert_at_beginning_tail_unchanged(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.insert(0, 0)
        assert ll.tail.value == 2

    # Inserting at end should not change the head
    def test_insert_at_end_head_unchanged(self):
        ll = LinkedList(1)
        ll.append(2)
        ll.insert(2, 3)
        assert ll.head.value == 1

    # Tail's next should remain None after inserting at the end
    def test_insert_at_end_tail_next_is_none(self):
        ll = LinkedList(1)
        ll.insert(1, 2)
        assert ll.tail.next is None

    # Multiple inserts at various positions should produce the correct order
    def test_insert_multiple_positions(self, capsys):
        ll = LinkedList(1)
        ll.append(5)
        ll.insert(1, 3)   # [1, 3, 5]
        ll.insert(1, 2)   # [1, 2, 3, 5]
        ll.insert(3, 4)   # [1, 2, 3, 4, 5]
        ll.print_list()
        assert capsys.readouterr().out == "1\n2\n3\n4\n5\n"
        assert ll.length == 5


# # ──────────────────────────────────────────────
# # remove
# # ──────────────────────────────────────────────

# class TestRemove:
#     # Removing the first node should use pop_first behavior and update head
#     def test_remove_at_beginning(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         removed = ll.remove(0)
#         assert removed.value == 1
#         assert ll.head.value == 2

#     # Removing the last node should use pop behavior and update tail
#     def test_remove_at_end(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         removed = ll.remove(2)
#         assert removed.value == 3
#         assert ll.tail.value == 2

#     # Removing a middle node should return the correct node
#     def test_remove_in_middle(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         removed = ll.remove(1)
#         assert removed.value == 2

#     # After removing a middle node, the previous node should link to the next one
#     def test_remove_middle_links_correctly(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.remove(1)
#         assert ll.get(0).next.value == 3

#     # Remove should decrement the length by 1
#     def test_remove_decrements_length(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.remove(1)
#         assert ll.length == 2

#     # Negative index is out of bounds and should return None
#     def test_remove_negative_index_returns_none(self):
#         ll = LinkedList(1)
#         assert ll.remove(-1) is None

#     # Index equal to length is out of bounds and should return None
#     def test_remove_index_equal_to_length_returns_none(self):
#         ll = LinkedList(1)
#         assert ll.remove(1) is None

#     # Index greater than length is out of bounds and should return None
#     def test_remove_index_beyond_length_returns_none(self):
#         ll = LinkedList(1)
#         assert ll.remove(5) is None

#     # Removing the only element should set head and tail to None
#     def test_remove_single_element(self):
#         ll = LinkedList(1)
#         removed = ll.remove(0)
#         assert removed.value == 1
#         assert ll.head is None
#         assert ll.tail is None
#         assert ll.length == 0

#     # The removed node should be disconnected (next set to None)
#     def test_remove_disconnects_node(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         removed = ll.remove(1)
#         assert removed.next is None

#     # Removing from an empty list should return None
#     def test_remove_from_empty_list_returns_none(self):
#         ll = LinkedList(1)
#         ll.pop()  # empty the list
#         assert ll.remove(0) is None

#     # Removing the last node should ensure tail's next is None
#     def test_remove_at_end_tail_next_is_none(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.remove(2)
#         assert ll.tail.next is None

#     # Removing all elements one by one should empty the list
#     def test_remove_all_elements(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         assert ll.remove(1).value == 2  # [1, 3]
#         assert ll.remove(1).value == 3  # [1]
#         assert ll.remove(0).value == 1  # []
#         assert ll.length == 0
#         assert ll.head is None
#         assert ll.tail is None

#     # After middle removal, remaining values should be in the correct order
#     def test_remove_middle_preserves_order(self, capsys):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.append(4)
#         ll.remove(2)  # remove value 3
#         ll.print_list()
#         assert capsys.readouterr().out == "1\n2\n4\n"


# # ──────────────────────────────────────────────
# # reverse
# # ──────────────────────────────────────────────

# class TestReverse:
#     # Reversing should swap head and tail
#     def test_reverse_swaps_head_and_tail(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.reverse()
#         assert ll.head.value == 3
#         assert ll.tail.value == 1

#     # After reversing, traversal order should be reversed
#     def test_reverse_reverses_order(self, capsys):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.append(4)
#         ll.reverse()
#         ll.print_list()
#         assert capsys.readouterr().out == "4\n3\n2\n1\n"

#     # Reverse should not change the length
#     def test_reverse_preserves_length(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.reverse()
#         assert ll.length == 3

#     # Reversing a single-element list should keep head and tail the same
#     def test_reverse_single_element(self):
#         ll = LinkedList(1)
#         ll.reverse()
#         assert ll.head.value == 1
#         assert ll.tail.value == 1
#         assert ll.head is ll.tail
#         assert ll.length == 1

#     # After reversing, head's next should point to the correct node
#     def test_reverse_head_next(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.reverse()
#         assert ll.head.next.value == 2

#     # After reversing, tail's next should be None
#     def test_reverse_tail_next_is_none(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.reverse()
#         assert ll.tail.next is None

#     # Reversing twice should restore the original order
#     def test_reverse_twice_restores_order(self, capsys):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.reverse()
#         ll.reverse()
#         ll.print_list()
#         assert capsys.readouterr().out == "1\n2\n3\n"

#     # Reversing a two-element list should swap the two nodes
#     def test_reverse_two_elements(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.reverse()
#         assert ll.head.value == 2
#         assert ll.tail.value == 1
#         assert ll.head.next is ll.tail
#         assert ll.tail.next is None

#     # All internal links should point backwards after reverse
#     def test_reverse_all_links(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         ll.append(4)
#         ll.reverse()
#         assert ll.get(0).value == 4
#         assert ll.get(1).value == 3
#         assert ll.get(2).value == 2
#         assert ll.get(3).value == 1

#     # Reverse should not create new nodes or modify values
#     def test_reverse_does_not_create_new_nodes(self):
#         ll = LinkedList(1)
#         ll.append(2)
#         ll.append(3)
#         original_head = ll.head
#         original_tail = ll.tail
#         ll.reverse()
#         # old head is now the tail, old tail is now the head
#         assert ll.tail is original_head
#         assert ll.head is original_tail
