public class linkedlist {

    private class Node {
        int data = 0;
        Node next = null;

        Node (int data) {
            this.data = data;
        }
    }

    private Node head = null;    
    private Node tail = null;
    private int size = 10;

    public int getSize() {
        return size;
    }

    public boolean isSizeEmpty() {
        return size == 0;
    }

    public void firstNode (int data) {
        Node node = new Node(data);
        addFirstNode(node);
    }
    public void addFirstNode(Node node) {
        if (isSizeEmpty()) {
            this.head = this.tail = node;
        }
        else {
            node.next = this.head;
            this.head = node;
        }
    }

}
