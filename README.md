# Misc: List Comprehensions


#### Instructions:
For each of the following tasks, write Python code that solves the problem. Test your code to ensure that it works as expected.

---

1. **Find all of the numbers from 1-100 that are divisible by 7:**
   - Use a loop or list comprehension to find the numbers divisible by 7 between 1 and 100.
   
   **Example output:**
   ```python
   [7, 14, 21, ..., 994]
   ```

2. **Find all of the numbers from 1-100 that have a 3 in them:**
   - Check each number from 1 to 100 and determine if the digit '3' is present.
   
   **Example output:**
   ```python
   [3, 13, 23, ..., 937, 943, 953, 973, 983, 993]
   ```

3. **Count the number of spaces in a string:**
   - Write a function that counts the number of spaces in a given string.
   
   **Example input:**
   ```python
   "Hello world, how are you?"
   ```
   
   **Example output:**
   ```python
   4
   ```

4. **Create a list of all the consonants in the string:**
   - Extract all consonants from the string `"Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams"`.
   
   **Example output:**
   ```python
   ['Y', 'l', 'l', 'w', 'Y', 'k', 's', 'l', 'k', 'y', 'l', ..., 's']
   ```

5. **Get the index and value as a tuple for items in the list:**
   - Given the list `["hi", 4, 8.99, 'apple', ('t,b','n')]`, return a list of tuples containing the index and the value.
   
   **Example output:**
   ```python
   [(0, "hi"), (1, 4), (2, 8.99), (3, 'apple'), (4, ('t,b','n'))]
   ```

6. **Find the common numbers in two lists (without using a tuple or set):**
   - Given `list_a = [1, 2, 3, 4]` and `list_b = [2, 3, 4, 5]`, find the numbers that are present in both lists.
   
   **Example output:**
   ```python
   [2, 3, 4]
   ```

7. **Produce a list of tuples consisting of only the matching numbers in these lists:**
   - Given `list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]` and `list_b = [2, 7, 1, 12]`, find the numbers that are in both lists and return them as tuples.
   
   **Example output:**
   ```python
   [(1, 1), (2, 2), (7, 7)]
   ```

8. **Find all of the words in a string that are less than 4 letters:**
    - Write a function that extracts words from a string that are less than 4 letters long.
    
    **Example input:**
    ```python
    "The quick brown fox jumps over the lazy dog"
    ```
    
    **Example output:**
    ```python
    ['The', 'fox', 'the', 'dog']
    ```

