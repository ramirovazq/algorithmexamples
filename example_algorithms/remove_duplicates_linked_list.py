def removeDuplicates(head):
    #print("...........")
    #dictionary_nodes = {}
    #final_list = []
    node = head 
    while True:
        try:
            actual_node = node
            next_node   = node.next
            if actual_node.data == next_node.data: # is repeated
                node.next = next_node.next
            else:
                node = next_node
        except AttributeError: # is the end of the list
            break
    return head
