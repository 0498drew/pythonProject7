janet = {'x_axis': 22, 'y_axis': 5, 'speed': 'medium'}

# move janet to the right
# determine how far to move janet based on her speed
if janet('speed') == 'slow':
    x_increment = 1
elif janet('speed') == 'medium':
    x_increment = 2
else:
    # Janet must be fast.
    x_increment = 3

# Janet's new position is the old position plus an incremet
janet['x_axis'] = janet['x_axis'] + x_increment
print("new x_axis:" + str(janet['x_axis']))