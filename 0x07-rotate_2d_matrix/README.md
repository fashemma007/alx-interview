<h1 style="text-align: center;">
	<a href='https://intranet.alxswe.com/projects/1220'>
		Rotate 2D Matrix
	</a>
</h1>

Given an `n` x `n` 2D matrix, rotate it 90 degrees clockwise.

* Prototype: `def rotate_2d_matrix(matrix):`
* Do not return anything. The matrix must be edited **in-place**.
* You can assume the matrix will have 2 dimensions and will not be empty.

Test 1
```
imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜
imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜
```
Test 2
```
imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 0, 2, 3],
              [4, 0, 5, 6],
              [4, 0, 5, 6],
              [7, 0, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜
imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜ ./main_0.py
[[7, 4, 4, 1],
[0, 0, 0, 0],
[8, 5, 5, 2], 
[9, 6, 6, 3]]

imitor＠excalibur»alx-interview/0x07-rotate_2d_matrix(main)➜
```

### Author(s)

[**Emmanuel Fasogba**](https://www.linkedin.com/in/emmanuelofasogba/)
- GitHub - [fashemma007](https://github.com/fashemma007)
- Twitter - [@tz_emiwest](https://www.twitter.com/tz_emiwest)
