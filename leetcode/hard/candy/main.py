from typing import List


class Children:
    def __init__(self, rating: int, index: int):
        self.index = index
        self.rating = rating
        self.candy = 1
        self.left = None
        self.right = None

    def serializer(self):
        return {
            "index": self.index,
            "rating": self.rating,
            "candy": self.candy,
            "left": self.left.index if self.left else None,
            "right": self.right.index if self.right else None,
        }


class Solution:
    def candy(self, ratings: List[int]) -> int:
        children_list = self.setChildren(ratings)
        children_list.sort(key=lambda x: x.rating)
        self.setCandy(children_list)
        return sum([child.candy for child in children_list])

    def setCandy(self, children_list: List[Children]):
        for child in children_list:
            if child.left and child.right:
                if (
                    child.left.rating < child.rating
                    and child.right.rating < child.rating
                ):
                    child.candy = max(child.left.candy, child.right.candy) + 1
                elif child.left.rating < child.rating:
                    child.candy = child.left.candy + 1
                elif child.right.rating < child.rating:
                    child.candy = child.right.candy + 1
            elif child.left:
                if child.left.rating < child.rating:
                    child.candy = child.left.candy + 1
                else:
                    child.candy = 1
            elif child.right:
                if child.right.rating < child.rating:
                    child.candy = child.right.candy + 1
                else:
                    child.candy = 1
            else:
                child.candy = 1

    def setChildren(self, ratings: List[int]) -> List[Children]:
        root = Children(ratings[0], 0)
        children_list = [root]
        current = root
        for i, rating in enumerate(ratings[1:]):
            child = Children(rating, i + 1)
            current.right = child
            child.left = current
            current = child
            children_list.append(child)
        return children_list
