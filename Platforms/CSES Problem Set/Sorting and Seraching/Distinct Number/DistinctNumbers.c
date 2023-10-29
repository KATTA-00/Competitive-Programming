#include <stdio.h>
#include <stdlib.h>

// Define a structure to represent a hash set
typedef struct HashSet {
    long int key;
    struct HashSet* next;
} HashSet;

// Initialize a new hash set
HashSet* initializeHashSet() {
    return NULL;
}

// Insert an element into the hash set
HashSet* insertIntoHashSet(HashSet* set, long int num) {
    HashSet* newNode = (HashSet*)malloc(sizeof(HashSet));
    newNode->key = num;
    newNode->next = set;
    return newNode;
}

// Check if an element exists in the hash set
int isInHashSet(HashSet* set, long int num) {
    HashSet* current = set;
    while (current != NULL) {
        if (current->key == num) {
            return 1; // Element found
        }
        current = current->next;
    }
    return 0; // Element not found
}

// Calculate the size of the hash set
int sizeOfHashSet(HashSet* set) {
    int size = 0;
    HashSet* current = set;
    while (current != NULL) {
        size++;
        current = current->next;
    }
    return size;
}

// Free memory used by the hash set
void freeHashSet(HashSet* set) {
    HashSet* current = set;
    while (current != NULL) {
        HashSet* temp = current;
        current = current->next;
        free(temp);
    }
}

int main() {
    HashSet* set = initializeHashSet();
    long int n;
    scanf("%ld", &n);
    
    for (int i = 0; i < n; i++) {
        long int num;
        scanf("%ld", &num);
        
        if (!isInHashSet(set, num)) {
            set = insertIntoHashSet(set, num);
        }
    }

    int ans = sizeOfHashSet(set);
    printf("%d\n", ans);

    // Free memory used by the hash set
    freeHashSet(set);

    return 0;
}
