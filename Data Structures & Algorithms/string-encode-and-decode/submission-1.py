class Solution:

    def encode(self, strs: List[str]) -> str:
        sec = 2
        temp_str=""
        for i in strs:
            for j in i:
                temp_str +=chr(ord(j)+sec)
            temp_str+="_#"
        return temp_str
    def decode(self, s: str) -> List[str]:
        sec=2
        new_list=s.split('_#')
        new_list1=[]
        for i in new_list:
            new_str=""
            for j in i:
                new_str +=chr(ord(j)-sec)
            new_list1.append(new_str)
                    
        return new_list1[:-1]