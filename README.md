# Longest Common Prefix Finder

This project is a Python solution to find the longest common prefix among a list of strings. It includes a script with sample test cases and instructions on how to run the project locally.

## Features
- Efficiently computes the longest common prefix.
- Handles edge cases such as:
  - An empty list of strings.
  - No common prefix among strings.
- Demonstrates robust testing.

## Prerequisites
- Python 3.6 or higher.

## Project Structure


## How to Run the Project Locally

1. **Clone the Repository**
   ```
   git clone https://github.com/Anuoluwapo25/BLOCKFUSE_test.git
   cd <BLOCKFUSE_test>

python --version

python question1.py

## Example Code

Here’s the Python function used in the project:

```
def longestpre(arrays):
    if not arrays:
        return ""
    
    firstarray = arrays[0]

    for array in arrays[1:]:
        while not array.startswith(firstarray):
            firstarray = firstarray[:-1]
            if not firstarray:
                return ""
    
    return firstarray
```

### Test the function 
```
arrays = [
    ["sunflower", "sunset", "sunday"],
    ["dog", "dot", "dove"],
    ["introduction", "interview", "intermediate"],
    ["banana", "bandana", "bangle"],
    ["coffee"],
    ["apple", "banana", "cherry"]
]

for i, strings in enumerate(arrays, 1):
    result = longestpre(strings)
    print(f"Test case {i}: {strings} -> Longest common prefix: '{result}'")
```


License
This project is licensed under the MIT License.

---

### Steps to Add This to Your Repository
1. Save the content above into a file named `README.md` in your project directory.
2. Push it to GitHub along with your code:
   ```
   git add README.md
   git commit -m "Add README file"
   git push origin main
   
