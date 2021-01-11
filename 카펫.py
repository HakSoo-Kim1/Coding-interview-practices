def solution(brown, yellow):
    brown = brown - 4
    for height in range( 1 , yellow + 1):
        width = yellow / height
        if (height * 2) + (width * 2) == brown and width <= height:
            return [height + 2, width + 2]