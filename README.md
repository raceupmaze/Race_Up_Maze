# Race_Up_Maze / ALI DARVISHI

This is an algorithm based on DFS for solving the given mazes.
DFS does not always give you the shortest path but if a path from Start to End exists, it will always find it.

below I'm explaining how my code works:
1. We upload a maze in a .txt format
2. We convert it into a 2D and then 1D array
3. We separate them so we can treat every coordinate individually
4. We find the Start and End location by just searching for 'S' and 'E' sign
5. We switch '.' to 0 and '#' to 1 cause it was easier to work with numbers
6. Ofcourse 0 means a free pass and 1 means a wall
7. We introduce our actions as directions --> UP , DOWN , LEFT , RIGHT
8. We build our function for solving the maze
9. it takes the array as a Maze , the Start position and the End position
10. We measure the number of rows and columns of the maze
11. We define a path list that starts from the Start location and wants to end in the End location, and we define a visited list that stores the coordinates that we have walked through
12. We create a while loop that runs as long as the path list is not empty ( it is clear that both the visited list and the path list have just 1 element in the beginning and its the Start position)
13. We define a current position that is always the last element of the path list
14. We will have a flag (q) , that I will explain later
15. If the current position is the End position that means we are done and we will return path
16. For moving we create a for loop that tries every direction for the current position
17. If the new cordinate is out of the rows and columns boundries it will not get accepted, if the value of that coordinate is 1 ( that means it is a wall) it will not get accepted and if the new coordinate is already in the visited list ( it means we are moving back or we are moving in a loop) it will not get accepted.
18. So if none of the directions can get to a new valid location , that means we have reached a dead spot and we have to get back. Here is where we use q.
19. for every direction q will be set up to 1, and if that value gives us a valid new location q will be set to 0, if none of the directions work for us, q will remain 1 and then out of the for loop we will delete the last element of the path that means we are moving one step back
20. we will continue this loop until we reach the End location or we delete every elements in the path list and that means we did not find any path from Start to End.
21. Then we will create another list named moves that will show us the directions, not the locations from start to end
22. And then we wil decode the moves to human language and print them.

How to execute it?
Its a python file, you can execute it anywhere you want, but I prefer uploading it on colab and then uploading mazes too 
I will provide you with a notebook file too


