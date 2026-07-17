class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[0]
        fleet=0
        time=0
        temp={}
        for j in range(len(speed)):
            temp[position[j]]=speed[j]
        sorted_by_key = dict(sorted(temp.items(), reverse=True))

        for i in sorted_by_key:
            time = (target-i)/sorted_by_key[i]
            if time>stack[-1]:
                stack.append(time)
            
            
        return len(set(stack))-1