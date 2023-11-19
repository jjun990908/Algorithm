bar = list(input())
answer = 0
st = []

for i in range(len(bar)):
    if bar[i] == '(':
        st.append('(')

    else:
        if bar[i-1] == '(': 
            st.pop()
            answer += len(st)

        else:
            st.pop() 
            answer += 1 

print(answer)