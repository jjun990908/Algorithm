#include <stdio.h>
#include <stdlib.h>
// #ifndef max
// #define max(a,b) (((a) > (b))? (a) : (b))
// #endif

struct node{
    int data;
    struct node* leftSubTree;
    struct node* rightSubTree;
};
void insert(struct node** root, int data);
void preOrder(struct node* root);
void inOrder(struct node* root);
void postOrder(struct node* root);
int size(struct node* root);
int height(struct node* root);
int sumOfWeight(struct node* root);
int maxPathWeight(struct node* root);
void mirror(struct node** root);
void destruct(struct node** root);

int main()
{
    int numTestCases;

    scanf("%d", &numTestCases);
    while (numTestCases--)
    {
        int num, i;
        struct node* root = NULL;

        scanf("%d",&num);
        for(i = 0; i< num; i++){
            int data;

            scanf("%d", &data);
            insert(&root, data);
        }
        printf("%d\n",size(root));
        printf("%d\n",height(root)-1);
        printf("%d\n",sumOfWeight(root));
        printf("%d\n",maxPathWeight(root));
        mirror(&root);
        preOrder(root); printf("\n");
        inOrder(root); printf("\n");
        postOrder(root); printf("\n");
        destruct(&root);
        if (root == NULL){
            printf("0\n");
        }
        else{
            printf("1\n");
        }
        
    }
    
    return 0;
}


//데이터 삽입(recursion)
void insert(struct node** root, int data){
    struct node* ptr;
    struct node* newnode =malloc(sizeof(struct node));
    newnode->data = data;
    if (*root==NULL){
        *root = newnode;
        return;
    }
    else{
        ptr = *root;
        if(ptr->data>data){
            if(ptr->leftSubTree == NULL){
                ptr->leftSubTree = newnode;
            }
            else{
                insert(&(ptr->leftSubTree),data);
            }
        }
        else{
            if(ptr->rightSubTree == NULL){
                ptr->rightSubTree = newnode;
            }
            else{
                insert(&(ptr->rightSubTree),data);
            }
        }
    }
}

void preOrder(struct node* root){
    if (root == NULL){
        return;
    }
    else {
        printf("%d ",root->data);
        preOrder( root -> leftSubTree);
        preOrder( root -> rightSubTree);
    }
    
}

void inOrder(struct node* root){
    if (root == NULL){
        return;
    }
    else{
        inOrder( root -> leftSubTree);
        printf("%d ",root->data);
        inOrder( root -> rightSubTree);
    }
}

void postOrder(struct node* root){
    if (root == NULL){
        return;
    }
    else {
        postOrder( root -> leftSubTree);
        postOrder( root -> rightSubTree);
        printf("%d ",root->data);
    }
    
}

// 노드의 개수 (recursion)
int size(struct node* root){
    if (root == NULL){
        return 0;
    }
    else {
        return(size(root->leftSubTree) + 1 + size(root->rightSubTree));
    }
}

// 높이 (recursion)
int height(struct node* root){
    if (root == NULL){
        return 0;
    }
    else {
        int left_height = height(root ->leftSubTree);
        int right_height = height(root->rightSubTree);
        if (left_height >= right_height){
            return left_height + 1;
        }
        else {
            return right_height + 1;
        }
    }
}

// 미러 이미지로 변환하기
void mirror (struct node** root){
    struct node *ptr;
    ptr = *root;
    if (ptr ==NULL){
        return;
    }
    else{
        struct node *tmp;
        tmp = ptr->leftSubTree;
        ptr->leftSubTree = ptr->rightSubTree;
        ptr->rightSubTree = tmp;
        mirror(&(ptr->leftSubTree));
        mirror(&(ptr->rightSubTree));
    }
}

// 노드에 저장된 데이터의 값의 합 구하기
int sumOfWeight(struct node* root){
    if(root == NULL){
        return 0;
    }
    else{
        return sumOfWeight(root->leftSubTree)+sumOfWeight(root->rightSubTree)+root->data;
    }
}

// 루트노드부터 단말노드까지의 경로 상의 데이터의 최대 합
int maxPathWeight(struct node* root){
    if(root == NULL){
        return 0;
    }
    else{
        // return root->data + max(maxPathWeight(root->leftSubTree),maxPathWeight(root->rightSubTree));
        int leftWeight,rightWeight;
        leftWeight = maxPathWeight(root->leftSubTree);
        rightWeight = maxPathWeight(root->rightSubTree);
        return root->data + (leftWeight >= rightWeight ? leftWeight : rightWeight);
    }
}

// 트리노드의 동적 메모리 해제하기
void destruct(struct node** root){
    struct node *ptr;
    ptr = *root;
    if(ptr->leftSubTree){
        destruct(&(ptr->leftSubTree));
    }
    if(ptr->rightSubTree){
        destruct(&(ptr->rightSubTree));
    }
    ptr=NULL;
    free((ptr));
    *root=NULL;
}