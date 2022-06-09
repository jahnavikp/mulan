string1="low"
string2="owl"
sortingstring1=[string1[i] for i in range(0,len(string1))]
sortingstring1.sort()
sortingstring2=[string2[i] for i in range(0,len(string2))]
sortingstring2.sort()
if (sortingstring1==sortingstring2):
   print("given strings are anagrams.")
else: 
   print("given strings aren't anagrams.")
