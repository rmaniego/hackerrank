read -p "Enter X: " X
read -p "Enter Y: " Y

if (( X < Y )); then
    echo "$X is less than $Y"
elif (( X > Y )); then
    echo "$X is greater than $Y"
else
    echo "$X is equal to $Y"
fi